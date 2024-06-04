"""d={1:"hii",2:"hello",3:"hellofriends"}
print(d[1])
print(d.get(2))
for i in d:
    print(i," :",d[i])"""
#d. get()
#d.update(key:value)
#d.pop(key)
#d.popitem()
#d.clear()
#key() to print keys
#values()to print values
#items() return of dict (key,values)tuple pairs
#fromkey()
#setdefault()
"""d={"a","b","c","d"}
d=dict.fromkeys(d,10)
print(d)
print(d.setdefault("a"))"""
#nested dictionary
"""d={1:"hi","a":123,100:{2:"abc","x":452,2.3:120},5.4:"python"}
print(d[100]["x"])"""
#write a program to add a key to a dictionary
"""import operator
d={}
n=int(input())
for i in range(n):
    k=input("enter  the key value : ")
    v=input("enter its value: ")
    d[k]=v
key=input()
value=input()
d.update({key:value})
print(d)"""
#to check key is present in the dictionary
"""import operator
d={}
n=int(input())
for i in range(n):
    k=input("enter  the key value : ")
    v=input("enter its value: ")
    d[k]=v
g=input(" ")
if g in d:
        print("key is present")
else :
      print("key is not present")
print(d)"""
#python program to generate and print a dictionarys 
"""n= input("input the number")
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)
"""
#merge two python dictionaries
"""d={}
d1={}
n=int(input())
for i in range(n):
    k=input("enter  the key value : ")
    v=input("enter its value: ")
    d[k]=v
for i in range(n):
    k=input("enter  the key value : ")
    v=input("enter its value: ")
    d1[k]=v
d2=d.copy()
d2.update(d1)
print(d2)"""
#`to remove thekey from a dictionary
"""d1={}
n=int(input())
for i in range(n):
    k=input("enter  the key value : ")
    v=input("enter its value: ")
    d1[k]=v
print(d1)
n=input("enter the key to remove ")
d1.pop(n)
print"""
#to map two list into dictionary
"""keys=input().split()
values=input().split()
d=dict(zip(keys,values))
print(d)"""
#to combine two dictionarynadding values for common keys
from collections import Counter
"""d={}
d1={}
n=int(input())
for i in range(n):
    k=input("enter  the key value : ")
    v=input("enter its value: ")
    d[k]=v
for i in range(n):
    k=input("enter  the key value : ")
    v=input("enter its value: ")
    d1[k]=v
    d2=counter(d)+counter(d1)
    print(d2)"""