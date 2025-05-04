print ('*** Welcome To Calculator App ***\nEnter tow numbers : ')
n1=float(input("first number:" ))
n2=float(input("second number:" ))
print('''
selsect the opration:
1- add
2- sub 
3- multibly
4- divition

''')
opration=int(input("opration number:" ))
if opration==1:
    result=n1+n2;
    print ("the sum = ",result)
elif opration==2:
    result=n1-n2;
    print ("the sub = ",result)
elif opration==3:
    result=n1*n2
    print ("the multiply = ",result)
elif opration==4:
    if n2==0 :
        print("error the second number = zero!\n")
    else :
        result=n1/n2;
        print ("the divition = ",result)
else :
    print ("error :please selsect the correct opration number in the next time :)!\n")
 
