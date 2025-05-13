import pyodbc

class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=AYUSH_SHARMA\SQLEXPRESS;"  # Replace as needed
            "Database=BankingSystem;"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
