# Name : Mostafa Ali 
# ID: 23120192

print("📚 Student Grade Analyzer 📚") ;
sup1="Math";
sup2="Science" ;
sup3="English";
x =int(input("Enter Math Score: "));
y =int(input("Enter Science Score: "));
z =int(input("Enter English Score: "));

Avrage=round(((x+y+z)/3),2) ;
print("\nAvrage Score:" , Avrage);
if Avrage>=90 :
    Grade="A (Excellent)";
elif Avrage>=80 and Avrage<=90 :
    Grade="B (Very Good)";
elif Avrage>=70 and Avrage<=80 :
    Grade="C (Good)";
elif Avrage>=60 and Avrage<=70 :
    Grade="Acceptable";
else :
    Grade="Fallen";
print("Grade: " , Grade);
if x>y and x>z :
   print("Best Subject: " ,sup1,"(",x,")" );
elif y>x and y>z :
    print("Best Subject: " ,sup2 ,"(",y,")");
else :
    print("Best Subject: " ,sup3 ,"(",z,")");
if x<y and x<z :
   print("worst Subject: " ,sup1 ,"(",x,")");
elif y<x and y<z :
    print("worst Subject: " ,sup2 ,"(",y,")");
else :
    print("worst10 Subject: " ,sup3 ,"(",z,")");


