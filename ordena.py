def ordenar_lista(lista):
    lista.sort()
    return lista

entrada = input("Introduce una lista de números separados por comas: ")

lista_numeros = [int(x) for x in entrada.split(",")]

lista_ordenada = ordenar_lista(lista_numeros)

print("La lista ordenada en orden ascendente es:", lista_ordenada)
