from fastapi import FastAPI
from dashApi.api import api_router
from dashApi.config import settings

app = FastAPI(title="DS Dash API")

app.include_router(api_router)
