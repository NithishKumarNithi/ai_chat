from typing import Annotated

import os
from datetime import datetime

from fastapi import status, Depends, HTTPException 

import jwt

from .auth import oauth_schema, password_hash

from server.data.settings import user_settings
from server.data.users import users

from server.model.schema import Users

SECRET =  os.getenv("SECRET")
ALGORITM = os.getenv("ALGORITM")
TOKEN_EXPIRES = os.getenv("TOKEN_EXPIRES")

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

def validate_token(token: Annotated[str, Depends(oauth_schema)]):

    try: 
        payload = jwt.decode(token, SECRET, ALGORITM)
        
        user = payload.get("user") 
        user_details = get_user_info(user)

        if not user_details:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Invalid User",
                headers={"WWW-Authenticate": "Bearer"})
    except jwt.ExpiredSignatureError :
            raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="The access token provided has expired.",
                            headers={"WWW-Authenticate": "Bearer"})
    except:
        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Could not validate credentials",
                            headers={"WWW-Authenticate": "Bearer"})


def get_current_user(token: Annotated[str, Depends(oauth_schema)]):

    try: 
        payload = jwt.decode(token, SECRET, ALGORITM)
        
        user = payload.get("user") 
        user_details = get_user_info(user)

        if not user_details:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Invalid User",
                headers={"WWW-Authenticate": "Bearer"})
    except jwt.ExpiredSignatureError :
            raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="The access token provided has expired.",
                            headers={"WWW-Authenticate": "Bearer"})
    
    return user_details



 




