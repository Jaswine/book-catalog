from os import getenv
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = getenv('APP_NAME', 'Book catalog')
    app_version: str = getenv('APP_VERSION', '1.0.0')