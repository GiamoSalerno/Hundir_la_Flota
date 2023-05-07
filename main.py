
from funciones import *
from variables import *

user = input("¿Cuál es tu nombre?")
print('Bienvenido,', user)
pantalla = crear_tablero()
tabenem = crear_tablero()
tablero = crear_tablero()
flotaenemiga = [(crear_barco(1, True)),
                (crear_barco(1, True)),
                (crear_barco(3, True)),
                (crear_barco(1, True)),
                (crear_barco(4, True))]

flotausuario = [(crear_barco(2)),
                (crear_barco(3)),
                (crear_barco(2)),
                (crear_barco(1)),
                (crear_barco(2))]
print('¡Comienza el juego!')

while vidas > 0 or hundidos < 5:
    display()
    disparar()
    display()
    recibir()
if vidas == 0:
    print('Has perdido.')
elif hundidos == 5:
    print('¡Has ganado!')
