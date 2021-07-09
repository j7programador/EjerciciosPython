'''dinero ganado despues de un mes, si el mes paga 15% de interes por año?'''

n=input('Ingrese el dinero invertido ')
n=float(n)

interespormes= 0.15/12

dineroganado = interespormes*n
print(f"el dinero ganado por mes es de: {round(dineroganado,2)}")
print(f"el dinero ganado por año es de: {n*0.15}")



