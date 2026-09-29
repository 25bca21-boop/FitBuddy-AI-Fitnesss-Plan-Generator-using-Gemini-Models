import os
from functools import lru_cache

from dotenv import load_dotenv


load_dotenv()


class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "FitBuddy AI")
        self.debug = os.getenv("DEBUG", "false").strip().lower() in {"1", "true", "yes", "on"}
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "").strip()
        self.gemini_model = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.8-flash"
        )


@lru_cache
def get_settings():
    return Settings()