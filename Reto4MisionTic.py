n,b = input().split()
n=int(n)
b=int(b)
x=[]
conjunto=set()
repetidos=0
while len(x)!=n:
	x=input().split()
for i in range(n):
	x[i]=int(x[i])

for a in range(n):
	if x[a] in x[a+1:b+a+1]:
		repetidos+=1
		
		
		
print(repetidos,end=' ')


for i in x:
	conjunto.add(i)
print(len(x)-len(conjunto))






	
	
	


