#Exercise, number guessing game
#Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number
#if user guessed correctly then print "You Win !!!!"
# if user guessed lower than actual number then print "too low"
#if user guessed highter than actual number then print "too high"
#google "how to generate random number in python" to generate random
#winning number
import random

winning_number = random.randint(0,10)
number_guessed = input("Ingrese el número adivinado: ")
number_guessed = int(number_guessed)

if winning_number == number_guessed:
	print("You win !!!")
elif winning_number < number_guessed:
	print("too high")
else:
	print("too low")
	

