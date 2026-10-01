l=[]
def add():
	global l
	a=int(input("enter the student rollno:"))
	b=input("enter the student name:")
	l.append([a,b])
	print("name added successfully")
def display():
	for i in l:
		print(i)
def search():
	s=int(input("enter the roll no to search:"))
	for i in l:
	   if s==i[0]:
	      print(i)
	   else:
	      print("not found")
			
	
