from enum import Enum

from pydantic import BaseModel


class LLMProviders(str, Enum):
    openai = "openai"
    gemini = "gemini"
    anthropic = "anthropic"

class LLMModels(BaseModel):
    provider: str
    models: list[str]

class Settings(BaseModel):
    providers: list[str]
    selected: str
    models: list[LLMModels]

class Users(BaseModel):
    user_id: int
    name: str
    email: str
    hash_pass: str

class LoginUser(BaseModel):
    user_id: int
    name: str
    email: str