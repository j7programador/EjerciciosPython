#Define is_palindrome function thatr take one word in string as input 
#and return True if it is palindrome else return False

a=input("ingrese la palabra para saber si es palindroma: ")

def is_palindrome(a):
	if a==a[::-1]:
		return True
	else:
		return False
print(is_palindrome(a))


