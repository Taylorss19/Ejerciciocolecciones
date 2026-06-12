


def Ingresar_Datos(datos):
    while True:
        nombre= input("Ingrese su nombre: ")
        if nombre in datos:
            print("Usuario ya existe. Intente otro.")
        else:
            break
    while True:
        sexo=input("Sexo (F o M): ").upper()
        if sexo=="F" or sexo=="M":
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")
    while True:
        contraseña=input("Ingrese contraseña: ")
        if " " in contraseña or len(contraseña)<8 or contraseña.isalpha() or contraseña.isdigit():
            print("Contraseña no valida. Intente otra.")
        else:
            print("contraseña válida")
            break

    datos[nombre]=[sexo,contraseña]

    print("Ingresado correctamente")

def Buscar_Usuario(datos):
    buscar=input("Ingrese usuario a buscar: ")
    if buscar in datos:
        print(f"El sexo del usuario es: {datos[buscar][0]} y la contraseña es: {datos[buscar][1]}")
    else:
        print("El usuario no se encuentra")

def Eliminar_Usuario(datos):
    eliminar=input("Ingrese usuario a buscar: ")
    if eliminar in datos:
        datos[eliminar].clear()
        print("Usuario eliminado con éxito!")

    else: 
        print("No se pudo eliminar usuario")

datos = {}

while True:
    print(""" MENU PRINCIPAL
    1.- Ingresar usuario.
    2.- Buscar usuario.
    3.- Eliminar usuario.
    4.- Salir.
    """)
    while True:
        try:
            op=int(input("Ingrese opción: "))
            break
        except ValueError:
            print("Opción debe ser un número")     
    if op==1:
        Ingresar_Datos(datos)
    elif op==2:
        Buscar_Usuario(datos)
    elif op==3:
        Eliminar_Usuario(datos)
    elif op==4:
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opción válida!!")



#fin
