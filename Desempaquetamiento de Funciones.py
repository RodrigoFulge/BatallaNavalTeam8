#Programa simple con desempaquetado de funciones

def Datos(name, surname, salute):
    Texto = f"{name}, {surname} {salute}!"
    print(Texto)

Error = True
while Error == True:
    Error = False
    try:
        nombre = input("Introduce un nombre: ")
    except:
        print("Introduce solo texto válido")
        Error = True
Error = True

while Error == True:
    Error = False
    try:
        apellido = input("Introduce un apellido: ")
    except:
        print("Introduce solo texto válido")
        Error = True
Error = True

while Error == True:
    Error = False
    try:
        saludo = input("Introduce un saludo: ")
    except:
        print("Introduce solo texto válido")
        Error = True
Error = True
Nombres = [nombre, apellido, saludo]
Datos(*Nombres)