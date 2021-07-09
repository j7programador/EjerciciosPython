#MODIFY NUMBER GUESSING GAME
import random

winning_number = random.randint(1,100)
number=0
veces=1

while winning_number!=number:
	
	number= int(input("ingrese el numero: "))
	

	if winning_number<number:
		print("El numero ingresado es demasiado alto")
	elif number<winning_number: 
		print("el numero ingresado es demasiado bajo")
	veces+=1
	
print(f"ha adivinado el número, realizó {veces} intentos")
