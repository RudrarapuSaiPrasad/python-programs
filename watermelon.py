a=int(input("enter the weight : "))
if(a%2!=0):
    print("no")
else:
    x=a/2
    if(x%2==0):
         print("weight of two pices",x,x)
    else:
        print("weight of two pices",x-1,x+1)

      