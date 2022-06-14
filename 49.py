# sum of even and odd numbers 
add=0
sum=0
lim=int(input("enter the limit "))
for i in range(1,lim+1):
    if i%2==0:
    
     sum=sum+i
    else:
        add=add+i

print("the sum of even  number is:",sum)
print("the sum of odd  number is:",add)
