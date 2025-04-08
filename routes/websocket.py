from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from fastapi.responses import HTMLResponse
from typing import List, Dict
import json
import asyncio
from ..utils.security import get_current_user
from ..main import app

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        if client_id not in self.active_connections:
            self.active_connections[client_id] = []
        self.active_connections[client_id].append(websocket)

    def disconnect(self, websocket: WebSocket, client_id: str):
        if client_id in self.active_connections:
            self.active_connections[client_id].remove(websocket)
            if not self.active_connections[client_id]:
                del self.active_connections[client_id]

    async def broadcast(self, message: str, client_id: str):
        if client_id in self.active_connections:
            for connection in self.active_connections[client_id]:
                await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/ws/logs/{file_id}")
async def websocket_logs(websocket: WebSocket, file_id: str):
    """WebSocket endpoint for real-time analysis logs"""
    await manager.connect(websocket, f"logs_{file_id}")
    try:
        while True:
            # Simulate log streaming
            # In a real implementation, this would connect to the analysis process
            await asyncio.sleep(1)
            log_message = {
                "timestamp": "2024-01-01T00:00:00",
                "level": "info",
                "message": f"Processing file {file_id}..."
            }
            await manager.broadcast(json.dumps(log_message), f"logs_{file_id}")
    except WebSocketDisconnect:
        manager.disconnect(websocket, f"logs_{file_id}")

@router.websocket("/ws/alerts")
async def websocket_alerts(websocket: WebSocket):
    """WebSocket endpoint for real-time alerts"""
    await manager.connect(websocket, "alerts")
    try:
        while True:
            # Simulate alert streaming
            # In a real implementation, this would monitor for new alerts
            await asyncio.sleep(5)
            alert_message = {
                "timestamp": "2024-01-01T00:00:00",
                "type": "detection",
                "severity": "high",
                "message": "New malware sample detected"
            }
            await manager.broadcast(json.dumps(alert_message), "alerts")
    except WebSocketDisconnect:
        manager.disconnect(websocket, "alerts")

async def send_analysis_update(file_id: str, message: str):
    """Send analysis update to connected clients"""
    await manager.broadcast(json.dumps({
        "timestamp": "2024-01-01T00:00:00",
        "type": "analysis_update",
        "file_id": file_id,
        "message": message
    }), f"logs_{file_id}")

async def send_alert(alert_type: str, severity: str, message: str):
    """Send alert to all connected clients"""
    await manager.broadcast(json.dumps({
        "timestamp": "2024-01-01T00:00:00",
        "type": alert_type,
        "severity": severity,
        "message": message
    }), "alerts") 