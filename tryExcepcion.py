'''Tu tarea es escribir una función capaz de ingresar valores enteros y verificar si están dentro de un rango especificado.

La función debe:

Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará al usuario que ingrese el valor nuevamente.
Si el valor de entrada es válido, será regresado como resultado.'''

def readint(prompt, min, max):
    
    try:
            v=int(input(prompt))
            if v<min or v>max:
                print('Error: el valor no está dentro del rango permitido (-10..10)')
            else:
                print("El numero es:", v)
    except ValueError:
            print('Error: entrada incorrecta')
       
    
# tu codigo aqui
#

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)
