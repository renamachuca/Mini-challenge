def crear_diccionario(claves, valores):
    # Crear el diccionario usando la función zip() y dict()
    diccionario = dict(zip(claves, valores))
    return diccionario

entrada_claves = input("Introduce una lista de claves separadas por comas: ")
entrada_valores = input("Introduce una lista de valores separados por comas: ")

claves = entrada_claves.split(",")
valores = entrada_valores.split(",")

diccionario = crear_diccionario(claves, valores)

print("El diccionario creado es:", diccionario)
