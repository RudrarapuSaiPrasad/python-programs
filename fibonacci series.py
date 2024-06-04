"""n=int(input("enter the value"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b"""
def fibonacci(n):
    if n<=1:
        return n
    else :
        return fibonacci(n-1)+fibonacci(n-2)
b=int(input("enter the number : "))
for i in range(b):
    print(f"fibonacci{i}={fibonacci(i)}")