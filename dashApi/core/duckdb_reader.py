import duckdb
from pathlib import Path
from typing import Literal
import pandas as pd

# Allow only these table names
ValidTable = Literal["pointers", "columns", "global_data", "pipes"]

# Path to DuckDB file
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "meta.duckdb"


def read_duckdb_table(table: ValidTable) -> list[dict]:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"DuckDB file not found at {DB_PATH}")

    con = duckdb.connect(str(DB_PATH), read_only=True)
    try:
        df = con.execute(f"SELECT * FROM {table}").fetchdf()
        return df.to_dict(
            orient="records"
        )  # convert to list of dicts (JSON serializable)
    finally:
        con.close()
