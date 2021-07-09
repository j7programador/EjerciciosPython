lista=[]
lista1=[]
for i in range(3):
	for a in range(3):
		n=int(input())
		lista1.append(n)
	lista.append(lista1)
	lista1=[]
print(lista)
for i in range(3):
	for a in range(3):
		print(lista[i][a],end=' ')
			
print("\n")
lista=[[int(input()) for i in range(3)] for i in range(3)]
print(lista)
