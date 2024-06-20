import random

def opciones_compu():
    elecciones = ["piedra", "papel", "tijeras"]
    eleccion = random.choice(elecciones)
    return eleccion

def determinar_ganador(eleccion_usuario, opciones_compu):
    if eleccion_usuario == opciones_compu:
        return "Empate"
    elif (eleccion_usuario == "piedra" and opciones_compu == "tijeras") or \
        (eleccion_usuario == "papel" and opciones_compu== "piedra") or \
        (eleccion_usuario == "tijeras" and opciones_compu == "papel"):
        return "¡Tú ganas!"
    else:
        return "La computadora gana"

def main():
    print("Bienvenido al juego de Piedra, Papel o Tijeras!")
    eleccion_usuario = input("Elige piedra, papel o tijeras: ").lower()

    if eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        print("Elección inválida. Por favor elige piedra, papel o tijeras.")
        return

    eleccion_computadora = opciones_compu()
    print(f"Computadora eligió: {eleccion_computadora}")

    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
    print(resultado)

if __name__ == "__main__":
    main()