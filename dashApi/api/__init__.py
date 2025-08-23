from fastapi import APIRouter
from dashApi.api.ping import router as ping_router
#from .ping import router as ping_router
from dashApi.api.plot import router as plot_router

api_router = APIRouter()
api_router.include_router(ping_router)
api_router.include_router(plot_router)
