#diccioanrio="{}" , clave=":" y listas="[]"
'''usuarios = {
    "juan":{"M","asdsad123123"},
    "maria":{"F","asdsad123123"}
}
#diccionario con claves: y listas
usuarios2= {
    "daniel":{
        "sexo":"M",
        "pass":"123asdf"
    },
    "Jorge":{
        "sexo":"M",
        "pass":"4567asdf"
    }
}'''
#diccionario dentro de otro disccionario con claves 


def ingresar_usuario():
    while True:
        nombre=input("Ingrese nombre de usuario: ")
        if nombre in usuarios:
            print("Usuario ya existe, intente con otro nombre")
        else:
            break
    while True:
        sexo=input("Ingrese sexo(M,F): ").upper()
        if sexo =="M" or sexo == "F":
            break
        else:
            print("el sexo debe ser Mo F, ingrese nuevamente!")
    while True:
        contraseña=input("Ingrese contraseña: ")
        if validar_contraseña(contraseña):
            break
        else:
            print("contraseña inválida, debe tener 8 caracteres entre letras y números")

    print("usuario ingresado correctamente")
    
    usuarios[nombre]={
        "sexo":sexo,
        "pass":contraseña
    }

def validar_contraseña(contraseña):
    if len(contraseña)<8 or " " in contraseña or contraseña.isdigit() or contraseña.isalpha():
        return


def buscar_usuario():
    nombre=input("Ingrese nombre a buscar: ")
    if nombre in usuarios:
        print(f"Sexo: ",usuarios[nombre]["sexo"])
        print("Contraseña: ",usuarios[nombre]["contraseña"])
    else:
        print("Nombre no encontrado")

def eliminar_usuario():
    nombre=input("Ingrese nombre a buscar: ")
    del nombre in usuarios:
        print("Usuario eliminado correctamente")
    else:
        print("Nombre no encontrado")

    

usuarios = {}


while True:
    print("--- Menu Principal ---")
    print("1. Ingresar Usuario")
    print("2. Buscar Usuario")
    print("3. Eliminar Usuario")
    print("4. Salir")
    while True:
        try:
            op=int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Por favor ingrese una opción válida")
    if op==1:
        ingresar_usuario()
    elif op ==2:
        buscar_usuario()
    elif op==3:
        eliminar_usuario()
    elif op==4:
        print("Saliendo...")
        break
    else:
        print("Por favor ingrese un valor entre 1 y 4")