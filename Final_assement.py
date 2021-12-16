print("Welcome to Bank Of Motown")


account_balance = 500
user_tries = 3

user_pin = 1234
print("1-Withdraw | 2-Check Balance | 3-Deposit ")
# print("4-Exit")
 
while user_tries != 0:
    pin = int(input("Enter Your 4 Digit Pin: "))
    if pin != user_pin:
        user_tries -= 1
        print("Wrong pin, You Have", user_tries, "Tries Left")
    else:
        user_input = int(input("Please Choose Transactions: "))
        if user_input == 1:
            withdraw = int(input("Enter The Amount You Would Like to Withdraw: "))
            print("Please take your amount:","Your New Balance Is", "${:,.2f}".format(account_balance - withdraw))
        if user_input== 2:
            print("Your Available Amount:","${:,.2f}".format(account_balance))
        if user_input == 3:
            user_deposit =int(input("Enter The Amount You Would Like to Desopit: "))
            print("Your new balance is", "${:,.2f}".format(account_balance + user_deposit))
    user_exit = input("Would You Like To Conintue? Y/N: ")
    if user_exit == "N":
        print("Thank You For Using Bank OF Motown")
        break
    else: 
        continue 
