# dashApi/core/serialization.py

import pandas as pd
import io
from fastapi.responses import JSONResponse, StreamingResponse, Response


def serialize_dataframe(
    df: pd.DataFrame, format: str, filename: str = "data"
) -> Response:
    """
    Serialize a DataFrame into a FastAPI-compatible response.

    Args:
        df (pd.DataFrame): The DataFrame to serialize.
        format (str): One of "json" or "csv".
        filename (str): Used in Content-Disposition header if CSV.

    Returns:
        fastapi.Response: JSONResponse or StreamingResponse.
    """
    format = format.lower()

    if format == "json":
        return JSONResponse(content=df.to_dict(orient="records"))

    elif format == "csv":
        buffer = io.StringIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        return StreamingResponse(
            buffer,
            media_type="text/csv",
            headers={"Content-Disposition": f'attachment; filename="{filename}.csv"'},
        )

    else:
        raise ValueError(f"Unsupported format: '{format}'")
