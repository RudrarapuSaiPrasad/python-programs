n=int(input() )
event=list(map(int,input("enter the number: ").split("  ")))    
for _ in range(n):
    unsolved=0
    if(event==-1):
        if(noofpolice==0):
            noofpolice-=1
        else:
            unsolved+=1
else:
    noofpolice+=event
print(unsolved)
