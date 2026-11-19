'#recursion is calling the function itself until the base condition is satisfy


#print numbers 1 to 10
def display(n):
    if n > 10:
        return
    print(n)
    display(n+1)
display(1)

#print numbers 10 to 1
#when ever print the statement outside the base condition it will reverse the elements
def display(n):
    if n > 10:
        return
    display(n+1)
    print(n)
display(1)

#print the string "python programming" to print letters with space
def display(n):
    if n == len(s):
        print()
        return
    print(s[n], end=' ')       #p y t h o n   p r o g r a m m i n g 
    display(n+1)
    print(s[n], end=' ')        #g n i m m a r g o r p   n o h t y p
s = "python programming"
display(0)

#python is print in
#p
#py
#pyt
#pyth
#pytho
#python
def display(n):
    if n == len(s):
        return
    print(s[:n+1])
    display(n+1)
s = "python"
display(0)

#string codegnan
# when passing parameters like
#0,3            0,4
#cod            code
#ode            odeg
#deg            degn
#egn            egna
#gna            gnan
#nan
def display(n,w):
    if n > len(s)-w:
        return
    print(s[n:n+w])
    display(n+1,w)
s = "Codegnan"
display(0,3)

#sum of numbers
def display(n):
    if n < 1:
        return 0 
    return n + display(n-1)
print(display(10))     #55

#factorial of a number
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)
print(factorial(6))           #720

#sum of elements in list
#l = [34,5,567,8,234,7,68,83]
def sumoflist(n):
    if n == len(l):
        return 0 
    return l[n] + sumoflist(n+1)
l = [34,5,567,8,234,7,68,83]
print(sumoflist(0))         #1006

