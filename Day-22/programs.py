#input: 61111113344445556662222
#output: 61163244536324

n=str(61111113344445556662222)
c=1
res=''
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        c+=1
    else:
        res+=n[i]+str(c)
        c=1
print(res+n[i]+str(c))

#find missing and repeating number from 1 to n

n=[1,2,3,4,5,6,6]
for i in range(len(n)):
    if n.count(i)>1:
        print("Repeating number:",i)
    
p=set(n)
l=(len(n)*(len(n)+1))//2
s=sum(p)
print('Missing number:',l-s)


#[{()}]  balanced
#[{(})]  unbalanced

b='[]([[(])])'
res=[]
for i in b:
    if i in ('{','[','('):
        res.append(i)
    elif res==[]:
        print("Unbalanced")
        break
    elif i=='}':
        p=res.pop()
        if p!='{':
            print("Unbalanced")
            break
    elif i==')':
        p=res.pop()
        if p!='(':
            print("Unbalanced")
            break
    elif i==']':
        p=res.pop()
        if p!='[':
            print("Unbalanced")
            break
else:
    print("Balanced")