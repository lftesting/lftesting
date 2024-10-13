# create a program that simulates ATM
# inicial account balance $2000
# ATM menu:
# 1 = Deposit
# 2 = Withdraw
# 3 = Available funds
# 4 = Exit

balance=2000
print("1. Deposit")
print("2. Withdraw")
print("3. Show account balance")
print("4. Exit")

selection=int(input("Enter desired option: "))

if selection ==1:
    deposit= float(input("Enter amount: "))
    balance+=deposit
    print(f"New balance: {balance}")
elif selection ==2:
    withdraw=float(input("Enter amount to withdraw: "))
    if withdraw > balance:
        print("Insufficient funds")
    else:
        balance-=withdraw
        print("Collect your withdrawal")
        print(f"New balance: {balance}")
elif selection==3:
    print(f"Available funds: {balance}")
elif selection==4:
    print("Thank you. Please collect your card")
else:
    print("Invalid option")
