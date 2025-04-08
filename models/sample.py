from typing import Optional, List
from enum import Enum
from .base import BaseDBModel

class FileType(str, Enum):
    PE = "pe"
    ELF = "elf"
    OTHER = "other"

class AnalysisStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class Sample(BaseDBModel):
    filename: str
    original_name: str
    file_type: FileType
    size: int
    md5: str
    sha1: str
    sha256: str
    status: AnalysisStatus = AnalysisStatus.PENDING
    user_id: Optional[str] = None
    tags: List[str] = []
    static_analysis_id: Optional[str] = None
    dynamic_analysis_id: Optional[str] = None
    classification_id: Optional[str] = None
    is_malicious: Optional[bool] = None
    confidence_score: Optional[float] = None
    malware_family: Optional[str] = None
    notes: Optional[str] = None 