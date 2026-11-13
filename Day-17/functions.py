#defining the function - to print the 1 to 10 numbers using loop
def numbers():
    for i in range(1, 11):
        print(i)
numbers()
numbers()
numbers()
numbers()
numbers()
#n times we will call the function it will print the output n 


#check whether the number is prime or not
def prime(n):
    c = 0
    for i in range(1, n+1):
        if n%i == 0:
            c+=1
    if c > 2:
        print("Not prime")
    else:
        print("Prime")
print(prime(int(input("Enter the number: "))))
#taking the input from user in the function calling

#(or)

def prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return "Not Prime"
    return "Prime"
print(prime(int(input("Enter the number: "))))


#sum of digits
def sum_of_digits(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum       
print(sum_of_digits(12345))
print(sum_of_digits(24681))



#reverse of a number
def revs(n):
    sum=0
    while n>0:
        sum= (sum*10) + n%10
        n//=10
    return sum       
print(revs(12345))
print(revs(24681))


#it will print according to the def function parameters order
def display(name,email,password):
    print("Name: ", name)
    print("Email: ", email)
    print("Password: ", password)
display("krishna","krishna@gmail.com","krishna@123")
display("ravi@gmail.com","ravi@123","ravi")
display("suresh@123","suresh","suresh@gmail.com")

#it will print according to assining order
def display(name,email,password):
    print("Name: ", name)
    print("Email: ", email)
    print("Password: ", password)
display(name="kiran",email="krian@gmail.com",password="krian@123")
display(email="harshi@gmail.com",password="harshi@123",name="harshi")
display(password="ammu@123",name="ammu",email="ammu@gmail.com")

#when don't give input it will print none
def display(name,email,password,phonenumber= None):
    print("Name: ", name)
    print("Email: ", email)
    print("Password: ", password)
    print("Phone Number: ", phonenumber)
display("amrutha","amrutha@gmail.com","amrutha@123")
display("kasi@gmail.com","kasi@123","kasi", 34567776574)
display("murthy@123","murthy","murthy@gmail.com")


# *n means takes the multiple inputs from user
def display(*n):
    print(n)
display(1,2,3,4)
display(1,2,3)
display(1,2,3,4,5,6)

# **n accepts the multiple keyword arguments - it will print like dict
def display(**n):
    print(n)
display(n1=1,n2=2,n3=3,n4=4)
display(n1=1,n2=2)
display(n1=1,n2=2,n3=3)