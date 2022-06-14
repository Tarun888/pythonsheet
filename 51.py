# count no. og digit in given number
count=0
number=int(input("enter the limit "))
for i in range(1,number+1):
    if number>0:
        number=number//10
        count=count+1
print("no. of digits in given number is",count)  



