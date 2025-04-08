from typing import Optional, List, Dict, Any
from .base import BaseDBModel

class StaticAnalysis(BaseDBModel):
    sample_id: str
    file_info: Dict[str, Any]
    strings: List[str]
    imports: List[str]
    exports: List[str]
    sections: List[Dict[str, Any]]
    resources: List[Dict[str, Any]]
    yara_matches: List[Dict[str, Any]]
    entropy: Dict[str, float]
    pe_header: Optional[Dict[str, Any]] = None
    elf_header: Optional[Dict[str, Any]] = None
    suspicious_indicators: List[Dict[str, Any]]
    metadata: Dict[str, Any]

class DynamicAnalysis(BaseDBModel):
    sample_id: str
    execution_time: float
    system_calls: List[Dict[str, Any]]
    file_operations: List[Dict[str, Any]]
    registry_operations: List[Dict[str, Any]]
    network_connections: List[Dict[str, Any]]
    process_tree: List[Dict[str, Any]]
    dropped_files: List[Dict[str, Any]]
    memory_dumps: List[str]
    screenshots: List[str]
    artifacts: List[Dict[str, Any]]
    sandbox_info: Dict[str, Any]
    error_logs: List[str] 