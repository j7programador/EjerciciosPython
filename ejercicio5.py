'''determinar el dinero que recibirá un trabajador por horas extras
, sabiendo que cuando las horas de trabajo exceden de 40 el resto es horas extras y que se pagan
al doble de una hora normal cuando no excedan de 8, el resto se pagan al triple'''

nroHorasTrabajadas=int(input("ingrese las horas trabajadas: "))
valorHora = float(input("ingrese el valor de la hora: "))

HorasExtrasDobles= nroHorasTrabajadas-40
HorasExtrasTriples= nroHorasTrabajadas-48



if nroHorasTrabajadas>48:
	TotalExtrasTriples= valorHora*3*HorasExtrasTriples
	ToltalExtrasDobles = valorHora*2*8
	print(TotalExtrasTriples+TotalExtrasDobles)
	
elif nroHorasTrabajadas>40 and nroHorasTrabajadas<48:

	ToltalExtrasDobles = valorHora*2*HorasExtrasDobles
	print(TotalExtrasDobles)
else:
	TotalGanado= nroHorasTrabajadas*valorHora
	print(TotalGanado)
	

	

	





