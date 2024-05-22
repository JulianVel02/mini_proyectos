"""

░█████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗░█████╗░
██╔══██╗██╔══██╗██║██║░░░██║██║████╗░██║██╔══██╗
███████║██║░░██║██║╚██╗░██╔╝██║██╔██╗██║███████║
██╔══██║██║░░██║██║░╚████╔╝░██║██║╚████║██╔══██║
██║░░██║██████╔╝██║░░╚██╔╝░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝

░█████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗░█████╗░██████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██║██║░░░██║██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║██║░░██║██║╚██╗░██╔╝██║██╔██╗██║███████║██║░░██║██║░░██║██████╔╝
██╔══██║██║░░██║██║░╚████╔╝░██║██║╚████║██╔══██║██║░░██║██║░░██║██╔══██╗
██║░░██║██████╔╝██║░░╚██╔╝░░██║██║░╚███║██║░░██║██████╔╝╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝
"""
import random


def bienvenida_al_juego():
    """Funcion de bienvenida al juego"""
    print("=======================")
    print("Bienvenido(a) al Juego!")
    print("=======================")
    print("\nEl objetivo del juego es adivinar el número generado por la computadora.\nBuena suerte! (⌐■_■) \n")


def adivina_el_numero(limite):
    """
    * Randint es:
    * Un random integer: numero entero aleatorio
    * Genera un numero aleatorio entre 1 y limite_superior (los dos parametros de la funcion)
    """

    numero_aleatorio = random.randint(1, limite)
    prediccion = 0
    cont = 0
    while prediccion != numero_aleatorio:
        # El usuario va a ingresar un numero
        prediccion = int(
            input(f"Ingrese un número entre 1 y {limite} a adivinar: "))
        if prediccion < numero_aleatorio:
            print("Intenta otra vez. El número ingresado es menor! 🤔 \n")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. El número ingresado es mayor! 😥 \n")
        cont += 1
    if cont >= 10:
        print(f"Felicidades!! Adivinaste el número {
            numero_aleatorio} correctamente, aunque te costó un poco... 😅 \n")
    else:
        print(f"Felicidades!! Adivinaste el número {
            numero_aleatorio} correctamente. 😎 \n")


def turno_computadora():
    print("=============================================")
    print("Ahora le me toca a mi adivinar tú número! 🤖")
    print("=============================================")
    print("\n")


def bienvenida_al_juego_computadora(x):
    """Funcion de bienvenida al turno de la computadora"""
    print(f"Selecciona un número entre 1 y {
          x}. Veremos si la computadora puede adivinarlo. ☝️🤓")


def adivina_numero_computadora(x):
    """Funcion para que la computadora adivine mi numero"""
    lim_inf = 1
    lim_sup = x
    respuesta = ""
    while respuesta != "c":
        # Genero una prediccion
        if lim_inf != lim_sup:
            prediccion = random.randint(lim_inf, lim_sup)
        else:
            prediccion = lim_inf  # puede ser el suoerior
        # Obtengo la respuesta
        respuesta = input(f"Mi predicción es: {
                          prediccion}. Dime si mi espuesta es: Alta (A) - Baja (B) - Correcta (C): ").lower()
        if respuesta == "a":
            lim_sup = prediccion - 1
        elif respuesta == "b":
            lim_inf = prediccion + 1
    print(f"La computadora adivinó tu número correctamente: {prediccion}!! 😎")
