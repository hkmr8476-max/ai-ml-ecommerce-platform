from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ML AI Ecommerce API"
    api_prefix: str = "/api/v1"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"


settings = Settings()
