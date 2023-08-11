def work_atm():
    balance = 1000
    pin = int(input("Enter your pin: "))
    while True:
        if pin == 2580:
            print("\nWelcome to the ATM")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            option = int(input("Enter your option: "))
            if option == 1:
                print(f"\nYour balance is: {balance}")
            elif option == 2:
                withdraw = int(input("Enter the amounf you want to withdraw: "))
                if withdraw > balance:
                    print("Insufficient funds!")
                else:
                    balance -= withdraw
                    print(f"Your balance is: {balance}")
            elif option == 3:
                deposit = int(input("Enter the amount you want to deposit: "))
                balance += deposit
                print(f"Your balance is: {balance}")
            elif option == 4:
                print("Thank you for using my ATM")
                break
            else:
                print("Invalid option!")
        else:
            print("Invalid pin!\n")
work_atm()