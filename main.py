class AtM:
    def __init__(self, card_number, pin_number, balance):
        self.card_number = int(card_number)
        self.pin_number = int(pin_number)
        self.balance = balance

    #function to wtihdraw cash
    def cashWithdrawal(self):
        withdraw_inp = int(input("Enter how much money you would like to withdraw: "))

        if withdraw_inp > self.balance or withdraw_inp < 0:
            print("You cannot withdraw that much")
            self.cashWithdrawal()
        else:
            print("Withdrawing cash.....")
            self.balance -= withdraw_inp
            print("Complete!")
            print("You now have " + str(self.balance) + " in your bank account")
            print("-----------------------------------------------------------")
        
    #function to check the balance
    def balancecheck(self):
        print("Your balance is " + str(self.balance))

    #function to deposit cash
    def cashdeposit(self):
        deposit_inp = int(input("Enter a sum of money from 500 to 2000 rupees: "))

        if deposit_inp >= 500 and deposit_inp <= 2000:
            self.balance += deposit_inp
            print("Your new balance is " + str(self.balance))
        else:
            print("Please enter a valid amount")
            self.cashdeposit()


atm = AtM(1234, 1234, 4500)
atm.balancecheck()

print("This is a text based user interface to use an atm")
print("COMMANDS: ")
print("1. cashwithdrawal: cw")
print("2. balancecheck: bc")
print("3. cashdeposit: cd")


while True:
    global inp

    inp = input("")

    if inp == "cw":
        atm.cashWithdrawal()
    elif inp == "bc":
        atm.balancecheck()
    elif inp == "cd":
        atm.cashdeposit()