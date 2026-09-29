from fastapi import APIRouter
from pydantic import BaseModel

from .ai.gemini import ask_gemini


router = APIRouter(
    prefix="/api"
)


class ChatRequest(BaseModel):
    message: str


@router.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "FitBuddy AI backend is running"
    }


@router.post("/chat")
async def chat(request: ChatRequest):

    message = request.message.strip()

    if not message:
        return {
            "success": False,
            "message": "Please enter a message."
        }

    if len(message) > 4000:
        return {
            "success": False,
            "message": "Message is too long. Please keep it under 4000 characters."
        }

    try:

        response = ask_gemini(message)

        return {
            "success": True,
            "response": response
        }

    except Exception as error:

        print("Gemini error:", error)

        return {
            "success": False,
            "message": (
                "Gemini AI is not available right now. "
                "Please check your API key and try again."
            )
        }