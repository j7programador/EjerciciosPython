n=int(input())
factorial=1
for i in range(1,n+1):
	factorial*=i
print(factorial)

def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return n * factorial(n-1)
print(factorial(n))
	
