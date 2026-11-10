#syntax for nested loop:
#for i in sq:
#    for j in seq:
#        #statements
#    print()  

#print the numbers from 0 to 4 -> in seperate rows
for row in range(3):
    for col in range(5):
        print(col, end = ' ')
    print()

#print 5 rows and 5 columns in 1
for i in range(5):
    for j in range(5):
        print(1, end = ' ')
    print()

#print 5 rows and cloumns in *
for i in range(5):
    for j in range(5):
        print('*', end = ' ')
    print()



#1 0 1 0 1 
#0 1 0 1 0 
#1 0 1 0 1 
#0 1 0 1 0 
#1 0 1 0 1

#1 displaying in the even numbers places
#0 displaying in odd numbers places

for  row in range(5):
    for col in range(5):
        if (row+col)%2 == 0:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

for row in range(5):
    for col in range(5):
        print(int((row+col)%2 == 0), end = ' ')
    print()


#0 1 0 1 0 
#0 1 0 1 0 
#0 1 0 1 0 
#0 1 0 1 0 
#0 1 0 1 0 
for i in range(5):
    for j in range(5):
        print(j%2, end=' ')
    print()


#1 2 3 4 5 
#6 7 8 9 10 
#11 12 13 14 15 
#16 17 18 19 20 
#21 22 23 24 25 
c = 1
for i in range(5):
    for j in range(5):
        print(c, end=' ')
        c+=1
    print()


#0 0 0 0 0 
#0 1 2 3 4 
#0 2 4 6 8 
#0 3 6 9 12 
#0 4 8 12 16 
for i in range(5):
    for j in range(5):
        print(i*j, end = ' ')
    print()


#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(i+1):
        print('*', end = ' ')
    print()

    
#* * * * * 
#* * * * 
#* * * 
#* * 
#* 
n = int(input("Enter the size: "))
for i in range(5):
    for j in range(n-i):
        print('*', end = ' ')
    print()