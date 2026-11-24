data = {
    123456: {"pin": 1234, "balance": 5000, "transactions": []},
    123457: {"pin": 1234, "balance": 6000, "transactions": []},
    123458: {"pin": 1234, "balance": 7000, "transactions": []},
    123458: {"pin": 1234, "balance": 8000, "transactions": []}
}

#login 
def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]["pin"] == pin:
        print("Login Succcessful")
        return True
    else:
        print("Invalid login")
        return False

#display the menu card
def menu():
    print()
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[T]ransactions")
    print("[C]hange pin")
    print("[E]xit")

#check balance
def checkbalance():
    print(f"Current Balance is {data[acc_num]['balance']}")

#deposit amount
def deposit():
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance'] += amount
    data[acc_num]['transactions'].append(f'Deposit: Rs. {amount}/-')
    print(f"{amount} is deposited successfully")

#withdraw amount
def withdraw():
    amount = int(input("Enter the amount: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance'] -= amount
        data[acc_num]['transactions'].append(f'Withdraw: Rs. {amount}/-')
        print(f"{amount} is withdraw successfully")
    else:
        print("Insufficient Balance")

#transctions
def transactions():
    if data[acc_num]['transactions']:
        print('----------Transactional History----------')
        for i in data[acc_num]['transactions']:
            print(i)
    else:
        print("No Transactions yet")

#change pin
def changepin():
    newpin = input("Enter the new pin: ")
    data[acc_num]['pin'] == newpin
    print("Pin changes successfully")