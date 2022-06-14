# fibonacci series
a,b=0,1
lim=int(input("enter the limit "))
for i in range(1,lim+1):
    print(a)

    c=a+b
    a=b
    b=c
print(c)    



