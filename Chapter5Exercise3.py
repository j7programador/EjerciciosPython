'''define a function that take list of words as argument and
return list with reverse of every element in that list'''


def element_reverse(l):
	lista=[]
	for i in l:
		lista.append(i[::-1])
	return lista

l=['jorge','toti','alma']

print(element_reverse(l))
print(l)


		
