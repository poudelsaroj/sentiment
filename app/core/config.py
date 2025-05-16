from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str = "development"
    model_name: str = "simple-textblob-sentiment"

    class Config:
        env_file = ".env"


settings = Settings()
