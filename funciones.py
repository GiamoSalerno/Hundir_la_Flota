import numpy as np
from variables import *

def crear_barco(eslora:int, tablero):
    """
    Función para crear y colocar barcos.
    
    Args:
        eslora (int): Longitud del barco.
        enemy (bool): Indica si es un barco aliado (por defecto) o enemigo.
    
    Returns:
        Tablero con los barcos en posición.
    """
    barco = []
    coord = np.random.choice(['N', 'S', 'E', 'W'])
    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    barco.append((x, y))

    while len(barco) < eslora:
        if   coord == 'N':
            x += 1
        elif coord == 'S':
            x -= 1
        elif coord == 'E':
            y -= 1
        elif coord == 'W':
            y += 1
        if (0 < x < 11 and 0 < y < 11) and tablero[x, y] == ' ':
            barco.append((x, y))
        else:
            x = np.random.randint(1, 10)
            y = np.random.randint(1, 10)
            barco = []
    for casilla in barco:
            tablero[casilla] = 'O'
    return barco

def crear_tablero():
    """
    Función para crear tableros de juego.
    
    Returns:
        Tablero de proporciones preestablecidas.
    """
    mar = np.full((10,10), ' ')
    filas = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']).reshape(-1,1)
    columnas = np.arange(11)
    tablero = np.concatenate((filas, mar), axis=1)
    tablero = np.vstack((columnas, tablero))
    return tablero

def disparar(abc, tabenem, pantalla):
    """
    Función para disparar a la flota enemiga, las coordenadas son establecidas por el usuario mediante un input.

    Returns:
        Tablero actualizado tras el ataque.
    """
    abc = variables.abc
    fila = input('¿Qué fila?').upper()
    x = abc[fila]
    y = int(input(('Fila', fila,', ¿Qué columna?')))
    if fila not in abc or y not in range(11):
        print("Coordenadas inválidas, por favor, intenta de nuevo.")
    blanco = (x, y)
    disparos.append(blanco)
    if tabenem[blanco] == 'O':
        pantalla[blanco] = 'X'
        print(f'{fila, y} ha dado en el blanco.')
        print(pantalla)
        for barco in flotaenemiga:
            for i, casilla in enumerate(barco):
                if casilla == disparos[-1]:
                    barco[i] = None
        estado()
        disparar()
    elif tabenem[blanco] == ' ':
        pantalla[blanco] = '#'
        print(f'{fila, y} ha fallado.')
    elif blanco in disparos:
        print('¡Ya has disparado a esa casilla!')
        disparar()
    return tablero

def display():
    """
    Función que sirve como interfaz, mostrando al usuario información útil como mapas, vidas y progreso.
    """
    print(pantalla)
    print('—'*50)
    print(tablero)
    print(f'{user} ; {now}')

def estado():
    """
    Función para llevar registro de hundimientos en la partida.
    """
    for i, barco in enumerate(flotaenemiga):
        if all(casilla is None for casilla in barco):
            print('¡Has hundido un barco!')
            flotaenemiga.pop(i)
            global hundidos
            hundidos += 1

def recibir():
    """
    Función que genera una coordenada aleatoria que servirá como el ataque enemigo.

    Returns:
        Tablero actualizado tras el ataque.
    """
    blanco = ((np.random.randint(0,10)), (np.random.randint(0,10)))
    if tablero[blanco] == 'O':
        tablero[blanco] = 'X'
        print(f'Has sido atacado en {blanco}.')
        global vidas
        vidas -= 1
        print(tablero)
        recibir()
    elif tablero[blanco] == ' ':
        tablero[blanco] = '#'
        print(f'Has sido atacado en {blanco}.')
    else:
        recibir()
    return tablero
