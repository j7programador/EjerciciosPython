'''un alumno desea saber cual es su calificacion final, 40% de sus tres calificaciones parciales, 50% del examen final
y 10% de la calificación de un trabajo final; salida: CalificacionFinal'''

parcial1= float(input("ingrese la nota del parcial 1: "))
parcial2= float(input("ingrese la nota del parcial 2: "))
parcial3= float(input("ingrese la nota del parcial 3: "))
examenFinal= float(input("ingrese la nota del examen final: "))
trabajoFinal = float(input("ingrese la nota del trabajo final: "))

CalificacionFinal= ((parcial1+parcial2+parcial3)/3)*0.40+examenFinal*0.5+trabajoFinal*0.10

print(f"La calificación final es de {CalificacionFinal}")


