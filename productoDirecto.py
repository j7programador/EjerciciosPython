''' Un algoritmo que calcule el producto directo de dos vectores de igual tamaño'''

productoDirecto=[]
Arreglo1=[]
Arreglo2=[1]
while len(Arreglo1)!=len(Arreglo2):
	Arreglo1= input("ingresar los valores del primer arreglo: ").split()

	Arreglo2= input("ingresar los valores del segundo arreglo: ").split()
	if len(Arreglo1)!=len(Arreglo2):
		print("El tamaño de los dos arreglos es diferente")
		
		
for a in range(len(Arreglo2)):
	Arreglo1[a]=float(Arreglo1[a])
	Arreglo2[a]=float(Arreglo2[a])
	
for i in range(len(Arreglo1)):
	productoDirecto.append(Arreglo1[i]*Arreglo2[i])
	
print("El producto punto de los dos arreglos es:",productoDirecto)


