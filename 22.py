from math import*
rate=int(input("enter the rate"))
principle_amnt=int(input("enter the principal_amnt"))
n=int(input("enter the no. of times interest"))
t=int(input("enter the no. of time period"))
a=(principle_amnt*(1+rate/n)**(n*t))
print(a)