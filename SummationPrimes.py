n=100000
primes=454396537

a=0
while n<=1999999:
	
	for i in range(2,2000):
		a=n%10
		if n>10 and (a==5 or a==6 or a==8 or a==4 or a==0 or a==2):
			break
		elif n%i==0:
			break
	else:
		primes+=n
	
	n+=1
print(primes)



