def convertir(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("ingrese el dato de celsius a convertir"))

fahrenheit = convertir(celsius)
print(f"{celsius} grados celsius son {fahrenheit} grados fahrenheit")