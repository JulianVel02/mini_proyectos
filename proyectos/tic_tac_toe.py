from tkinter import *
import random


def siguiente_turno(row, column):
    """Siguiente turno del juego"""
    global jugador
    if botones[row][column]['text'] == "" and verificar_ganador() is False:

        if jugador == jugadores[0]:
            botones[row][column]['text'] = jugador

            if verificar_ganador() is False:
                jugador = jugadores[1]
                etiqueta_turno.config(text=jugadores[1] + " turn")
            elif verificar_ganador() is True:
                etiqueta_turno.config(text=jugadores[0] + " wins")
            elif verificar_ganador() == "Tie":
                etiqueta_turno.config(text="Tie!")
        else:
            botones[row][column]['text'] = jugador

            if verificar_ganador() is False:
                jugador = jugadores[0]
                etiqueta_turno.config(text=jugadores[0] + " turn")
            elif verificar_ganador() is True:
                etiqueta_turno.config(text=jugadores[1] + " wins")
            elif verificar_ganador() == "Tie":
                etiqueta_turno.config(text="Tie!")


def verificar_ganador():
    """Se verifica el ganador mediante condiciones"""
    for fila in range(3):
        if botones[fila][0]['text'] == botones[fila][1]['text'] == botones[fila][2]['text'] != "":
            botones[fila][0].config(bg="green")
            botones[fila][1].config(bg="green")
            botones[fila][2].config(bg="green")
            return True

    for columna in range(3):
        if botones[0][columna]['text'] == botones[1][columna]['text'] == botones[2][columna]['text'] != "":
            botones[0][columna].config(bg="green")
            botones[1][columna].config(bg="green")
            botones[2][columna].config(bg="green")
            return True

    if botones[0][0]['text'] == botones[1][1]['text'] == botones[2][2]['text'] != "":
        botones[0][0].config(bg="green")
        botones[1][1].config(bg="green")
        botones[2][2].config(bg="green")
        return True
    elif botones[0][2]['text'] == botones[1][1]['text'] == botones[2][0]['text'] != "":
        botones[0][2].config(bg="green")
        botones[1][1].config(bg="green")
        botones[2][0].config(bg="green")
        return True
    elif espacios_vacios() is False:
        for fila in range(3):
            for columna in range(3):
                botones[fila][columna].config(bg="yellow")
        return "Tie"
    else:
        return False


def espacios_vacios():
    """Verifica si hay espacios vacíos en el tablero"""
    # for fila in range(3):
    #     for columna in range(3):
    #         if botones[fila][columna]['text'] == "":
    #             return True
    # return False
    espacios = 9
    for fila in range(3):
        for columna in range(3):
            if botones[fila][columna]['text'] != "":
                espacios -= 1
    if espacios == 0:
        return False
    else:
        return True


def nuevo_juego():
    """Reinicia el juego"""
    global jugador
    jugador = random.choice(jugadores)
    etiqueta_turno.config(text=jugador + " turn")
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text="", bg="#f0f0f0")


ventana = Tk()
ventana.title("Tic-Tac-Toe")
jugadores = ["⭕", "❌"]
jugador = random.choice(jugadores)
botones = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

etiqueta_turno = Label(text=jugador + " turn", font=('consolas', 40))
etiqueta_turno.pack(side="top")

reseteo_boton = Button(text="Restart", font=(
    'consolas', 20), command=nuevo_juego)
reseteo_boton.pack(side="top")

frame = Frame(ventana)
frame.pack()

for fila in range(3):
    for columna in range(3):
        botones[fila][columna] = Button(frame, text="", font=('consolas', 40),
                                        width=5, height=2,
                                        command=lambda fila=fila, columna=columna: siguiente_turno(fila, columna))
        botones[fila][columna].grid(row=fila, column=columna)

ventana.mainloop()
