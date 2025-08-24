from fastapi import APIRouter
from dashApi.api.ping import router as ping_router
from dashApi.api.plot import router as plot_router
from dashApi.api.duckdb import router as duckdb_router

api_router = APIRouter()
api_router.include_router(ping_router)
api_router.include_router(plot_router)
api_router.include_router(duckdb_router)
