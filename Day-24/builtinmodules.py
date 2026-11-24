import sys

#when ever excuting the program pass the parameters that it excute
print(sys.argv)
#['builtinmodules.py', '1', '2', '45', '7', '658', '7'] - output

#path of the program
print(sys.path)

#python version
print(sys.version)
#3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] - output

#exit from the program
#sys.exit()

#exit from the program this condition will not excute
print("Hello world")


import platform

#system where it is windows or mac
print(platform.system())

#release windows either 10 or 11
print(platform.release())

#processor of system intel 
print(platform.processor())

import math

#value of pi
print(math.pi)

#value of e
print(math.e)

#display float 
print(math.sqrt(16))
print(math.sqrt(25))
print(math.pow(2, 5))
print(math.pow(3, 3))

#round value gives less than 0.5 gives same number grater tha 0.5 gives next number
print(round(12.00000000001))
print(round(12.3))
print(round(12.8))
print(round(12.99999999999999999))

#ceil means gives upper value
print(math.ceil(12.00000000001))
print(math.ceil(12.3))
print(math.ceil(12.8))
print(math.ceil(12.99999999999999999))

#floor gives the lower value
print(math.floor(12.00000000001))
print(math.floor(12.3))
print(math.floor(12.8))
print(math.floor(12.99999999999999999))

#converts to positive integer
print(abs(-44))
#convert to positive interger and float value
print(math.fabs(-44))

#factorial of a number
print(math.factorial(6))
#greatest common divisor bw two numbers
print(math.gcd(12, 16))

print(math.log(2, 2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(120))
print(math.radians(120))

import random

#gives same random numbers repeatidly
random.seed(10)

#gives random value from 0 to 1
print(random.random())
#gives the random from according to given range
print(random.randint(1, 10))
#gives the random from according to given range in float value
print(random.uniform(1, 10))

l = ['python', 'java', 'c', 'c++', 'flask', 'mysql', 'fastapi']
#gives you one random chioce from list
print(random.choice(l))
#gives you k random chioce from list
print(random.choices(l, k=3))

print(l)
random.shuffle(l)      #shuffle the values in list
print(l)

from collections import Counter, defaultdict, deque

s = 'python programming'

#it will display frquency count
print(Counter(s))

#without counter function
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

s = 'java programming'
#intilizating the default value 0 according to datatype
d = defaultdict(int)
for i in s:
    d[i] += 1
print(d)


#dequeue is used when adding and deleting elements from either right or left based on our choice
s = deque([])
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.appendleft(9)
s.appendleft(8)
s.popleft()   #pop from left
s.pop()        #pop from right
print(s)


from itertools import combinations, permutations

#combinations abc - ab bc ca
#permutations abc - ab ba bc cb ca ac

s = 'abcd'
print([''.join(i) for i in combinations(s, 3)])
print([''.join(i) for i in permutations(s, 3)])