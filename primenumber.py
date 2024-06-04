def primenum():
    num=int(input("Enter the number: "))
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num % 2==0:
                print(num,"is not the prime number")
        else:
                print(num,"prime number")
    else:
        print(num,"is not a prime number")
primenum()