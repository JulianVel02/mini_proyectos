import random
import string

from modulos.modulo_palabras import palabras_arg
from modulos.modulo_vidas import vidas_diccionario_visual


def obtener_palabra(palabras):
    """ Se selecciona una palabra al alzar de la lista de palabras"""
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()


def bienvenida_al_juego():
    """Funcion de bienvenida al juego"""
    print("==========================================")
    print("💀 Bienvenido(a) al Juego del Ahorcado 💀")
    print("==========================================")


def ahorcado():
    """Juego del ahorcado"""
    palabra = obtener_palabra(palabras_arg)
    # conjuntos de letras por palabra # 'Python' = {'P', 'y', 't', 'h', 'o', 'n'}
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    # Abecedario por conjunto de letras
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        # Letras adivinadas
        # ' '.join({'a', 'b', 'c'}) -> 'A B C'
        print(f"Te quedan {vidas} vidas y usaste las letras: {
              ' '.join(letras_adivinadas)}")

        # Mostrar estado actual de la palabra
        palabra_lista = [
            letra if letra in letras_adivinadas else '-' for letra in palabra]

        # imprime el diagrama del ahorcado segun las vidas
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Elije una letra: ").upper()

        # Si la letra elegida por el usuario esta en el abecedario y no está en el conjunto de
        # letras que ya se ingresaron, se suma la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si la letra está en la palabra la saco de las pendientes a adivinar
            # Si no está en la palabra, resto una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\n Tu letra: {letra_usuario} no está en la palabra.")
        # Si la letra elegida por el usuario fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nYa elegiste esa letra! Por favor elige otra... 🙄")
        else:
            print("\nEsta letra NO es válida.")
    # LLego acacuando se adivinan todas las letras o cuando se terminan todas las vidas
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Perdiste, fuiste AHORCADO!! La palabra era {palabra}")
    else:
        print(f"Feliciades!! 👏👏 Adivinaste la palabra {palabra}!!")
