Numeros= int(input("Ingrese el número: ")) 
def Factorial(n):
	if n==0:
		return 1
	else:
		for a in range(1,n):
			n*=a #n=n*a
		return n
for i in range(Numeros+1):
	print(f"{i}! = {Factorial(i)}")
