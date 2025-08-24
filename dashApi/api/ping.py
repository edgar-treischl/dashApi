from fastapi import APIRouter
from fastapi.responses import JSONResponse

from dashApi.core.processor import get_ping_response
from dashApi.models.schema import PingResponse


router = APIRouter()


@router.get("/ping", response_model=PingResponse, tags=["Health"])
async def ping():
    return get_ping_response()
