from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio
from .src.master_agent import MasterAgent
import uvicorn

# Initialize FastAPI app
app = FastAPI()
master_agent = MasterAgent()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    mode: str = "sync"  # sync, async, workflow

class WorkflowRequest(BaseModel):
    user_id: str
    tasks: List[str]

@app.post("/chat/")
async def chat(request: ChatRequest):
    """Handle chat messages and invoke MasterAgent."""
    try:
        response = await master_agent.process_request(request.user_id, request.message, request.mode)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @app.post("/workflow/")
# async def workflow(request: WorkflowRequest):
#     """Execute a workflow with multiple tasks."""
#     try:
#         response = await master_agent.execute_workflow(request.user_id, request.tasks)
#         return {"results": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
