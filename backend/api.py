from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio
from src.master_agent import MasterAgent
from src.llmservice import LLMService
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your Next.js frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

master_agent = MasterAgent()
llm_service = LLMService()
class ChatRequest(BaseModel):
    #user_id: str
    message: str
    #mode: str = "sync"  # sync, async, workflow
class AnswerRequest(BaseModel):
    input: str
# class WorkflowRequest(BaseModel):
#     user_id: str
#     tasks: List[str]

@app.post("/chat/")
async def chat(request: ChatRequest):
    """Handle chat messages and invoke MasterAgent."""
    try:
        response = await master_agent.process_input(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/answer/")
async def answer(request: AnswerRequest):
    """Handle user input and generate a response using the LLM."""
    try:
        # Call the LLM service to generate a response
        response = await llm_service.generate_response(request.input)
        return {"result": response}
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
