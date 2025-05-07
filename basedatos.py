import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

connection = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_NAME')};"
    f"Trusted_Connection=yes;"
    f"TrustServerCertificate=yes;"
    f"Encrypt=no;"
)
