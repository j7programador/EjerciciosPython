name, character = input("ingrese su nombre y el caracter que quiere contar, separados de una coma: ").split(",")
#name.strip() #soluciona el problema de los espacios, eliminando los espacios a la derecha y a izquierda
#si solo quiero eliminar los espacios de la izquierda es lstrip()
#si solo quiero eliminar los espacios de la derecha es rstrip()



print("esta es la longitud del nombre: ",len(name))
print(f"tiene {character} {name.lower().count(character.lower.strip())} veces ")#con el lower() cuenta la letra sin importar si es mayuscula o minuscula.
