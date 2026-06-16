from fastapi import FastAPI

 
from aichat.routers import home, settings, users

from dotenv import load_dotenv
 
app = FastAPI()

load_dotenv()

app.include_router(home.router, prefix="/home",)
app.include_router(settings.router)
app.include_router(users.router)
