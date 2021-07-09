#define a fuction which will take list as a argument and this function
#will return a reversed list
#note you simply do this with reverse method or [::-1]
#but try to do this with the help of append and return method

n=int(input('Ingrese el numero de enteros de la lista: '))
l=[]
for i in range(n):
	a= int(input())
	l.append(a)
	
def reverse_list(l):
	a=len(l)-1
	lista=[]
	for i in range(len(l)):
		lista.append(l[a-i])
	return lista
print(reverse_list(l))

		
