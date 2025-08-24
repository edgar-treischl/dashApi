# test_duckdb.py

from dashApi.core.duckdb_reader import read_duckdb_table

if __name__ == "__main__":
    table_name = "pointers"  # Try any of: pointers, columns, global_data, pipes
    result = read_duckdb_table(table_name)
