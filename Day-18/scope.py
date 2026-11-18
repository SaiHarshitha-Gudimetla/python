#Local scope - variable is declared in inside of function is access in inside only
#Global Scope - variable is declared in outside of function is acces in inside and outside of function

def display():
    n = 10
    print("Inside function:",n)
display()
print("Outside the function:",n)
#Inside function: 10
#Traceback (most recent call last):
#  File "C:\Users\gudim\OneDrive\Documents\python full stack\Day-18\scope.py", line 8, in <module>
#    print("Outside the function:",n)
#NameError: name 'n' is not defined


#global keyword - it used to variable is inside the function 
#                 and it used in outside also
#using the global keyword don't pass the variable as paramaters
def display():
    global n 
    n = 10
    print("Inside the function:",n)
display()
print("Outside the function:",n)
#Inside the function: 10
#Outside the function: 10

def display():
    course = "JFS"
    print("Starting: ",course)
    def update():
        course = "PFS"
        print("Ending: ",course)
    update()
    print("Final: ",course)
display()
#Starting:  JFS
#Ending:  PFS
#Final:  JFS


#nonlocal - it used when the inside the function variable is access (outside of that function) in the inside of the another function

def display():
    course = "JFS"
    print("Starting: ",course)
    def update():
        nonlocal course
        course = "PFS"
        print("Ending: ",course)
    update()
    print("Final: ",course)
display()
#Starting:  JFS
#Ending:  PFS
#Final:  PFS

#it declare the inbulit functions as variables
#because it act as variable

s = "codegnan"
len = 10
print(len(s))

#Traceback (most recent call last):
#  File "C:\Users\gudim\OneDrive\Documents\python full stack\Day-18\scope.py", line 62, in <module>
#    print(len(s))
#TypeError: 'int' object is not callable

s = "codegnan"
max = 10
print(max(s))

#Traceback (most recent call last):
#  File "C:\Users\gudim\OneDrive\Documents\python full stack\Day-18\scope.py", line 72, in <module>
#    print(max(s))
#TypeError: 'int' object is not callable