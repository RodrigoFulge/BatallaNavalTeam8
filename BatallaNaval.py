import random, math
#Versión 8.0 - Agregada funcionalidad para indicar posiciones que ya recibieron un disparo
BalanceIntentos = 1.5 

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

    def SetBarcos(self): #Se usa la comprensión de diccionarios aquí para generar el diccionario en una forma más comprimida con menos variables
        Reiniciar = True
        while Reiniciar == True:  
            Finds = 0
            Reiniciar = False  
            self.BarcosPuestos = {i: [random.randint(0, self.TamañoTablero - 1), random.randint(0, self.TamañoTablero - 1)] for i in range(self.numeroBarcos)}
            #print(self.BarcosPuestos)
            for CompararDuped in self.BarcosPuestos.values():
                Finds = 0
                for AnalisisDuped in self.BarcosPuestos.values():
                    #print(f"CompararDuped: {CompararDuped[0]}")
                    #print(f"CompararDuped: {CompararDuped[1]}")
                    #print(f"AnalisisDuped: {AnalisisDuped[0]}")
                    #print(f"AnalisisDuped: {AnalisisDuped[1]}")
                    if CompararDuped[0] == AnalisisDuped[0] and CompararDuped[1] == AnalisisDuped[1]:
                        Finds += 1
                        #print(f"finds: {Finds}")
                        if Finds > 1:
                            #print("Se encontraron duplicados, volver a generar!")
                            Reiniciar = True #Vuelve a generar una lista de coordenadas si encuentra al menos un duplicado
                            #print(Reiniciar)

        for coordenadas in self.BarcosPuestos.values(): #Aquí values sirve para poder iterar todos los valores del diccionario
            self.tablero[coordenadas[0] + 1][coordenadas[1] + 1] = "X"
        #print(self.BarcosPuestos)
        return self.BarcosPuestos
    
    def Acierto_Barco(IntentoX,IntentoY,Board): #Esta función se activará cuando el jugador acierte a un barco
        Board[IntentoX][IntentoY] = "F"
        return Board



Aciertos = 0
Error = True
while Error == True: #Compreba que el usuario solo introduzca números.
    Error = False
    try:
        BoardSize = int(input("¿De que tamaño será el tablero?"))
    except: #Si introduce algo más, recibe una excepción osea un error, y manda Error como True para repetir el código.
        print("Por favor introduce solo números!")
        Error = True   
Error = True #Vuelve a establecer Error como True para próximas comprobaciones  

while Error == True: #Compreba que el usuario solo introduzca números.
    Error = False
    try:
        NumShips = int(input("¿Cuántos barcos habrá?"))
    except: #Si introduce algo más, recibe una excepción osea un error, y manda Error como True para repetir el código.
        print("Por favor introduce solo números!")
        Error = True
    if Error != True:    
        if NumShips > ((BoardSize*BoardSize)):
            print("No puede haber más barcos que casillas (El cuadrado del tamaño del tablero)")
            Error= True
Error = True  #Vuelve a establecer Error como True para próximas comprobaciones  
IntentosRestantes = math.ceil(NumShips+(NumShips*BalanceIntentos)) #Define la cantidad de intentos. Será el número de barcos por 1.5. Aun así, se puede modificar libremente con la variable al inicio
print(IntentosRestantes)
Juego = BatallaNaval(NumShips,BoardSize) #Inicializa el juego
Board = BatallaNaval.Tablero(Juego) #Inicia el tablero. 
Barcos = BatallaNaval.SetBarcos(Juego) #Diccionario de las coordenadas. 
for i in range(BoardSize+1):
    print(Board[i])
print(Barcos) #Imprime el diccionario retornado por Tablero    
while Aciertos != NumShips and IntentosRestantes != 0: #Mientras el número de aciertos sea menor al número de barcos, el juego seguirá
    Golpe = False
    while Error == True:
        Error = False
        try:
            IntentoX = int(input("Ingresa la coordenada X de tu ataque: "))
        except:
            print("Por favor introduce solo números!")
            Error = True
        if IntentoX >= BoardSize: #Comprobación para no poder introducir numeros fuera de área
            print("No puedes atacar más allá del área del tablero!")
            Error = True
    Error = True
    IntentoX += 1
    while Error == True:
        Error = False
        try:
            IntentoY = int(input("Ingresa la coordenada Y de tu ataque: "))
        except:
            print("Por favor introduce solo números!")
            Error = True
        if IntentoY >= BoardSize: #Comprobación para no poder introducir numeros fuera de área
            print("No puedes atacar más allá del área del tablero!")
            Error = True
    Error = True
    IntentoY += 1 #En las dos variables de intentos se les suma 1 para que no tome en cuenta los bordes
    
    for i in range(len(Barcos)): #Repetirá el ciclo según la cantidad de coordenadas de barcos disponibles
        indice = Barcos[i]
        #print(Board)
        if Board[IntentoX][IntentoY] == "X": #Si hay un barco, setea Golpe a True para que ejecute la función de acierto más abajo
            Golpe = True
        if Board[IntentoX][IntentoY] == "F":  #Impide ganar otro punto si ya se había acertado a un barco en esa coordenada
            print("Ya habías acertado a ese barco. No tienes por que rematarlo")
        if Board[IntentoX][IntentoY] == "O":  #Impide volver a disparar a una zona ya atacada
            print("Ya habías disparado allí, volver a disparar no hará hacer aparecer otro barco... ¿O sí? (No, no lo hará)")


    if Golpe == True:
        Aciertos += 1
        print("Acertaste a un barco!!")
        Board=BatallaNaval.Acierto_Barco(IntentoX,IntentoY,Board) #Actualiza el tablero mediante la función
    else:
        IntentosRestantes -= 1
        print("No has acertado")
        Board[IntentoX][IntentoY] = "O"
        print(f"Intentos restantes: {IntentosRestantes}")

    for i in range(BoardSize+1): #Imprime el tablero actualizado
            print(Board[i])
if Aciertos == NumShips:
    print("Ganaste!! Derribaste todos esos barcos. Eres todo un criminal de guerra!! Tomar todas esas vidas debe hacerte sentir imponente!!")

if IntentosRestantes == 0:
    print("No derribaste todos los barcos. Tus soldados han sacrificado sus vidas y aun así no has logrado defender su patria. Sus muertes han sido en vano, y tus tierras han sido tomadas. Felicidades")
input("Presiona cualquier tecla para Salir")
    

