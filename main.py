from enum import Enum

from fastapi import FastAPI, status, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel

from settings import settings
from users import users


app = FastAPI()

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


def is_user_exit(id: int):
    isExit = False
    
    for user in users:
        if user["user_id"] == id:
            isExit = True
    
    return isExit
            
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="data is unprocessable")

@app.get("/")
async def home():
    return JSONResponse(content={"message": "welcome home"},status_code=status.HTTP_200_OK)

@app.get("/settings")
async def get_settings():
    return JSONResponse(content= settings, status_code=status.HTTP_200_OK)

@app.put("/settings/update")
async def update_settings(settings: Settings):
    if not settings.selected:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="selected field is required")
    elif settings.selected not in LLMProviders:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="invalid providers")
    return JSONResponse(content=jsonable_encoder(settings), status_code=status.HTTP_202_ACCEPTED)

@app.get("/users")
async def get_users():
    return JSONResponse(content=users, status_code=status.HTTP_200_OK)

@app.get("/users/{user_id}")
async def get_users(user_id: int):
    if not is_user_exit(user_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    return JSONResponse(content=users[user_id - 1], status_code=status.HTTP_200_OK)