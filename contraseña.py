import random
import string

def generar_contraseña(longitud):
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud de la contraseña debe estar entre 8 y 16 caracteres.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

    return contraseña

def main():
    try:
        longitud = int(input("Ingrese la longitud deseada para la contraseña (entre 8 y 16 caracteres): "))
        contraseña = generar_contraseña(longitud)
        print(f"Contraseña generada: {contraseña}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()
