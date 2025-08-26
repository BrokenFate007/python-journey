
#This is ongoing code for ATM simulation. :)

bank_balance = 0

while True:
    print("a. Deposit Money \nb. Withdraw Money\nc. Check Balance\nd. Transfer Money\ne. Exit")

    choice = str(input("Input your choice (a,b,...):"))


    while choice == str("a"):
        deposited_money = float(input("How much money you want to deposit:"))
        bank_balance += deposited_money
        print("Deposit successful. Current bank balance:",bank_balance)
        print("Anymore work?")
        deposit_choice=str(input("Do you need anymore transaction?(y or n)"))
        if deposit_choice in ["y", "yes"]:
            choice = str(input("Input your choice(a,b,...):"))
        else:
            print("Thank you for your visit")
            break

    while choice == str("b"):
        debited_money = float(input("How much money you want to withdraw:"))
        if debited_money<=bank_balance:
            bank_balance-=debited_money
            print("Bank balance:",bank_balance)
        else:
            print("You have insufficient amount of money.")
        break
        # choice = str(input("Input your choce(a,b,..):"))
   
    while choice == str("e"):
        break