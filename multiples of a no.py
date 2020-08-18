#multiples of a number
a=int(input("enter a number"))
b=int(input("enter a number"))
n=int(input("enter a number"))
for i in range(a,b+1):
    if i%n==0:
        print(i,end=" ")
