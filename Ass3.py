#Name: Ayman Shaaban
#ID: 23120261
#1
file=open("students.txt" ,"w")
#2
file.writelines([
    "student_name, grade\n",
    "Ali, 85\n",
    "Sara, 91\n",
    "Jone, 78\n",
    "Noor, 95\n",
    "Omar, 62\n"
])
file.close()
#3
file=open("students.txt" ,"r")
lines=file.readlines()
print("lines as list : ",lines)
file.close()
#4
file = open("students.txt", "r")
lines = file.readlines()
file.close()

for i in lines[1:]:
    name,grade= i.split(",")
    print("student : " , name , "|" , "Grade : "  , grade)
#5
print("input a new student name and grade :\n")
Nname=input("new student name : ")
Ngrade=input("new student grade : ")
#6
file=open("students.txt" ,"a")
file.writelines([Nname ,", ",Ngrade])
file.close()
#7
file = open("students.txt", "r")
lines = file.readlines()
file.close()
for i in lines[1:]:
    name,grade= i.split(",")
    print("student : " , name , "|" , "Grade : "  , grade)
#8
file = open("students.txt", "r")
lines = file.readlines()
file.close()
for i in lines[1:]:
    name,grade= i.split(",")
    if(int(grade)>=60):
        print(name,"-Pass")
    else:
       print(name,"-Fail") 
