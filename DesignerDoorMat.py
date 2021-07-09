filas, columnas = input().split()
filas=int(filas)
columnas= int(columnas)


a='.|.'
for i in range(1,filas,2):
	x=(a*i).center(columnas,"-")
	print(x)
letrero= "WELCOME".center(columnas,"-")
print(letrero)

for i in reversed(range(1,filas,2)):
	x=(a*i).center(columnas,"-")
	print(x)










