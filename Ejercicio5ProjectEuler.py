number=1
aumentador=2520
contador=1
divisor=1

while contador!=20:
	if number%divisor==0:
		divisor+=1
		contador+=1
		
		
		
	else:
		divisor=1
		aumentador+=1
		number=aumentador*10
		contador=0
		
		
	
print(number)
