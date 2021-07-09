#common elements finder function
#define a functions which take 2 list as input and return a list
#which contains common elements of both lists

#example input [1,2,5,8], [1,2,7,6]
#output [1,2]

def common_elements(lista1,lista2):
	listaEnd=[]
	a=[]
	if len(lista1)>len(lista2):
		a=lista1
	else:
		a=lista2
	for i in a:
		if i in lista1 and i in lista2:
			listaEnd.append(i)
	return listaEnd
def common_finder(l1,l2):
	output=[]
	for i in l1:
		if i in l2:
			output.append(i)
	return output
lista1=[1,2,5,8]
lista2=[1,2,7,6]
print(common_elements(lista1,lista2))
print(common_finder(lista1,lista2))
	
