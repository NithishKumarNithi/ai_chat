from fastapi import FastAPI

from .routers.home import home
from .routers.settings import settings
from .routers.users import users

from dotenv import load_dotenv
 
app = FastAPI()

load_dotenv()

app.include_router(home.router)
app.include_router(settings.router)
app.include_router(users.router)
