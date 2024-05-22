import random


def bienvenida_al_juego():
    """Funcion de bienvenida al juego"""
    print("==========================================================")
    print("Bienvenido(a) al Juego de Piedra🪨 - Papel📃 - Tijeras✂️")
    print("==========================================================")


def jugar():
    usuario = input(
        "Elije una opción: \n-Piedra (pi)\n-Papel (pa)\n-Tijeras (ti)\nElijo: ").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return 'Empate!! 😮'
    if gano_jugador(usuario, computadora):
        return 'Ganaste!! 😎'
    return 'Perdiste!! 😭'


def gano_jugador(jugador, oponente):
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
            or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
