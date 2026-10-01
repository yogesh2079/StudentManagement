import student
print("1. add a student/n 2. display student details/n 3. search for a student/n 4.exit")
while True:
   n=int(input("enter number:"))
   if n==1:
   	student.add()
   elif n==2:
   	student.display()
   elif n==3:
   	student.search()
   elif n==4:
   	break
   else:
   	print("invalid")
  

