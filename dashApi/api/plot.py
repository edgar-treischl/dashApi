from fastapi import APIRouter, HTTPException, Response
from dashApi.core.plotter import generate_gapminder_plot_bytes
from fastapi import Query


router = APIRouter()


@router.get("/plot", tags=["Images"])
async def plot(
    year: int = Query(..., ge=1952, le=2007, description="Year between 1952 and 2007")
):
    try:
        img_bytes = generate_gapminder_plot_bytes(year)
        return Response(content=img_bytes, media_type="image/png")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
