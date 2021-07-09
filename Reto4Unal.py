import json
diccionario=input()
miDiccionario=json.loads(diccionario)
lista=input().split()
listaComprables=[]
#print(miDiccionario)
suma=0
for i in lista:
	if i in miDiccionario.keys():
		listaComprables.append(i)
		suma+=miDiccionario[i]
print(suma)
for j in listaComprables:
	print(j,end=" ")
print("")

			
	
