# It is Bank Account Code which will include balance check, deposition and withdrawal.
b = 500
while True:
    def Balance () :
        print("Your balance is ", b)
    def Withdraw () :
        global b
        w = int(input("Please enter the amount you want to withdraw "))
        b = b - w
        print("Your new balance is ", b)
    def Deposite () :
        global b
        d = int(input("Please enter the amount you want to deposite "))
        b = b + d
        print("Your new balance is ", b)
    
    print("Welcome to your account")
    print("What do you want to do?")
    print("1. Balance check\n2. Withdraw\n3. Deposition")
    ans = int(input("Please enter your answer "))
    while ans != 1 and ans != 2 and ans != 3 :
        print("The answer you have given is invalid\nPlease enter a number between 1,2,3")
        ans = int(input("Please enter your answer "))
    if ans == 1 :
        Balance()
    elif ans == 2:
        Withdraw()
    elif ans == 3:
        Deposite()
    print("Do you want to do anymore transaction?")
    print("1. Yes 2. No")
    rep = int(input("Please enter your answer "))
    while rep != 1 and rep != 2   :
        print("The answer you have given is invalid\nPlease enter a number between 1 and 2")
        rep = int(input("Please enter your answer "))
    if rep == 1 :
        continue
    elif rep == 2:
        break