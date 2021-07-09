#Define a fuction
#input
# num, iterable(tuple, list) containing numbers as args
#to power(3,*args)
# example nums=[1,2,3]

# output list [1,8,27]

#if user didn't pass any args then give a user a message 'hey yo didn't pass
#args

#else
#return list
# NOTE: USE list comprehension

num=int(input("Ingrese el exponente: "))
numeros=int(input("Ingrese hasta que numero va a calcular las potencias: "))

lista=[i for i in range(1,numeros+1)]

def to_power(num,*lista):
	if lista:
		potencias=[i**num for i in lista]
		return potencias
	else:
		return "Hey didn't pass args"

print(to_power(num,*lista))


