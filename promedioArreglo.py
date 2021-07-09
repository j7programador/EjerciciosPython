Arreglo=input("Ingrese los números reales del arreglo(separados por un espacio): ").split()

for i in range(len(Arreglo)):
	Arreglo[i]=float(Arreglo[i])
	
promedio=sum(Arreglo)/len(Arreglo)
print("El promedio del arreglo de reales es de:",promedio)





