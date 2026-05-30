#funciones
def SumarDosNumeros():
    '''Esta funcion permite sumar dos números,
        ingresados dentro de la función    
        '''
    num1=int(input("Ingrese número 1: "))
    num2=int(input("Ingrese número 2: "))
    suma=num1+num2
    print(f"la suma del {num1} + {num2} es: {suma}")
    
def sumar(a,b):
    suma= a + b
    return suma

#linea ppal
SumarDosNumeros()

res=sumar(4,5)
print(res)

num1=int(input("Numero 1: "))
num2=int(input("Numero 2: "))
res=sumar(num1,num2)
print ("La suma es: ",res)