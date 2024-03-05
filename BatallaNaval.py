import random
#Versión 1.0 - Creación del código que arma el tablero y pone los barcos

class BatallaNaval:
    
    def __init__(self,numeroBarcos,TamañoTablero):
        self.numeroBarcos = 5 
        self.TamañoTablero = 5
        self.BarcosPuestos = {}

    def Tablero(self): #Esta función definirá el tamaño del dablero Y los barcos puestos
        tablero = []
        for i in range (self.TamañoTablero): #Creando el tablero, considerando el espacio del inicio y las filas con números
            fila = []
            if i == 0:
                for k in range(-1,self.TamañoTablero-1):
                    if k > 2:
                        fila.append(f"{k}")
                    elif k < 0:
                        fila.append("")
                    else:
                        fila.append(f"{k}")

            else:
                fila.append(i-1)
                for l in range(self.TamañoTablero-1):
                    fila.append(" ")
            tablero.append(fila)


        for i in range(self.numeroBarcos): #Poner los barcos en el tablero YA creado
            CoordX = random.randint(1,self.TamañoTablero-1)
            CoordY = random.randint(1,self.TamañoTablero-1)
            self.BarcosPuestos[i] =  [CoordX-1,CoordY-1] #Pone las coordenadas de los barcos en un diccionario
            tablero[CoordX][CoordY] = "X" #Pone los Barcos como una X


        for i in range(self.TamañoTablero):
            print(tablero[i])

        return(self.BarcosPuestos) #Retorna el diccionario con las coordenadas
    
Juego = BatallaNaval(4,4)
Barcos = BatallaNaval.Tablero(Juego)
print(Barcos) #Imprime el diccionario retornado por Tablero