def tabla_de_multiplicar(numero):
    for num in range(1,11):
        producto = numero * num
        print(f"{numero} x {num} = {producto}")

numero = int(input("Ingrese el numero del cual quieras saber su tabla de multiplicar")) 



tabla_de_multiplicar(numero)
