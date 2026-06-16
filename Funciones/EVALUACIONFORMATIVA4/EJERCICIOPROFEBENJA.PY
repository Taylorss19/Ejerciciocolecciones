inventario=[]
def menu():
    print("""========== MENÚ PRINCIPAL ==========
1. Agregar producto
2. Buscar producto
3. Eliminar producto
4. Actualizar disponibilidad
5. Mostrar productos
6. Salir
=====================================
          """)
    
    while True:
        try:
            op=int(input("Ingrese una opción: "))
            break
        except ValueError:
            print("Error: opción debe ser un número")

    if op==1:
        print(inventario)

    elif op==2:
        nombre=input("Ingrese el nombre del producto a buscar: ")
        posicion=buscar_producto(inventario,nombre)
        if posicion!=1:
            print(f"Producto encontrado en la posición {posicion}")
            mostrar_datos_producto(inventario[posicion])
        else:
            print(f"el producto {nombre} no se encuentra registrado.")

    elif op==3:
        nombre=input("Ingrese nombre")
        posicion=buscar_producto(inventario,nombre)
        if posicion !=1:
            del inventario(posicion)
            print("Producto eliminado correctamente")
        else:
            print(f"el producto {nombre} no se encuentra registrado.")

    elif op==4:
        inventario=actualizar_disponibilidad(inventario)
        print("Disponivilidad actualizada para todos los productos")

    elif op==5:
        mostrar_datos_producto(producto)

def validar_nombre(nombre):
    if nombre=="":
        return False
    return True

def validar_precio(precio):
    if precio<=0:
        return False
    return True

def validar_stock(stock):
    if stock<=0:
        return False
    return True

def validar_lista(inventario):
    if len(inventario)==0:
        return False
    return True

def agregar_producto(inventario):
    nombre=input("Ingrese nombre del producto: ")
    if validar_nombre(nombre)==False:
        print("Error el nombre no puede estar vacío.")
        return
    precio = int(input("Precio del producto: "))
    if validar_precio(precio)==False:
        print("Error el precrio debe ser mayor que 0.")
        return
    stock=int(input("Ingrese stock del producto: "))
    if validar_stock(stock)==False:
        print("Error, stock debe ser mayor que 0.")
        return
    
    producto={
        "nombre": nombre.strip(),
        "precio": precio,
        "stock": stock,
        "disponible": False
    }


    inventario.append(producto)
    print("Producto agregado con exito")
    return inventario

def buscar_producto(inventario.nombre):
    if validar_lista(inventario)==False:
        print("No hay productos registrados")
        return -1
    for i in range(len(inventario)):
        if inventario[i]["nombre"]==nombre:
            return -1
    return -1

def mostrar_datos_producto(producto):
    if producto["disponible"]:
        estado="Disponible"
    else:
        estado="Sin stock"

print(f"nombre: {producto["nombre"]}")
print(f"precio: {producto["precio"]}")
print(f"stock: {producto["stock"]}")
print(f"disponible: {disponible}")





