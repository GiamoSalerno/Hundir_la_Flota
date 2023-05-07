
import numpy as np

user = input("Introduce tu  nombre")

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

tablero = crear_tablero()
tabenem = crear_tablero()
pantalla = crear_tablero()

def crear_barco(eslora:int, enemy = False):
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
        if enemy == True:
            tabenem[casilla] = 'O'
        else:
            tablero[casilla] = 'O'
    return barco

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

disparos = []
hundidos = 0
abc = {'A' : 1,
       'B' : 2,
       'C' : 3,
       'D' : 4,
       'E' : 5,
       'F' : 6,
       'G' : 7,
       'H' : 8,
       'I' : 9,
       'J' : 10}

def disparar(abc = abc):
    """
    Función para disparar a la flota enemiga, las coordenadas son establecidas por el usuario mediante un input.

    Returns:
        Tablero actualizado tras el ataque.
    """
    abc = abc
    fila = input('¿Qué fila?').upper()
    if fila == 'CHEAT':
        print(tabenem)
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

vidas = 10

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

now = f'Barcos enemigos hundidos: {hundidos}. Vidas: {vidas}.'

def display():
    """
    Función que sirve como interfaz, mostrando al usuario información útil como mapas, vidas y progreso.
    """
    print(pantalla)
    print('—'*50)
    print(tablero)
    print(f'{user} ; {now}')

print('Bienvenido,', user)
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
