numero=int(input("Ingrese el numero hasta donde vamos a elevar al cubo: "))
def CubeDictionary(n):
	cubes={}
	for i in range(1,n+1):
		cubes[i]=i**3
	return cubes

print(CubeDictionary(numero))


