# test_connection.py
from db import Database

try:
    conn = Database()
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)


