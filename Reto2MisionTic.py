distancia,velocidad,tiempo= input().split()

distancia=int(distancia)
velocidad=int(velocidad)
tiempo=int(tiempo)

vMovimiento = (distancia/tiempo)*(3.6)

if vMovimiento<=velocidad and distancia>0 and velocidad > 0 and tiempo >0:
	print("OK")
elif vMovimiento<1.25*velocidad and distancia>0 and velocidad > 0 and tiempo >0:
	print("MULTA")
elif vMovimiento>1.25*velocidad and distancia>0 and velocidad > 0 and tiempo >0:
	print("CURSO SENSIBILIZACION")
elif distancia<0 or velocidad < 0 or tiempo<0:
	print("VALORES NEGATIVOS")

