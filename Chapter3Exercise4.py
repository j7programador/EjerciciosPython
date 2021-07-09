#problem
#ask user ti input a number containing more than one digit
#example 1256
#calculate 1+2+5+6 and print

number= input("ingrese un número de mas de un digito: ")
total=0
for i in range(len(number)):
	total+=int(number[i])
print(f'la suma de los digitos es de {total}')

