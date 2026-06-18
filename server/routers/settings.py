from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from server.data.settings import settings

from server.model.schema import LLMProviders, Settings

router = APIRouter()

@router.get("/settings")
async def get_settings():
    return JSONResponse(content= settings, status_code=status.HTTP_200_OK)

@router.put("/settings/update")
async def update_settings(settings: Settings):
    if not settings.selected:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="selected field is required")
    elif settings.selected not in LLMProviders:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="invalid providers")
    return JSONResponse(content=jsonable_encoder(settings), status_code=status.HTTP_202_ACCEPTED)