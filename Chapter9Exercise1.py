'''define a function that take list of strings
list containing reverse of every string '''

lista=['abc','tuv','xyz']
def listReverse(lista):
	lista=[i[::-1] for i in lista]
	return lista

print(listReverse(lista))
