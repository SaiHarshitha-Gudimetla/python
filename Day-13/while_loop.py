#int
#while cond:
    #statement
    #update

#remove the 0's from list
l= [1,0,3,0,4,0,0,0,0,5,0,6,0,4,0]
while 0 in l:
    l.remove(0)
print(l)

#print numbers form 1 to 10
i = 1
while i<11:
    print(i)
    i+=1

#print numbers from 10 to 1
i = 10
while i>0:
    print(i)
    i-=1

#print even numbers from 2 to 100
i = 2
while i<101:
    print(i)
    i+=2

#print multiples of 5
i = 5
while i<101:
    print(i)
    i+=5

#"while" can iterate only the Sting, list, tuple
#set, dict can iterate

#how to iterate the string
a = 'Python Programming'
i = 0
while i<len(a):
    print(i,a[i])
    i+=1

#how to iterate the list
l = [1,3,5,6,7,9,8]
i = 0
while i<len(l):
    print(i,l[i])
    i+=1

#how to iterate the tuple
t = (53,534,42,657,56,3,53,334)
i = 0
while i<len(t):
    print(i,t[i])
    i+=1


#break - when value is 5
l = [1,3,5,6,7,9,8]
i = 0
while i<len(l):
    if l[i] == 5:
        break
    print(i,l[i])
    i+=1

#continue - when value is 5
l = [1,3,5,6,7,9,8]
i = 0
while i<len(l)-1:
    i+=1
    if l[i] == 5:
        continue
    print(i,l[i])


#codegnan 
#cn oa dn eg

c = 'pythonprogramming'
i = 0
j = len(c)-1
while i<=j:
    if i==j:
        print(c[i])
    else:
        print(c[i], c[j])
    i+=1
    j-=1