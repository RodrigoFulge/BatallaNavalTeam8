import random
#Versión 2.0 - Agregada función de ataque y acierto a barcos. Aun falta refinar para que no haya errores con que se generen dos barcos en la misma coordenada
    #Además, se han separado la creacion de tablero y creación de barcos en dos funciones diferentes
Aciertos = 0
class BatallaNaval:
    
    def __init__(self,NumShips,BoardSize):
        self.numeroBarcos = NumShips
        self.TamañoTablero = BoardSize
        self.BarcosPuestos = {}
        self.tablero = []

    def Tablero(self): #Esta función definirá el tamaño del dablero Y los barcos puestos
        self.tablero = []
        for i in range (self.TamañoTablero+1): #Creando el tablero, considerando el espacio del inicio y las filas con números
            fila = []
            if i == 0:
                for k in range(-1,self.TamañoTablero):
                    if k > 2:
                        fila.append(f"{k}")
                    elif k < 0:
                        fila.append("")
                    else:
                        fila.append(f"{k}")

            else:
                fila.append(i-1)
                for l in range(self.TamañoTablero):
                    fila.append(" ")
            self.tablero.append(fila)
        return self.tablero

    def SetBarcos(self):
        for i in range(self.numeroBarcos): #Poner los barcos en el tablero YA creado
            CoordX = random.randint(1,self.TamañoTablero)
            CoordY = random.randint(1,self.TamañoTablero)
            self.BarcosPuestos[i] =  [CoordX-1,CoordY-1] #Pone las coordenadas de los barcos en un diccionario. Se resta uno para no considerar los bordes como coordenadas
            self.tablero[CoordX][CoordY] = "X" #Pone los Barcos como una X
        return(self.BarcosPuestos) #Retorna el diccionario con las coordenadas
    
#Errores
        #No hay comprobación en caso de que dos barcos caigan en la misma posición. Hacer algo en una futura versión
    
    def Acierto_Barco(IntentoX,IntentoY,Board): #Esta función se activará cuando el jugador acierte a un barco
        Board[IntentoX][IntentoY] = "F"
        return Board

    def Fallo(self):
        pass

NumShips = int(input("¿Cuántos barcos habrá?"))
BoardSize = int(input("¿De que tamaño será el tablero?"))
Juego = BatallaNaval(NumShips,BoardSize) #Inicializa el juego
Board = BatallaNaval.Tablero(Juego) #Inicia el tablero. 
Barcos = BatallaNaval.SetBarcos(Juego) #Diccionario de las coordenadas. 
for i in range(BoardSize+1):
    print(Board[i])
print(Barcos) #Imprime el diccionario retornado por Tablero    
while Aciertos != NumShips: #Mientras el número de aciertos sea menor al número de barcos, el juego seguirá
    Golpe = False
    IntentoX = int(input("Ingresa la coordenada X de tu ataque: "))
    IntentoX += 1
    IntentoY = int(input("Ingresa la coordenada Y de tu ataque: "))
    IntentoY += 1 #En las dos variables de intentos se les suma 1 para que no tome en cuenta los bordes
    for i in range(len(Barcos)): #Repetirá el ciclo según la cantidad de coordenadas de barcos disponibles
        indice = Barcos[i]
        print(indice)
        if Board[IntentoX][IntentoY] == "X": #Si hay un barco, setea Golpe a True para que ejecute la función de acierto más abajo
            Golpe = True
            print("Acertaste a un barco!!")
        else:
            print("No has acertado")
        if Board[IntentoX][IntentoY] == "F":  #Impide ganar otro punto si ya se había acertado a un barco en esa coordenada
            print("Ya habías acertado a ese barco. No tienes por que rematarlo")

    if Golpe == True:
        Aciertos += 1
        Board=BatallaNaval.Acierto_Barco(IntentoX,IntentoY,Board) #Actualiza el tablero mediante la función

    for i in range(BoardSize+1): #Imprime el tablero actualizado
            print(Board[i])

    


