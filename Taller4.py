### Programacion de Computadoras IV
## Taller 4
# Braulio Rodriguez 8-899-1093

import redis

r = redis.Redis(host="localhost", port="6379", db=0)
r.flushall()

#Funciones


def add(var1, var2):
    r.set(var1, var2)


def edit(var3, var4):
    r.delete(var3)
    r.set(var3, var4)


def delete(var5):
    r.delete(var5)


def view():
    palabra = r.keys()
    for i in palabra:
        palabras = r.get(i)
        print("Slang: ", i, "Definicion: ", palabras)


def search(var6):
    buscar = r.get(var6)
    print("El slang", var6, " significa :", buscar)


# Menu de opciones
print("""
1. Insertar
2. Editar
3. Borrar
4. Visualizar
5. Buscar
6. Salir
""")

resp = 1
while(resp == 1):
    opcion = int(input("Ingrese una opcion"))

    if (opcion == 1):
        print("Ingresar nuevo registro")
        var1 = input("Ingrese un slang panameno: ")
        var2 = input("Ingrese su significado: ")
        add(var1, var2)

    elif (opcion == 2):
        print("Edite un registro: ")
        var3 = input("Ingrese un slang panameno ya existente: ")
        var4 = input("Ingrese su nuevo significado: ")
        edit(var3, var4)

    elif opcion == 3:
        print("Borre un registro")
        var5 = input("Ingrese el slang que desea eliminar")
        delete(var5)

    elif opcion == 4:
        print("Ver listado de palabras")
        view()

    elif opcion == 5:
        print("Buscar significado de palabra")
        var6 = input("Ingrese un slang panameno: ")
        search(var6)

    elif opcion == 6:
        break

    else:
        print("ERROR! OPCION INVALIDA")

    resp = input("Si desea continuar presione [1]")