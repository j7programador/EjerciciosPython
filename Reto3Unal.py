Direcciones=input().split()
contador=1
conteo=[]
compacto=[]


for i in range(len(Direcciones)):
	if i<(len(Direcciones)-1):
		if  Direcciones[i]==Direcciones[i+1]:
			contador+=1
		else:
			compacto.append(Direcciones[i])
			conteo.append(contador)
			contador=1
	else:
		if Direcciones[i]==Direcciones[i-1]:
			contador+=1
			compacto.append(Direcciones[i])
			conteo.append(contador)
		else:
			contador=+1
			compacto.append(Direcciones[i])
			conteo.append(contador)
			
for i in range(len(compacto)):
	print(compacto[i],end=" ")
print("")
if conteo[len(conteo)-1]!=1:
	conteo[len(conteo)-1]=conteo[len(conteo)-1]-1
for i in range(len(conteo)):
	print(conteo[i],end=" ")


	
		
			
	
