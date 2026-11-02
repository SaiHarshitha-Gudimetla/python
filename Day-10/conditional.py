#Simple If - product is best seller or not
product = input("Enter the product: ")
bestseller = eval(input("Enter the status: "))

if bestseller:
    print(f'{product} is bestseller.')



#Simple-If - Battery Charging
battercharge = int(input("Enter the battery:"))

if battercharge<20:
    print(f'Battery is low: {battercharge}, charge your phone.')


#Simple If - bill
bill = int(input("Enter the bill: "))
status = eval(input("Is it raining? "))

if status:
    bill+=30
    print("Extra Delivery charges applied")
print(f"Final Bill: {bill}")