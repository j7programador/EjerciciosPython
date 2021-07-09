numero_magico = 12345679
while True:
  numero_usuario = input("Ingrese un número entre 1 y 9: ")
  if numero_usuario<='9'and numero_usuario>'0':
  	if int(numero_usuario)<10 and int(numero_usuario)>0:
    		numero_usuario = int(numero_usuario)
    		numero_usuario*=9
    		break
print(numero_magico*numero_usuario)
