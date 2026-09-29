from google import genai

from app.config import get_settings


settings = get_settings()


def ask_gemini(prompt: str) -> str:
    if not settings.gemini_api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Add it to the .env file."
        )

    client = genai.Client(api_key=settings.gemini_api_key)
    chat = client.chats.create(model=settings.gemini_model)
    response = chat.send_message(prompt)

    text = getattr(response, "text", None)
    if not text:
        return "Gemini returned an empty response."

    return text.strip()