# sum of numbers and skip negative numbers
sum=0
print("enter the 10 numbers")
for i in range(1,11):
 num=int(input("number %d="%i))
 if num<0:
   continue
sum=sum+num
print("the sum of 10 natural numbers skipping the negative nos is:",sum)


