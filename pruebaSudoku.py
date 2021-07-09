'''Como probablemente sabes, Sudoku es un rompecabezas de colocación de números jugado en un tablero de 9x9. El jugador tiene que llenar el tablero de una manera muy específica:

Cada fila del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
Cada columna del tablero debe contener todos los dígitos del 0 al 9 (nuevamente, el orden no importa).
Cada subcuadro de 3x3 de la tabla debe contener todos los dígitos del 0 al 9.
Si necesitas más detalles, puedes encontrarlos aquí.

Tu tarea es escribir un programa que:

Lea las 9 filas del Sudoku, cada una con 9 dígitos (verifica cuidadosamente si los datos ingresados son válidos).Da como salida Si si el Sudoku es válido y No de lo contrario.
Prueba tu código utilizando los datos que te proporcionamos.
Datos de Prueba
Entrada de Muestra:

295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
Salida de Muestra:
Yes

Entrada de Muestra:

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

Salida de la Muestra

No
'''
Lista=[]
listaVerticales=[]
listaCuadrados=[]
ListadeConteo=[]
for i in range(9):
	sudoku=input()
	Lista.append(sudoku)
for i in Lista:
	for a in range(1,10):
		ListadeConteo.append(i.count(str(a)))
	for b in range(9):
		for c in range(9):
			listaVerticales.append(Lista[b][c])
		for d in listaVerticales:
			ListadeConteo.append(listaVerticales.count(d))
		listaVerticales=[]

for e in range(9):
	for f in range(3):
		listaCuadrados.append(int(Lista[e][f]))
for k in range(1,10):
	ListadeConteo.append(listaCuadrados[0:9].count(k))
	ListadeConteo.append(listaCuadrados[9:18].count(k))
	ListadeConteo.append(listaCuadrados[18:27].count(k))
listaCuadrados=[]

for g in range(9):
	for h in range(3,6):
		listaCuadrados.append(int(Lista[g][h]))
for x in range(1,10):
	ListadeConteo.append(listaCuadrados[0:9].count(x))
	ListadeConteo.append(listaCuadrados[9:18].count(x))
	ListadeConteo.append(listaCuadrados[18:27].count(x))
#print(listaCuadrados)

listaCuadrados=[]

for j in range(9):
	for l in range(6,9):
		listaCuadrados.append(int(Lista[j][l]))
for y in range(1,10):
	ListadeConteo.append(listaCuadrados[0:9].count(y))
	ListadeConteo.append(listaCuadrados[9:18].count(y))
	ListadeConteo.append(listaCuadrados[18:27].count(y))
#print(listaCuadrados)
listaCuadrados=[]
print(ListadeConteo)



if 2 in ListadeConteo:
	a="No"
else:
	a="Yes"
print(a)







		
	
		
		
		
		
		
			





