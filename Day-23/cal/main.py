#importing the file as alias
import logic as lg

print(lg.add(20,10))
print(lg.sub(20,10))
print(lg.mul(20,10))
print(lg.div(20,10))
print(lg.mod(20,10))
print(lg.pow(20,10))


#importing the all functions in the file
from logic import *

print(add(20,10))
print(sub(20,10))
print(mul(20,10))
print(div(20,10))
print(mod(20,10))
print(pow(20,10))


#when ever we want only one or two functions in the file
#specify that functions
from logic import add,sub

print(add(20,10))
print(sub(20,10))