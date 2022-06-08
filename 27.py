# students grade
marks = int(input("Enter marks"))  
if marks>=90:
    print("A grade")
elif(marks<90 and marks>=75 ) :   
    print("B grade")
elif(marks<75 and marks>=60) :   
    print("C grade")
elif(marks<60 and marks>=50 )  :  
    print("D grade")
elif(marks<60 and marks>=40 )  :  
    print("D grade")
elif(marks==40 )  :  
    print("just passed")
    
elif(marks<40 )  :  
    print("failed")
else:
    print("invalid")    

