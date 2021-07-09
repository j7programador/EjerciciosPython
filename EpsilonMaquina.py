n=0
def Epsilon(n):
	if (1+2**-n)==(1+2**(-n-1)):
		return 2**-n
	else:
		return Epsilon(n+1)


print(Epsilon(n))

def EpsilonConCiclo(n):

	while (1+2**-n)!=1+2**(-n-1):
		n+=1
	return(2**-n)

print(EpsilonConCiclo(n))




		
