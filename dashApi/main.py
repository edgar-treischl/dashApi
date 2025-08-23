from fastapi import FastAPI
from dashApi.api.routes import router
from dashApi.config import settings

app = FastAPI(title="DS Dash API")

app.include_router(router)

