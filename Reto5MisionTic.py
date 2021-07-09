Nombres=['Manzanas', 'Limones','Peras', 'Arandanos','Tomates','Fresas','Helado','Galletas','Chocolates','Jamon']
Precios=[5000,2300,2700,9300,2100,4100,4500,500,3500,15000]
Inventario=[25,15,33,5,42,3,41,8,80,10]
for i in range(len(Precios)):
	Precios[i]=float(Precios[i])



def borrar():
	global a
	a=''
	borrado=input().split()
	borrado[0]=int(borrado[0])
	borrado[2]=float(borrado[2])
	borrado[3]=int(borrado[3])
	try:

		Nombres.remove(borrado[1])
		Precios.remove(borrado[2])
		Inventario.remove(borrado[3])
	except:
		a='ERROR'
def actualizar():
	global a
	a=''
	actualizado=input().split()
	actualizado[2]=float(actualizado[2])
	actualizado[0]=int(actualizado[0])-1
	if actualizado[1] not in Nombres:
		a='ERROR'
	try:
		Precios[actualizado[0]]=actualizado[2]
		actualizado[3]=int(actualizado[3])
		Inventario[actualizado[0]]=actualizado[3]
	except:
		a='ERROR'
def agregar():
	global a
	a=''
	agregado=input().split()
	agregado[0]=int(agregado[0])-1
	agregado[2]=float(agregado[2])
	agregado[3]=int(agregado[3])
	if agregado[1] in Nombres:
		a='ERROR'
	try:
		Nombres.insert(agregado[0],agregado[1])
		Precios.insert(agregado[0],agregado[2])
		Inventario.insert(agregado[0],agregado[3])
	except:
		a='ERROR'
	

Accion=''
while Accion!='BORRAR' and Accion!='AGREGAR' and Accion!='ACTUALIZAR':
	Accion=input()
	if Accion=='BORRAR':
		borrar()
	elif Accion=='ACTUALIZAR':
		actualizar()
	elif Accion=='AGREGAR':
		agregar()

if a=='ERROR':
	print('ERROR')
else:
	Mayor=Precios[0]
	Menor=Precios[0]
	NombreMayor=''
	NombreMenor=''
	for i in range(1,len(Nombres)):
		if Precios[i] > Mayor:
			Mayor=Precios[i]
			NombreMayor=Nombres[i]
		
		if Precios[i]< Menor:
			Menor=Precios[i]
			NombreMenor=Nombres[i]
	Total=0
	for i in range(len(Inventario)):
		Total+=Inventario[i]*Precios[i]

	print(NombreMayor,NombreMenor,round(sum(Precios)/len(Precios),1),Total)





	




