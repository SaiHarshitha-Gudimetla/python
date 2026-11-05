#for with else - pin verification

pin = 1234
for i in range(5):
    epin = int(input("Enter the pin: "))
    if epin == pin:
        print("Login Successful")
        break
    else:
        print("Invalid pin")
else:
    print("Max Attempts Reached! Try again after 30 secs")


# l = [2,4,6,7,90,24,45,34,56,40] - search the number at which index

l = [2,4,6,7,90,24,45,34,56,40]
search = int(input("Enter a number: "))
for i in range(len(l)):
    if l[i] == search:
        print(f"Search is found at {i}")
        break
else:
    print(f"{search} is not found")    

#enumerate -  generate sequence numbers
c = "Codegnan"                         #string
for i in enumerate(c):
    print(i[0], i[1])              

l = [23,34,345,56,7,34,7,645]            #list
for i in enumerate(l):
    print(i[0], i[1])                   

t = (53,533,7,5,45,57,46,6,64)          #tuple
for i in enumerate(t):
    print(i[0], i[1])                       

s = {1,43,654,657,45,23,5345}             #set
for i in enumerate(s):
    print(i[0], i[1])

d = {"k1": "v1", "k2": "v2", "k3": "v3"}   #dict
for i in enumerate(d):
    print(i[0], i[1], d[i[1]])