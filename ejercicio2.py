'''sueldo base, y tiene 10% comision de ventas, salidas: dinero por comisiones por tres ventas en el mes'''

n=float(input("ingrese el sueldo base: "))
a=0
b=0
for i in range(3):
	a=float(input(f"ingrese el valor de la venta {i+1}: "))
	b+=a
TotalGanado= n + b*0.10

print(f"el total ganado en el mes es de {TotalGanado}")


