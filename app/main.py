from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.services.ai_service import generate_response


app = FastAPI(title="SupportGuard AI")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)


class ChatResponse(BaseModel):
    response: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = generate_response(request.message)

    return ChatResponse(response=response)
    