#if the customer doesnot have the account in the bank

from db import Database
import random

class Customer:
    def __init__(self,phone_no,name=None,email=None,Account_type=None,balance=0.00):
        self.phone_no=phone_no
        self.name=name
        self.email=email
        self.Account_type=Account_type
        self.balance=balance
        self.account_no=self.rand_account()
    
    #now creating the methord
    # now the stask s to generate the randaom account no
    def rand_account(self):
        db=Database()

        while True:
            account_no=random.randint(100000,999999)
            exists = db.fetchone("SELECT 1 FROM Customers WHERE account_no = ?", (account_no,))
            if not exists:
                db.close()
                return account_no


        

   # @staticmethod
    def create(self):
        db=Database()
         # Check if the phone number already exists
        exists = db.fetchone("SELECT 1 FROM Customers WHERE phone_no = ?", (self.phone_no,))
        if exists:
            print(f"❌ A customer with phone number {self.phone_no} already has an account.")
            db.close()
            return
        db.execute(
            "INSERT INTO Customers (account_no,phone_no,name, email, Account_type,balance) VALUES (?, ?, ?,?,?,?)",
            (self.account_no,self.phone_no,self.name,self.email,self.Account_type,self.balance)

        )
        print(f"The account is created : {self.name} with Account No {self.account_no} and opening balance ₹ {self.balance}")
        db.close()
    @staticmethod
    def login(phone_no):
        db = Database()
        customer = db.fetchone("SELECT account_no, phone_no, name, email, Account_type, balance FROM Customers WHERE phone_no = ?", (phone_no,))
        db.close()
        if customer:
            print(f"✅ Welcome back, {customer.name if hasattr(customer, 'name') else customer[1]}!")
            return {
                
                "account_no":customer[0],
                "phone_no":customer[1],

                "name": customer[2],
                "email": customer[3],
                "Account_type":customer[4],
                "balance": customer[5]
            }
        else:
            print("❌ Customer not found.")
            return None

        