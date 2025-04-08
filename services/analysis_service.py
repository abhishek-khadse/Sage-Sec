import os
import pefile
import yara
import magic
from typing import Dict, Any
from ..models.analysis import StaticAnalysis, DynamicAnalysis
from ..models.sample import AnalysisStatus
from ..main import app
import subprocess
import json
import tempfile
import shutil

class AnalysisService:
    def __init__(self):
        self.db = app.mongodb
        self.upload_dir = app.settings.UPLOAD_DIR

    async def start_static_analysis(self, sample_id: str):
        """Start static analysis of a sample"""
        try:
            # Get sample information
            sample = await self.db.samples.find_one({"_id": sample_id})
            if not sample:
                return

            # Update status
            await self.db.samples.update_one(
                {"_id": sample_id},
                {"$set": {"status": AnalysisStatus.IN_PROGRESS}}
            )

            # Get file path
            file_path = os.path.join(self.upload_dir, sample["filename"])

            # Perform static analysis
            static_analysis = await self._perform_static_analysis(file_path)
            static_analysis["sample_id"] = sample_id

            # Save results
            result = await self.db.static_analysis.insert_one(static_analysis)
            static_analysis_id = str(result.inserted_id)

            # Update sample with static analysis ID
            await self.db.samples.update_one(
                {"_id": sample_id},
                {
                    "$set": {
                        "static_analysis_id": static_analysis_id,
                        "status": AnalysisStatus.COMPLETED
                    }
                }
            )

        except Exception as e:
            # Update status to failed
            await self.db.samples.update_one(
                {"_id": sample_id},
                {"$set": {"status": AnalysisStatus.FAILED}}
            )
            raise e

    async def _perform_static_analysis(self, file_path: str) -> Dict[str, Any]:
        """Perform static analysis on a file"""
        analysis = {
            "file_info": {},
            "strings": [],
            "imports": [],
            "exports": [],
            "sections": [],
            "resources": [],
            "yara_matches": [],
            "entropy": {},
            "suspicious_indicators": [],
            "metadata": {}
        }

        # Get basic file info
        mime = magic.Magic()
        analysis["file_info"]["mime_type"] = mime.from_file(file_path)
        analysis["file_info"]["size"] = os.path.getsize(file_path)

        # Try PE analysis
        try:
            pe = pefile.PE(file_path)
            analysis["pe_header"] = {
                "machine": hex(pe.FILE_HEADER.Machine),
                "timestamp": pe.FILE_HEADER.TimeDateStamp,
                "characteristics": hex(pe.FILE_HEADER.Characteristics)
            }

            # Get imports
            if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
                for entry in pe.DIRECTORY_ENTRY_IMPORT:
                    for imp in entry.imports:
                        if imp.name:
                            analysis["imports"].append(imp.name.decode())

            # Get exports
            if hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
                for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                    if exp.name:
                        analysis["exports"].append(exp.name.decode())

            # Get sections
            for section in pe.sections:
                analysis["sections"].append({
                    "name": section.Name.decode().rstrip('\x00'),
                    "virtual_address": hex(section.VirtualAddress),
                    "virtual_size": hex(section.Misc_VirtualSize),
                    "raw_size": hex(section.SizeOfRawData),
                    "entropy": section.get_entropy()
                })

            # Get resources
            if hasattr(pe, "DIRECTORY_ENTRY_RESOURCE"):
                for resource_type in pe.DIRECTORY_ENTRY_RESOURCE.entries:
                    if resource_type.name:
                        analysis["resources"].append({
                            "type": resource_type.name.__str__(),
                            "id": hex(resource_type.struct.Id)
                        })

        except pefile.PEFormatError:
            # Not a PE file, try other analysis methods
            pass

        # Run strings command
        try:
            strings_output = subprocess.check_output(["strings", file_path]).decode()
            analysis["strings"] = strings_output.splitlines()
        except:
            pass

        # Run YARA rules
        try:
            rules = yara.compile(filepath="rules/index.yar")
            matches = rules.match(file_path)
            analysis["yara_matches"] = [match.rule for match in matches]
        except:
            pass

        return analysis

    async def start_dynamic_analysis(self, sample_id: str):
        """Start dynamic analysis of a sample"""
        try:
            # Get sample information
            sample = await self.db.samples.find_one({"_id": sample_id})
            if not sample:
                return

            # Update status
            await self.db.samples.update_one(
                {"_id": sample_id},
                {"$set": {"status": AnalysisStatus.IN_PROGRESS}}
            )

            # Get file path
            file_path = os.path.join(self.upload_dir, sample["filename"])

            # Create temporary directory for analysis
            with tempfile.TemporaryDirectory() as temp_dir:
                # Copy file to temp directory
                temp_file = os.path.join(temp_dir, sample["filename"])
                shutil.copy2(file_path, temp_file)

                # Perform dynamic analysis
                dynamic_analysis = await self._perform_dynamic_analysis(temp_file)
                dynamic_analysis["sample_id"] = sample_id

                # Save results
                result = await self.db.dynamic_analysis.insert_one(dynamic_analysis)
                dynamic_analysis_id = str(result.inserted_id)

                # Update sample with dynamic analysis ID
                await self.db.samples.update_one(
                    {"_id": sample_id},
                    {
                        "$set": {
                            "dynamic_analysis_id": dynamic_analysis_id,
                            "status": AnalysisStatus.COMPLETED
                        }
                    }
                )

        except Exception as e:
            # Update status to failed
            await self.db.samples.update_one(
                {"_id": sample_id},
                {"$set": {"status": AnalysisStatus.FAILED}}
            )
            raise e

    async def _perform_dynamic_analysis(self, file_path: str) -> Dict[str, Any]:
        """Perform dynamic analysis on a file"""
        analysis = {
            "execution_time": 0,
            "system_calls": [],
            "file_operations": [],
            "registry_operations": [],
            "network_connections": [],
            "process_tree": [],
            "dropped_files": [],
            "memory_dumps": [],
            "screenshots": [],
            "artifacts": [],
            "sandbox_info": {},
            "error_logs": []
        }

        # TODO: Implement actual dynamic analysis using Cuckoo Sandbox or similar
        # This is a placeholder implementation
        try:
            # Run in sandbox environment
            # For now, just simulate some results
            analysis["system_calls"] = [
                {"timestamp": "2024-01-01T00:00:00", "call": "CreateFile", "args": ["C:\\Windows\\System32\\kernel32.dll"]},
                {"timestamp": "2024-01-01T00:00:01", "call": "ReadFile", "args": ["C:\\Windows\\System32\\kernel32.dll"]}
            ]
            
            analysis["network_connections"] = [
                {"timestamp": "2024-01-01T00:00:02", "protocol": "TCP", "source": "192.168.1.1:1234", "destination": "8.8.8.8:53"}
            ]

        except Exception as e:
            analysis["error_logs"].append(str(e))

        return analysis 