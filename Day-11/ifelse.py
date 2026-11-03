#ifelse - login successful or not
data = ('admin@gmail.com', 'admin@123')

gmail = input("Enter the mail: ")
password = input("Enter the passsword: ")
if (gmail, password) == data:
    print("Login successful")
else:
    print("Invalid login")


#ifelse - booking seats
seats = {
    's1': 'Booked',
    's2': 'Available',
    's3': 'Available',
    's4': 'Available',
    's5': 'Booked',
    's6': 'Available'
}

seatno = input("Enter the seat no(sn): ")
if seatno in seats and seats[seatno] == 'Available':
    seats[seatno] = 'Booked'
    print(f'{seatno} is booked successfully')
    print(seats)
else:
    print(f'{seatno} is already booked')  


#ifelse - product is available or not
products = {
    'laptop': {'price': 40000, 'stock': 10},
    'mouse': {'price': 400, 'stock': 0},
    'keyboard': {'price': 2000, 'stock': 3},
    'tab': {'price': 20000, 'stock': 5},
    'phone': {'price': 60000, 'stock': 8}
}
search = input("Enter the product name: ")
if search in products and products[search]['stock'] > 0:
    print(f"you can buy {search} at this price: {products[search]['price']}")
else:
    print(f"{search} is not avaliable")