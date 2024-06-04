"""l=[1,2,3,4,5]
for i in range(1,4):
    l[i-2]=l[i]
for i in range(0,4):
    print(l[i],end=" ")"""
"""l=[1,2,3]
l1=l
l[0]=4
print(l1)"""
"""l=[1,2,3,8,4,7,6]
print(l.index(2))
print(l.count(2))
l.sort()
print(l)
l.reverse()
print(l)"""

#index(1) index at which two present
#copy()
#count(2) no of twos
#sort() for desending order sort(reverse=true)
#reverse()
#sum(l)
#min(l)
#max(l)
#len() to find lenght 
"""L=[2,3,4,5,3,150,7,8,9,222]
L.sort()
print(L[-2])
#nested list
l1=[1,3,5,[3,4,5,6],6,7,9,0]
print(l1)
#list compensation
l2=[x**2 for x in range(1,11) if x %2 == 0]
print(l2)"""
#take two different list ,merge them and printa new sorted list
"""a=map(int,input().split())
b=map(int,input().split())
a.extend(b)
a.sort()
print(a)"""
#input a list and sort the elements in the list accourdung yhe lenght
"""l=input().split()
l.sort(key=len)
print(l)
"""
#swap first and last input
"""a=input().split()
b=len(a)
temp=a[0]
a[0]=a[b-1]
a[b-1]=temp
print(a)"""
"""i=input().split()
i[0],i[-1]=i[-1],i[0]
print(i)"""
#print the list after the duplicate element in it
"""a=input().split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)"""
#print the element in the list which has occured odd number of times
"""a= input().split()
b=[]
for i in a:
    if a.count(i)%2 !=0 and i not in b:
        b.append(i)
print(b)"""
#Take the nested list having two values and sort the list according to the secord element in the list
"""n=input().split()
a=[input().split() for i in range(n)]
for explain later
 """
#read A list and print  sum of three minimum elements in the list (dublicate elements)
"""a=list(map(int,input().split()))
b=set(a)
c=list(b)
c.sort()
print(c)
print(sum(c[:3]))"""
"""a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(sum(b[:3]))"""
# segregate the given list as even elements first in descending order and the odd elements next in ascending order

"""a=list(map(int,input().split()))
b=[]
for i in a:
    if i%2==0:
        b.insert(0,i)
    else:
        b.append(i)
print(b)"""
#print product of the elements in the list which are within the given range.
"""a=list(map(int,input().split()))
b=[]
m,n=map(int,input().split())
for i in a:
    if i in range(m,n+1):
        b.append(i)
p=1
for i in b:
    p*=i
print(p)  """  
#given lists in alist ,find the maximum sum of elements of list in alist of lists and print its index
n=int(input())
a=[map(int,input().split()) for i in range(n)]
m=0
for i in a:
    s=sum(i)
    if s>m:
        m=s
        ind=a.index(i)
print(ind)