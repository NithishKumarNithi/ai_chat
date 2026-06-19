from typing import Annotated

import os
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

import jwt

from server.utils.dependencies import get_user_info, verify_password, get_current_user
from server.model.schema import LoginUser

router = APIRouter()

SECRET =  os.getenv("SECRET")
ALGORITM = os.getenv("ALGORITM")

@router.get("/")
async def home():
    return JSONResponse(content={"message": "welcome home"},status_code=status.HTTP_200_OK)

@router.post("/login")
async def login(formdata: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = get_user_info(formdata.username)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="username not found")
    elif not verify_password(formdata.password, user):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect credentials")
    
    payload = {"id": user["user_id"], "user": user["name"]}
    jwt_en = jwt.encode(payload, SECRET, ALGORITM)
 
    return JSONResponse(content={"message": "login successful", "token": jwt_en, "type": "Bearer"}, status_code=status.HTTP_200_OK)

@router.get("/verify")
async def verify_token(user: Annotated[LoginUser, Depends(get_current_user)]):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": jsonable_encoder(LoginUser(**user))})
 