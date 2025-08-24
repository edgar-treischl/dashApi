from fastapi import APIRouter, HTTPException, Query
from dashApi.core.duckdb_reader import read_duckdb_table, ValidTable
from dashApi.core.serialization import serialize_dataframe
import pandas as pd
import traceback

router = APIRouter()


@router.get("/duckdb-table", tags=["Table"])
async def get_duckdb_table(
    table: ValidTable = Query(..., description="DuckDB meta table"),
    format: str = Query("json", description="Output format: 'json' or 'csv'"),
):
    try:
        data = read_duckdb_table(table)
        # Convert list to DataFrame if needed
        if isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            df = data

        return serialize_dataframe(df, format=format, filename=table)

    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        print("Error in /duckdb-table endpoint:\n", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
