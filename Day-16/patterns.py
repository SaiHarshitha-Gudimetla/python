'''#        * 
#      * * 
#    * * * 
#  * * * * 
#* * * * * 

n = int(input("Enter the number: "))
for row in range(n):
    for sp in range(n-1-row):
        print(' ', end=' ')
    for col in range(row+1):
        print('*', end=' ')
    print()


#* * * * * 
#  * * * * 
#    * * * 
#      * * 
#        * 

n = int(input("Enter the number: "))
for row in range(n):
    for sep in range(row):
        print(' ', end= ' ')
    for col in range(n-row):
        print('*', end=' ')
    print()

#*
#* *
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#* 

n = int(input("Enter the size: "))
m = n//2
for row in range(n):
    if row <= m:
        for col in range(row+1):
            print('*', end=' ')
    else:
        for col in range(n-row):
            print('*', end=' ')
    print()

#                       (or)

n = int(input("Enter the size: "))
m = n//2
for row in range(n):
    if row <= m:
        print('* '*(row+1))
    else:
        print('* '*(n-row))      

#                     (or)

n = int(input("Enter the size: "))
m = n//2
for row in range(n):
    print('* '*(row+1) if row <= m else '* '*(n-row))          


#* * * * * 
#*       * 
#*       * 
#*       * 
#* * * * * 

n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()                

#* * * * * * * * * 
#*       *       * 
#*       *       * 
#*       *       * 
#* * * * * * * * * 
#*       *       * 
#*       *       * 
#*       *       * 
#* * * * * * * * * 

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1 or i == m or j == m:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()                 

#* * * * * * * * * 
#* *     *     * * 
#*   *   *   *   * 
#*     * * *     * 
#* * * * * * * * * 
#*     * * *     * 
#*   *   *   *   * 
#* *     *     * * 
#* * * * * * * * * 

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1 or i == m or j == m or i == j or i+j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()                         

#A
#* * * * * 
#*       * 
#* * * * * 
#*       * 
#*       * 
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or j == n-1 or i==m:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()                 

#B
#* * * * * 
#*       * 
#* * * * * 
#*       * 
#* * * * * 
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or j == n-1 or i==m or i == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()   

#C
#* * * * * 
#*         
#*         
#*         
#* * * * *
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()         

#D
#* * * * * 
#*       * 
#*       * 
#*       * 
#* * * * * 
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i==n-1 or j==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()                   

#E
#* * * * * 
#*         
#* * * * * 
#*         
#* * * * * 
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i==n-1 or i==m:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()                 

#F
#* * * * * 
#*         
#* * * * * 
#*         
#*
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or  i==m:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#G
#* * * * * 
#*         
#*   * * * 
#*       * 
#* * * * * 

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or (j == n-1 and i >= m) or (i == m and j >= m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()    

#H
#*       * 
#*       * 
#* * * * * 
#*       * 
#*       * 
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or i==m or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()   

#I
#* * * * * 
#    *     
#    *     
#    *     
#* * * * *
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j==m or i == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


#j
#* * * * * 
#    *     
#*   *     
#*   *     
#* * * 

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == m or (i==n-1 and j<=m) or (j==0 and i>=m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()          

#K
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or (i+j==m and i<=m) or (i-j==m and i>=m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()        

#L
#*         
#*         
#*         
#*         
#* * * * * 
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or i == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()          

#M
#*       * 
#* *   * * 
#*   *   * 
#*       * 
#*       *

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()                         

#N
#*       * 
#* *     * 
#*   *   * 
#*     * * 
#*       * 

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()    

#O
#* * * * * 
#*       * 
#*       * 
#*       * 
#* * * * *
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()    

#P
#* * * * * 
#*       * 
#* * * * * 
#*         
#*
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or i == 0 or (j == n-1 and i<=m) or i==m:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()            

#Q
#R 
#S 
#* * * * * 
#*         
#* * * * * 
#        * 
#* * * * * 
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or (j==0 and i<=m) or i==m or (j==n-1 and i>=m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#T 
#* * * * * 
#    *     
#    *     
#    *     
#    *  
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or  j==m:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()'''   

#U 
#*       * 
#*       * 
#*       * 
#*       * 
#* * * * *
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#V 
#W 

#X
#*       * 
#  *   *   
#    *     
#  *   *   
#*       * 
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==j or i+j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#Y 
#*       * 
#  *   *   
#    *     
#    *     
#    *  
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if (i==j and j<=m) or (i+j == n-1 and j>=m) or (j==m and i>=m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#Z  
#* * * * * 
#      *   
#    *     
#  *       
#* * * * *
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()           