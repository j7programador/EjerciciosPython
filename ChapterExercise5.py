#ask a user for name
#Example - Harshit Vashisth
#print count of each words
#output:
	#H:1
	#a:2
	#r:1
	#s:3
	#h:3
	#i:2
	#t:2
	# :1
	#V:1
	
name= input("ingrese un nombre: ")
name1=""
for i in name:	
	if i not in name1:
		name1+=i
		print(f'{i} : {name.count(i)}')
		

	
	
	
