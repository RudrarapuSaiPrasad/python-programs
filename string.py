"""str=input(" ")
print(str.index("a"))
print(str.rindex("a"))
print(len(str))
print(str.upper())
print(str.lower())"""
# wap to remove consective duplicate from the given string 
"""str=input(" ")
result=str[0]
for i in range(1,len(str)):
    if str[i]!=result[-1]:
        result+=str[i]
print(result)"""
#move allspace to the front of a given string
"""str=input()
space=" "
result=" "
for i in str:
    if i==" ":
        space+=i
    else:
        result+=i
d=space+result
print(d)"""
#write a program to create a string  from two given strings concatering uncommon characters of the said strings
"""s1=input()
s2=input()
uncommon="".join(set(s1)^set(s2))
print(uncommon)"""
#wap program to find the max occurance character in the given string
s=input()
char=max(s,key=s.count())
print(f"maximum occurring character:{char}")