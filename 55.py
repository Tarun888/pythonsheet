# factors of a number
value=1
num =int(input("enter the integer"))
while(value<=num):
    if(num%value==0):
        print("the factor of given nos is",value)
        value+=value
