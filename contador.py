def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

cadena = input("Introduce una cadena de caracteres: ")

numero_vocales = contar_vocales(cadena)

print("El número de vocales en la cadena es:", numero_vocales)
