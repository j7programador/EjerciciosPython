#define a function which takes two numbers as a input and
# return greater of two numbers
a,b=input("ingrese los dos números que vamos a comparar, separados de un espacio: ").split(" ")
a=int(a)
b=int(b)
def mas_grande(a,b):
	if a>b:
		return a
	else:
		return b
print("el número más grande es: ",mas_grande(a,b))
