import pyodbc
import pandas as pd

def read_query(filepath):
    with open(filepath, "r") as f:
        return f.read()
    
def run_query(query):
    conn_str = (
        "Driver={SQL Server};"
        "Server=PRTPRDCSQL10;"
        "Database=SalesforceCache;"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_str)
    result = pd.read_sql(query, conn)
    conn.close()
    
    return result