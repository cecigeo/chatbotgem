from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from gemini import query_gemini

app = FastAPI()

class ChatInput(BaseModel):
    message: str
    user_id: str = "default"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chat/welcome")
async def welcome():
    return {"response": "Hola 👋 Soy tu asistente contable. ¿En qué puedo ayudarte?"}

@app.post("/chat")
async def chat_endpoint(input: ChatInput):
    message = input.message

    response = query_gemini(message)


    return {"response": response}