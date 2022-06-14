from re import I


a=float(input("enter the first value a"))
b=float(input("enter the second value b"))

i=1
while(i<=a and i<=b):
    if(a%i==0 and b%i==0):
        val=i
    i=i+1
print("hcf of {0} and {1} ={2}".format(a,b,val))  