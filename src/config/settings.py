from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    database_url: str
    csv_file_path: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"