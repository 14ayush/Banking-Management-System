from db import Database
import random
from customer import Customer

class banking:
    print(f"Hello Sir How May I help you ")
    def __init__(self,phone_no):
        self.phone_no=phone_no
    

    def applyatm(self):
        db=Database()
        exist=db.fetchone("SELECT card_no FROM Customers where phone_no=?",(self.phone_no,))
        if exist and exist['card_no']:
            print(f"You already have a card with card no:",exist['card_no'])
            return
        card_no=random.randint(100000000,999999999)
        '''db.execute(
            "UPDATE Customers SET card_no=? WHERE phone_no=?",
            (card_no, self.phone_no)
        )
        db.close()'''
        print(f"Your ATM card is Generated, Here is your Card no",card_no)


    def accountinfo(self):
        db=Database()
        exists=db.fetchone("SELECT * FROM Customers where phone_no=?",(self.phone_no,))
        db.close()
        if exists:
            print(f"""Account Information:
            Name: {exists['name']}
            Account No: {exists['account_no']}
            Phone No: {exists['phone_no']}
            Card No: {exists['card_no'] or 'Not Issued'}
            Balance: {exists['balance'] if 'balance' in exists else 'N/A'}""")
        else:
            print("Customer not found.")

    def changepin(self):
        #print(f"Enter the current pin\n")
        db=Database()
        exists=db.fetchone("SELECT card_no,pin_no from Customers WHERE phone_no=?",(self.phone_no,))
        if not exists or not exists['card_no'] :
            print(f"No ATM card Found..Please apply for ATM Card First")
            return
        
        
        curr_pin=int(input("Enter the current Pin:\n"))
        if not exists[pin_no]:
            print(f"No pin found  set the pin first")
            return
        elif str(exists[pin_no])!=curr_pin:
            print(f"Invalid pin! Give the correct pin ")
            return
        
        new_pin=int(input("Enter the 4-Digit new pin"))
        if not new_pin.isdigit() or len(new_pin)!=4:
            print(f"Pin must be digit and have exactly 4 no's")
            return
        db.execute("UPDATE Customers SET pin_no=? where phone_no=?",(int(new_pin),self.phone_no))
        db.close()
        print(f"New pin setup Successfully!! Thank You Visit Again ")

        

