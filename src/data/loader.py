import duckdb
import pandas as pd
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
ROOT    = Path(__file__).resolve().parents[2]
RAW     = ROOT / "data" / "raw"
DB_PATH = ROOT / "data" / "processed" / "instacart.duckdb"


def get_connection() -> duckdb.DuckDBPyConnection:
    """Return a DuckDB connection, creating tables if they don't exist."""
    con = duckdb.connect(str(DB_PATH))
    _create_tables(con)
    return con


def _create_tables(con: duckdb.DuckDBPyConnection) -> None:
    tables = {
        "orders":                  "orders.csv",
        "order_products_prior":    "order_products__prior.csv",
        "order_products_train":    "order_products__train.csv",
        "products":                "products.csv",
        "aisles":                  "aisles.csv",
        "departments":             "departments.csv",
    }

    existing = {row[0] for row in con.execute("SHOW TABLES").fetchall()}

    for table_name, csv_file in tables.items():
        if table_name not in existing:
            csv_path = RAW / csv_file
            print(f"Loading {table_name}...")
            con.execute(f"""
                CREATE TABLE {table_name} AS
                SELECT * FROM read_csv_auto('{csv_path}')
            """)
            count = con.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
            print(f"  done: {count:,} rows")
        else:
            print(f"  {table_name} already loaded")


def query(sql: str, con=None) -> pd.DataFrame:
    """Run SQL and return a pandas DataFrame."""
    close_after = con is None
    if con is None:
        con = get_connection()
    result = con.execute(sql).df()
    if close_after:
        con.close()
    return result