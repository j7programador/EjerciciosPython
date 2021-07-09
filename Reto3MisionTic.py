n=int(input())
a=[]
band=False
for i in range(n):
	x=input().split()
	for i in range(len(x)):
		x[i]=int(x[i])
	a.append(x)

for c in a:
	if (c[0]>=10 and c[0]<=12) and c[1]<=18 and c[2]>=15 and c[3]<=92:
		print(c[4])
		band=True
		
if band==False:
	print("NO DISPONIBLE")

	
		
		

	

	
