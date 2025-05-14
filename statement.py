from db import Database
from customer import Customer
class statement:
    def __init__(self,pin_no,phone_no,balance):
        self.phone_no=phone_no
        self.pin_no=pin_no
        self.balance=balance
    
    def statement(self):
        db=Database()
        pin=int(input("Enter 4-Digit Pin\n"))
        customer=db.fetchone("SELECT pin_no from Customers where phone_no=?",(self.phone_no))
        if not customer:
            print(f"Invalid Transaction!!!")
            return
        elif str(customer[pin_no])!=pin:
            print(f"Invalid pin! Give the correct pin ")
            return
        

        # Fetch last 5 transactions
        transactions = db.fetchall(
            """
            SELECT date_time, account_no, description, transaction_type, amount
            FROM transaction_table
            WHERE phone_no=?
            ORDER BY date_time DESC
            LIMIT 5
            """,
            (self.phone_no,)
        )

        if not transactions:
            print("No transactions found.")
            return

        print("\n===== Last 5 Transactions =====")
        for txn in transactions:
            print(f"""
Date & Time       : {txn['date_time']}
Account No        : {txn['account_no']}
Description       : {txn['description']}
Transaction Type  : {txn['transaction_type']}
Amount            : ₹{txn['amount']}

-----------------------------""")
            print(f"Remaining Balance:₹{self.balance}")
        db.close()
