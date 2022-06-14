# sum of natural nos until users enter a possitive number
sum=0
print("enter the 10 numbers")
for i in range(1,11):
 num=int(input("number %d="%i))
 if num<0:
     break
 sum=sum+num
   
print("the sum of 10 natural numbers skipping the negative nos is:",sum)


