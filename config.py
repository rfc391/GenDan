import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    EMAIL = os.getenv("GENETIC_EMAIL", "default@example.com")
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    HOST = os.getenv("FLASK_HOST", "0.0.0.0")
    PORT = int(os.getenv("FLASK_PORT", 8080))
