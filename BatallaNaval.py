import random
import math
from openai import OpenAI
#Versión 11.0 - Implementación de Funciones con IA
client = OpenAI(api_key='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')
BalanceIntentos = 1.5

class BatallaNaval:
    
    def __init__(self, NumShips, BoardSize):
        self.numeroBarcos = NumShips
        self.TamañoTablero = BoardSize
        self.BarcosPuestos = {}
        self.tablero = []

    def Tablero(self): 
        self.tablero = []
        for i in range(self.TamañoTablero + 1):
            fila = []
            if i == 0:
                for k in range(-1, self.TamañoTablero):
                    if k > 2:
                        fila.append(f"{k}")
                    elif k < 0:
                        fila.append("")
                    else:
                        fila.append(f"{k}")
            else:
                fila.append(i - 1)
                for l in range(self.TamañoTablero):
                    fila.append(" ")
            self.tablero.append(fila)
        return self.tablero

    def SetBarcos(self): 
        Reiniciar = True
        while Reiniciar == True:  
            Finds = 0
            Reiniciar = False  
            self.BarcosPuestos = {i: [random.randint(0, self.TamañoTablero - 1), random.randint(0, self.TamañoTablero - 1)] for i in range(self.numeroBarcos)}
            for CompararDuped in self.BarcosPuestos.values():
                Finds = 0
                for AnalisisDuped in self.BarcosPuestos.values():
                    if CompararDuped[0] == AnalisisDuped[0] and CompararDuped[1] == AnalisisDuped[1]:
                        Finds += 1
                        if Finds > 1:
                            Reiniciar = True 

        for coordenadas in self.BarcosPuestos.values():
            self.tablero[coordenadas[0] + 1][coordenadas[1] + 1] = "X"
        return self.BarcosPuestos
    
    def Acierto_Barco(IntentoX, IntentoY, Board): 
        Board[IntentoX][IntentoY] = "F"
        return Board


def FraseLose():
    RandomPhrase = random.randint(1,10)
    if RandomPhrase != 3:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": "¿Podrías darme una frase motivacional para luego de haber perdido una partida en un juego? Solo incluye la frase en tu respuesta"}
        ],
        max_tokens=30
        )
        print(completion.choices[0].message.content)
    else:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": "¿Podrías darme una frase burlona para luego de haber perdido una partida en un juego? Solo incluye la frase en tu respuesta"}
        ],
        max_tokens=30
        )
        print(completion.choices[0].message.content)

def FraseWin():
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": "¿Podrías darme una frase de felicitaciiones para luego de haber ganado una partida en un juego? Solo incluye la frase en tu respuesta"}
        ],
        max_tokens=30
        )
        print(completion.choices[0].message.content)

    

Aciertos = 0
Error = True
while Error == True: 
    Error = False
    try:
        BoardSize = int(input("¿De qué tamaño será el tablero?"))
    except: 
        print("Por favor introduce solo números!")
        Error = True   
Error = True  

while Error == True: 
    Error = False
    try:
        NumShips = int(input("¿Cuántos barcos habrá?"))
    except: 
        print("Por favor introduce solo números!")
        Error = True
    if Error != True:    
        if NumShips > ((BoardSize*BoardSize)):
            print("No puede haber más barcos que casillas (El cuadrado del tamaño del tablero)")
            Error= True
Error = True   
IntentosRestantes = math.ceil(NumShips + (NumShips * BalanceIntentos)) 
print(IntentosRestantes)

Juego = BatallaNaval(NumShips, BoardSize) 
Board = Juego.Tablero() 
Barcos = Juego.SetBarcos() 

for i in range(BoardSize + 1):
    print(Board[i])

while Aciertos != NumShips and IntentosRestantes != 0: 
    Golpe = False
    while Error == True:
        Error = False
        try:
            IntentoX = int(input("Ingresa la coordenada X de tu ataque: "))
        except:
            print("Por favor introduce solo números!")
            Error = True
        if IntentoX >= BoardSize:
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
        if IntentoY >= BoardSize:
            print("No puedes atacar más allá del área del tablero!")
            Error = True
    Error = True
    IntentoY += 1 
    
    for i in range(len(Barcos)):
        if Board[IntentoX][IntentoY] == "X":
            Golpe = True
        if Board[IntentoX][IntentoY] == "F":  
            if i == len(Barcos) - 1:
                print("Ya habías acertado a ese barco. No tienes por qué rematarlo")
        if Board[IntentoX][IntentoY] == "O":  
            if i == len(Barcos) - 1:
                print("Ya habías disparado allí, volver a disparar no hará hacer aparecer otro barco... ¿O sí? (No, no lo hará)")

    if Golpe == True:
        Aciertos += 1
        print("Acertaste a un barco!!")
        Board = BatallaNaval.Acierto_Barco(IntentoX, IntentoY, Board)
    else:
        IntentosRestantes -= 1
        print("No has acertado")
        Board[IntentoX][IntentoY] = "O"
        print(f"Intentos restantes: {IntentosRestantes}")

    for i in range(BoardSize + 1): 
            print(Board[i])

if Aciertos == NumShips:
    FraseWin()

if IntentosRestantes == 0:
    FraseLose()