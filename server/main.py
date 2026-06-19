from typing import Annotated

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
 
from server.routers import home, settings, users

from dotenv import load_dotenv
 
app = FastAPI()

load_dotenv()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
app.include_router(home.router, prefix="/home",)
app.include_router(settings.router)
app.include_router(users.router)
