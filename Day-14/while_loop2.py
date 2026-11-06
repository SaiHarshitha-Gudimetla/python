#l = [12,9,3,4,5,10,2,4,5,2,4,5] - addition bw the first and last number

l = [12,9,3,4,5,10,2,4,5,2,4,5]
i = 0
j = len(l)-1
while i <= j:
    if i == j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i += 1
    j -= 1 


#take input from user until they stop

bill = 0
while True:
    product = input("Enter the products(STOP): ")
    if product == 'STOP':
        print("Total Bill: ", bill)
        break
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    bill += price*quantity

#dict - keys-product, values-prices
#display the menu card
#ask the user to pick the product name and quantity
#bill contain the products, quantity, price, total bill, thank you

products = {
    'bread': 50, 'milk': 30, 'sugar': 50, 'salt': 20, 'flour': 45, 'cooking oil': 150, 'butter': 60, 'rice': 130, 'wheat': 80, 'jam': 60, 'tissues': 30
}

#display menu
print("Welcome to the store".center(50,'-'))
print("Product Name", "Price")
for i in products:
    print(i.ljust(12,' '), ':', products[i])

#taking the inputs from user - cart
carts = {}
while True:
    cart = input("Enter the product name(exit): ").lower()
    if cart == 'exit':
        break
    qua = int(input("Enter the quantity: "))
    carts[cart] = qua

#printing the bill
print("Bill".center(50,'-'))
print('Product Name Quantity Price')
bill = 0
for i in carts:
    print(i.ljust(12,' '), str(carts[i]).ljust(12,' '),products[i])
    bill += carts[i]*products[i]
print(f"Total bill: {bill}")
print("Thanks for Shopping😊")