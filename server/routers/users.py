from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from server.data.users import users
from server.data.settings import settings
from server.model.schema import LoginUser

from server.utils.dependencies import get_user_settings, get_current_user

router = APIRouter()

@router.get("/users")
async def get_users():
    return JSONResponse(content=users, status_code=status.HTTP_200_OK)

@router.get("/users/{user_id}")
async def get_users(user_id: int, user: Annotated[LoginUser, Depends(get_current_user)]):
    if user_id != user["user_id"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid User" )
    return JSONResponse(content=jsonable_encoder(LoginUser(**user)), status_code=status.HTTP_200_OK)

@router.get("/users/{user_id}/settings")
async def get_user_config(user_id: int):
    user_config = get_user_settings(user_id)
    if not user_config["config"]:
        default_settings = { "setting_exit": user_config["setting_exit"], "default_settings": settings}
        return JSONResponse(content=default_settings, status_code=status.HTTP_200_OK)
    return JSONResponse(content=user_config["config"], status_code=status.HTTP_200_OK)