from typing import Annotated

import os
from datetime import datetime

from fastapi import status, Depends, HTTPException 
from fastapi.security import OAuth2PasswordBearer

import jwt
from pwdlib import PasswordHash

from ..data.settings import settings, user_settings
from ..data.users import users

from ..model.schema import Users

SECRET =  os.getenv("SECRET")
ALGORITM = os.getenv("ALGORITM")
TOKEN_EXPIRES = os.getenv("TOKEN_EXPIRES")

print(SECRET)

oauth_schema = OAuth2PasswordBearer(tokenUrl="login")

password_hash = PasswordHash.recommended()

def is_user_exit(id: int):
    is_exit = False
    
    for user in users:
        if user["user_id"] == id:
            is_exit = True
            break
    
    return is_exit

def get_user_settings(user_id: int):
    is_setting_exit = False
    config = None

    for setting in user_settings:
        if setting["user_id"] == user_id:
            is_setting_exit = True
            config = setting
            break
    return {"setting_exit": is_setting_exit, "config": config}

def get_user_info(username: str):
    for user in users:
        if user["name"] == username.lower():
            return user
    return None
    
def verify_password(password: str, user: Users):
    return password_hash.verify(password, user["hash_pass"])

def get_hash_password(password: str):
    return password_hash.hash(password)

def get_current_user(token: Annotated[str, Depends(oauth_schema)]):

    try: 
        payload = jwt.decode(token, SECRET, ALGORITM)
        
        user = payload.get("user") 
        user_details = get_user_info(user)
        print("de payload : ", datetime.fromtimestamp(payload.get("exp")))
        if not user_details:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"})
    except  jwt.ExpiredSignatureError :
            raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="The access token provided has expired.",
                            headers={"WWW-Authenticate": "Bearer"})
    
    return user_details



 




