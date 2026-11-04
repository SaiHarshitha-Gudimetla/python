#Sting list tuple set dict range()

#iterating the string
s = "Codegnan"
for i in s:
    print(i)

#checking the vowels
a = input("Enter the word: ")
for i in a:
    if i in 'aeiouAEIOU':
        print(i) 

#list of elements to iteration - check the even numbers
s = [10,23,45,89,34,85,12]
for i in s:
    print(i)


a = list(map(int, input("Enter the nums: ").split()))
for i in a:
    if i%2 == 0:
        print(i)  


#tuple iteration - sum of tuple
s = (10,23,45,89,34,85,12)
for i in s:
    print(i)

sumoftuple = 0
a = tuple(map(int, input("Enter the nums: ").split()))
for i in a:
    sumoftuple += i
print("Sum of Tuple: ", sumoftuple)  


#set iteration - max of set
s = {10,23,45,89,34,85,12}
for i in s:
    print(i)

max = 0
a = set(map(int, input("enter the nums: ").split()))
for i in a:
    if i>max:
        max = i
print("Max of set: ", max)    


#dict iteration - sum of marks of students
marks = {'python': 90, 'mysql': 85, 'fastapi': 80, 'html': 85, 'css': 90}
for i in marks:
    print(i, marks[i])

sum = 0
marks = {'python': 90, 'mysql': 85, 'fastapi': 80, 'html': 85, 'css': 90}
for i in marks:
    sum += marks[i]
print("Total Marks: ", sum)   


#range(start, end+1, step)
#range is going the generate the sequence of values

#from 1 to 10
for i in range(1,11):
    print(i, end = ' ')  

#from 20 to 1
for i in range(20,0,-1):
    print(i,end=' ')    

#from 1 to 100 only even numbers
for i in range(2,100,2):
    print(i, end=' ')      

#printing the table
n = int(input("Enter the table no: "))
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')    

#input - codegnan, output - c0o1d2e3g4n5a6n7
c = "Codegnan"
for i in range(len(c)):
    print(c[i], i, end = ' ')      

#[12,34,45,10,78,43,80]  - even number indxes - sum of indexes
#0+1+3+4+6 = 14
sum= 0
a = [12,34,45,10,78,43,80]
for i in range(len(a)):
    if a[i]%2 == 0:
        sum += i
print("sum:",sum)  

#break
for i in range(1,11):
    if i == 5:
        break
    print(i)        # 1 2 3 4

#continue
for i in range(1,11):
    if i == 5:
        continue 
    print(i)       # 1 2 3 4 6 7 8 9 10

#pass
for i in range(1,10):
    pass

if True:
    pass

class Booking:
    pass

def func():
    pass

#(12,34,45,10,78,43,80) - odd number indxes - product of indexes
product = 0
t = (12,34,45,10,78,43,80)
for i in range(len(t)):
    if t[i]%2 != 0:
        product *= i 
print("Product:", product)