from customer import Customer

def main():
    print("🏦 Welcome to AS Banking")
    print("1. Log in")
    print("2. Open new account")
    choice = input("Choose (1 or 2): ")

    if choice == "1":
        try:
            phone_no = int(input("Enter your Registered Phone No: "))
            data = Customer.login(phone_no)
            if data:
                print(f"""🔍 Account Info:
Account No: {data['account_no']}
Name: {data['name']}
""")
                print(f"Enter any key to start banking")
        
        except ValueError:
            print("❌ Invalid phone number format.")
    elif choice == "2":
        phone_no = input("Enter your Mobile No to Register: ")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        Account_type = input("Enter the account type (Savings or Current): ")
        try:
            balance = float(input("Enter initial deposit amount: "))
            new_customer = Customer(phone_no, name, email, Account_type, balance)
            new_customer.create()
        except ValueError:
            print("❌ Invalid balance amount.")
    else:
        print("❌ Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
