import random
class ATM():
    def __init__(self, name, id, balance=0):
        self.name = name
        self.id = id
        self.balance = balance

    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name}")
        print(f"Id: {self.id}")
        print(f"Available balance: Nu.{self.balance}\n")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Nu.", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Nu.", self.balance)
            print()

    def check_balance(self):
        print("Available balance: Nu.", self.balance)
        print()

    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)

        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Nu.):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Nu.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name}                  
              Id: {self.id}                
              Available balance: Nu.{self.balance}                    

              Thanks for choosing us as your bank                  
          ******************************************
          """)


print("******* WELCOME TO THE BANK *******")
print("\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
id = input("Enter your id : ")
print("Congratulations! Account created successfully......\n")

atm = ATM(name, id)
while True:
    trans = input("Do you want to do any transaction?(yes/no):")
    if trans == "yes":
        atm.transaction()
    elif trans == "no":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command!  Enter 'yes' or 'no' ")