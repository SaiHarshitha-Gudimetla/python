#Pass by value: passing values of immutuable
#Pass by refernce: passing values of mutuable

#int float str list tuple set dict bool
#it will not effect the values outside the function
#int float str tuple bool
#it will effect the values outside the function
#list set dict

#int
def display(n):
    n += 10
    print("Inside function: ", n)
n = 10
display(n)
print("Outside function: ",n)
#Inside function:  20
#Outside function:  10

#float
def display(n):
    n += 10.3
    print("Inside function: ", n)
n = 10.3
display(n)
print("Outside function: ",n)
#Inside function:  20.6
#Outside function:  10.3

#str
def display(n):
    n += "Programming"
    print("Inside function: ", n)
n = "Python"
display(n)
print("Outside function: ",n)
#Inside function:  PythonProgramming
#Outside function:  Python

#list
def display(n):
    n.append(10)
    print("Inside function: ", n)
n = [1,2,3,4]
display(n)
print("Outside function: ",n)
#Inside function:  [1, 2, 3, 4, 10]
#Outside function:  [1, 2, 3, 4, 10]

#tuple
def display(n):
    n = (5,6,7,8)
    print("Inside function: ", n)
n = (1,2,3,4)
display(n)
print("Outside function: ",n)
#Inside function:  (5, 6, 7, 8)
#Outside function:  (1, 2, 3, 4)

#set
def display(n):
    n.update({5,6,7})
    print("Inside function: ", n)
n = {1,2,3,4}
display(n)
print("Outside function: ",n)
#Inside function:  {1, 2, 3, 4, 5, 6, 7}
#Outside function:  {1, 2, 3, 4, 5, 6, 7}

#dict
def display(n):
    n[5] = 5
    print("Inside function: ", n)
n = {1:1,2:2,3:3,4:4}
display(n)
print("Outside function: ",n)
#Inside function:  {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
#Outside function:  {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

#bool
def display(n):
    n = False
    print("Inside function: ", n)
n = True
display(n)
print("Outside function: ",n)
#Inside function:  False
#Outside function:  True