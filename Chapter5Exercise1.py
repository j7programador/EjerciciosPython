#define a function which will take list containing numbers as input
#and return list containing square of every elements
n=int(input('Ingrese el numero de enteros de la lista: '))
l=[]
for i in range(n):
	a= int(input())
	l.append(a)
	
def square_list(l):
	lista=[]
	for i in l:
		lista.append(i**2)
	return lista
print(square_list(l))
		
