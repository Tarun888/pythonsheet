# sum of fibonacci
sum=0 
a,b=0,1
lim=int(input("enter the limit "))
for i in range(1,lim+1):
    print(a)

    c=a+b
    a=b
    b=c
    sum=sum+c
# print("the fibo series is",c)
print("the sum of fibo series is",sum)
    
