import os
import hashlib
import magic
import shutil
from typing import Dict, Any, List
from fastapi import UploadFile
from ..models.sample import Sample, FileType
from ..main import app

class FileService:
    def __init__(self):
        self.upload_dir = app.settings.UPLOAD_DIR
        self.db = app.mongodb

    async def save_upload_file(self, file: UploadFile) -> str:
        """Save uploaded file to disk and return its path"""
        file_path = os.path.join(self.upload_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file_path

    async def get_file_info(self, file_path: str) -> Dict[str, Any]:
        """Get file information including hashes and type"""
        # Calculate hashes
        md5_hash = hashlib.md5()
        sha1_hash = hashlib.sha1()
        sha256_hash = hashlib.sha256()
        
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                md5_hash.update(chunk)
                sha1_hash.update(chunk)
                sha256_hash.update(chunk)
        
        # Get file type using python-magic
        mime = magic.Magic(mime=True)
        file_type = mime.from_file(file_path)
        
        # Determine file type
        if "application/x-dosexec" in file_type:
            file_type_enum = FileType.PE
        elif "application/x-executable" in file_type:
            file_type_enum = FileType.ELF
        else:
            file_type_enum = FileType.OTHER
        
        return {
            "filename": os.path.basename(file_path),
            "file_type": file_type_enum,
            "size": os.path.getsize(file_path),
            "md5": md5_hash.hexdigest(),
            "sha1": sha1_hash.hexdigest(),
            "sha256": sha256_hash.hexdigest()
        }

    async def save_sample(self, sample: Sample) -> str:
        """Save sample information to database"""
        result = await self.db.samples.insert_one(sample.dict(by_alias=True))
        return str(result.inserted_id)

    async def get_sample(self, sample_id: str, user_id: str = None) -> Dict[str, Any]:
        """Get sample information from database"""
        query = {"_id": sample_id}
        if user_id:
            query["user_id"] = user_id
        sample = await self.db.samples.find_one(query)
        if sample:
            sample["_id"] = str(sample["_id"])
        return sample

    async def list_samples(self, skip: int, limit: int, user_id: str = None) -> List[Dict[str, Any]]:
        """List samples with pagination"""
        query = {}
        if user_id:
            query["user_id"] = user_id
        
        cursor = self.db.samples.find(query).skip(skip).limit(limit)
        samples = []
        async for sample in cursor:
            sample["_id"] = str(sample["_id"])
            samples.append(sample)
        return samples

    async def delete_sample(self, sample_id: str, user_id: str = None) -> bool:
        """Delete sample from database and filesystem"""
        query = {"_id": sample_id}
        if user_id:
            query["user_id"] = user_id
        
        sample = await self.db.samples.find_one(query)
        if not sample:
            return False
        
        # Delete file from filesystem
        file_path = os.path.join(self.upload_dir, sample["filename"])
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Delete from database
        result = await self.db.samples.delete_one(query)
        return result.deleted_count > 0 