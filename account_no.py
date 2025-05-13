from db import Database
import random
def rand_account(self):
        db=Database()

        while True:
            account_no=random.randint(100000,999999)
            exists = db.fetchone("SELECT 1 FROM Customers WHERE account_number = ?", (account_no,))
            if not exists:
                db.close()
                return account_no
