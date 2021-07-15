'''Crea un programa llamado ex_3_3, que calcule el equivalente humano de la edad de un perro.
Los dos primeros años de vida de un perro equivalen cada uno a diez y medio años humanos, y
los siguientes años de vida de un perro equivalen cada uno a cuatro años humanos.'''

edadPerro=int(input('ingrese la edad del perro: '))

if edadPerro<3:
	edadHumano=edadPerro*10.5
else:
	edadHumano=2*10.5+(edadPerro-2)*4

print("La edad del perro en edad de humano es:",edadHumano)


