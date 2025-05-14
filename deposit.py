from db import Database
from datetime import datetime

class deposit:
    def __init__(self,phone_no):
        self.phone_no=phone_no
    
    def amount_deposit(self):
        print("💰 Daily cash deposit limit is ₹20,000")
        try:
            amount=int(input("Enter the amount:\n"))
        except ValueError:
            print(f"Invalid Amount")
        
        if amount>20000:
            print(f"Daily Deposit limit Exceeds")
            return
        elif amount<100:
            print(f"Error!! Amount must be greater than ₹100")
        
        db=Database()
        customer=db.fetchone("SELECT account_no,balance from Customers where phone_no=?",(self.phone_no))
        if not customer:
            print(f"Invalid Customer")
        
        new_balance=customer['balance']+amount
        db.execute("UPDATE Customers SET balance=? where phone_no=?",(new_balance,self.phone_no))

        #record the data into transaction table 

        now=datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        description=f"Cash {customer['name']}"
        db.execute(""" INSERT INTO transaction_table (
             date_time, account_no, description, transaction_type, amount, remaining_balance
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            now,
            customer['account_no'],
            description,
            "credit",
            amount,
            new_balance
        ))

        db.close()
        print(f"✅ ₹{amount} deposited successfully.")
        print(f"💼 Updated Account Balance: ₹{new_balance}")




        