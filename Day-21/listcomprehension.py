#List comprehension - A list comprehension is a concise, single-line Python syntax 
#                     used to create a new list by transforming or filtering items 
#                     from an existing iterable (like a list, tuple, or range). 
#                     It replaces traditional for loops and .append() calls with cleaner, faster code.

#list Comprehension means that list is to declaration, iteration, updation

#l=[]
#for
#update

#res = [update for]

#print the elements from 1 to 10
res = [i for i in range(1,11)]
print(res)

#factors of a number
n = 16
fact = [i for i in range(1, n+1) if n%i == 0]
print(fact)

#display the names starts with s
names = ['sai harshitha', 'sai amrutha', 'kasi', 'murthy']
resn = [i for i in names if i.startswith('s')]
print(resn)

#in the list print the even numbers, in odd numbers display the 0
l =[2,4,7,5,65,435,4,53,23,3,645,787,8]
rese = [i if i%2 == 0 else 0 for i in l]
print(rese)

#diaplay the numbers 1,2,3 for 5 times
nes  = [[j for j in range(1,4)] for i in range(5)]
print(res)

#set comprehension

#print numbers from 1 to 10
res = {i for i in range(1,11)}
print(res)

#factors of given number
n = 16
fact = {i for i in range(1,n+1) if n%i == 0}
print(fact)


#dictoinary comprehension

res = {i:i+10 for i in range(1,11)}
print(res)