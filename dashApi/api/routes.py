from fastapi import APIRouter, Query
from dashApi.core.processor import get_hello_message
from dashApi.models.schema import HelloResponse

router = APIRouter()

@router.get("/hello", response_model=HelloResponse)
def hello(name: str = Query(..., min_length=1, description="Name of the person to greet")):
    return get_hello_message(name)
