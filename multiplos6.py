'''inicio=1
while inicio*6<=150:
	print(inicio*6,end=' ')
	inicio+=1
	
print("numero multiplos: ",inicio-1)'''
m=int(input("desea hallar los multiplos de: "))
n=int(input(f"ingrese hasta donde desea saber los multiplos de {m}: "))
a=''
def multiploSeis(n,m,a):
	
	if n%m==0:
		a+=str(n)+''
		return a
		
	else:
		return multiploSeis(n-1,m,a)
	


print(multiploSeis(n,m,a))

