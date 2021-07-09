#exercise one of three
#sum of n natural numbers
# ask a user for natural number(n)
#print total from 1 to n, using while loop

total=0
a=0
numero = int(input('Ingrese el número hasta donde se van a sumar los números naturales: '))

while a!=numero:
	a+=1
	total+=a
print(f'la suma de numeros naturales hasta el {numero} es de {total}')


