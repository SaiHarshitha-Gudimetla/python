#To using the generator function using the yield keyword
def reels():
    res = ('1-100', '101-200', '201-300', '301-400', '401-500', '501-600', '601-700')
    #yield keyword is used to return the multiple times in one function
    yield res[0]
    yield res[1]
    yield res[2]
    yield res[3]
    yield res[4]
    yield res[5]
    yield res[6]

    #instead of writing the all statements just itearte in the loop
    for i in res:
        yield i

feed = reels()
#call the function multiple times
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))

#instead calling all functions just itearte in loop
for i in feed:
    print(i)

#generate the factors of number using the generator
def factorsofnumber(n):
    for i in range(1,n+1):
        if n%i == 0:
            yield i

res  = factorsofnumber(12)
for i in res:
    print(i)

#prime numbers upto 100
def primenumbers(n):
    for i in range(2,n+1):
        for j in range(2, i//2+1):
            if i%j == 0:
                break
        else:
            yield i
res = primenumbers(100)
for i in res:
    print(i)


#basic for loop concept for fibonacci series
n = 10
a = 0
b = 1
print(0,1)
for i in range(n-2):
    c = a+b
    print(c)
    a = b
    b = c

##fibonacci series upto 10
def fibonacciseries(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b

res = fibonacciseries(10)
for i in res:
    print(i)

#(or)

def fib(n):
    if n == 1:
        yield 0
    elif n >= 2:
        a, b = 0, 1
        yield 0 
        yield 1
        for _ in range(n-2):
            c = a+b
            a = b
            b = c
            yield c

res = fib(10)
for i in res:
    print(i)
