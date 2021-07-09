#Exercise -WATCH COCO
#Ask user's name and age 
# If user's name start with ( 'a' or 'A') and age is above 10
#print 'you can watch coco movie'
#else print ' sorry, you cannot watch coco'

name, age = input("ingrese su nombre y edad(separados por un espacio)").split(" ")
age = int(age)
name= name.lower()

if name[0]=='a'and age >10:
	print("'you can watch coco movie'")
else: 
	print("'sorry, you cannot watch coco'")

