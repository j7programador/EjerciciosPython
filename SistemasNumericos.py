number=int(input())
espacios=len(f'{number:b}')
def print_formatted(number):
	for i in range(1,number+1):					  	 																			 			print(f'{i}'.rjust(espacios),f'{i:o}'.rjust(espacios),f'{i:x}'.upper().rjust(espacios),\
			f'{i:b}'.rjust(espacios))
print_formatted(number)
