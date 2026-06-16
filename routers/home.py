from typing import Annotated

import os
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

import jwt

from aichat.utils.dependencies import get_user_info, verify_password

router = APIRouter()

SECRET =  os.getenv("SECRET")
ALGORITM = os.getenv("ALGORITM")

@router.get("/")
async def home():
    return JSONResponse(content={"message": "welcome home"},status_code=status.HTTP_200_OK)

@router.get("/login")
async def login(formdata: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = get_user_info(formdata.username)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="username not found")
    elif not verify_password(formdata.password, user):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect credentials")
    
    expire_time = datetime.now()
    print("exp time : ", expire_time)
    payload = {"id": user["user_id"], "user": user["name"], "exp": expire_time}
    print(payload)
    jwt_en = jwt.encode(payload, SECRET, ALGORITM)

    return JSONResponse(content={"message": "login successful", "token": jwt_en, "type": "Bearer"}, status_code=status.HTTP_200_OK)