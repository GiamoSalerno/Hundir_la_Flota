import numpy as np
class tablero:
    size = (10,10)
    default = np.full(size, '-')
    
    def __init__(self, size, default) -> None:
        self.size = size
        self.default = default
        pass

    def crear(self):
        """
        Función para crear tableros de juego.
        
        Returns:
            Tablero de proporciones preestablecidas.
        """
        filas = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']).reshape(-1,1)
        columnas = np.arange(11)
        tablero = np.concatenate((filas, self.default), axis=1)
        tablero = np.vstack((columnas, tablero))
        return tablero
    
    class barco:
        coord = np.random.choice(['N', 'S', 'E', 'W'])

        def __init__(self, coord) -> None:
            self.coord = coord
            pass

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