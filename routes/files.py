from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from typing import List
import hashlib
import os
import magic
from ..models.sample import Sample, FileType, AnalysisStatus
from ..services.file_service import FileService
from ..services.analysis_service import AnalysisService
from ..utils.security import get_current_user

router = APIRouter()
file_service = FileService()
analysis_service = AnalysisService()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None,
    current_user: dict = Depends(get_current_user)
):
    try:
        # Save file temporarily
        file_path = await file_service.save_upload_file(file)
        
        # Get file information
        file_info = await file_service.get_file_info(file_path)
        
        # Create sample record
        sample = Sample(
            filename=file_info["filename"],
            original_name=file.filename,
            file_type=file_info["file_type"],
            size=file_info["size"],
            md5=file_info["md5"],
            sha1=file_info["sha1"],
            sha256=file_info["sha256"],
            user_id=current_user.get("id")
        )
        
        # Save to database
        sample_id = await file_service.save_sample(sample)
        
        # Schedule analysis tasks
        if background_tasks:
            background_tasks.add_task(analysis_service.start_static_analysis, sample_id)
            background_tasks.add_task(analysis_service.start_dynamic_analysis, sample_id)
        
        return JSONResponse(
            status_code=201,
            content={
                "message": "File uploaded successfully",
                "sample_id": str(sample_id),
                "file_info": file_info
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def list_files(
    skip: int = 0,
    limit: int = 10,
    current_user: dict = Depends(get_current_user)
):
    try:
        files = await file_service.list_samples(skip, limit, current_user.get("id"))
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{sample_id}")
async def delete_file(
    sample_id: str,
    current_user: dict = Depends(get_current_user)
):
    try:
        success = await file_service.delete_sample(sample_id, current_user.get("id"))
        if not success:
            raise HTTPException(status_code=404, detail="File not found")
        return {"message": "File deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{sample_id}")
async def get_file(
    sample_id: str,
    current_user: dict = Depends(get_current_user)
):
    try:
        file_info = await file_service.get_sample(sample_id, current_user.get("id"))
        if not file_info:
            raise HTTPException(status_code=404, detail="File not found")
        return file_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 