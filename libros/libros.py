import os
import time


def menu_principal():
    opc = True
    while opc == True:
        os.system('cls')
        print("\x1b[1;97;41m" +
              "***   Stock de Venta de Libros   ***" + "\x1b[0m" + "\n")

        print("1. Alta / Baja / Modificacion")
        print("2. Consultas")
        print("3. Salir\n")
        print("Seleccione una opcion, debe ingresar el número de opcion:")
        opc = input("Ingrese seleccion: ")

        if opc == "1":
            menu_abm()
            opc = True
        elif opc == "2":
            menu_consultas()
            opc = True
        elif opc == "3":
            print("¿Realmente desea Salir? (si/NO): ")
            resp = input()
            if resp.lower() == "si":
                return
            else:
                opc = True
        else:
            print("La opcion elegida es invalida")
            time.sleep(2)
            opc = True

        # time.sleep(1)
    return


def menu_abm():
    opc = True
    while opc == True:
        os.system('cls')
        print("\x1b[1;97;41m" +
              "***   Alta / Baja / Modificacion   ***" + "\x1b[0m" + "\n")
        print("1. Alta")
        print("2. Baja ")
        print("3. Modificacion")
        print("4. Volver al menu anterior\n")
        print("Seleccione una opcion, debe ingresar el número de opcion:")
        opc = input("Ingrese seleccion: ")
        if opc == "1":
            print(
                "¿Cuantos ingresos de registro va a realizar? Ingrese un numero entre 1 y 20: ")
            cant = int(input())
            if (cant > 0) and (cant < 20):
                alta(cant)
            else:
                print("Valor invalido")
                time.sleep(2)
            opc = True
        elif opc == "2":
            baja()
            opc = True
        elif opc == "3":
            modificacion()
            opc = True
        elif opc == "4":
            return
        else:
            print("La opcion elegida es invalida")
            time.sleep(2)
            opc = True

    return


def alta(cant):
    cont = 1
    while cant > 0:
        print(cant)
        cant -= 1

        os.system('cls')
        print("\x1b[1;97;41m" + "***  Alta de Registro número " +
              str(cont) + "   ***" + "\x1b[0m" + "\n")
        cont += 1

        libro = {"codigo": "", "nombre": "",
                 "cantidad": "", "precio": "", "genero": ""}

        libro["codigo"] = input("Ingrese el codigo numerico del articulo: ")

        while libro.get("codigo").isnumeric() == False:
            print("Debe ingresar un numero")
            libro["codigo"] = input(
                "Ingrese el codigo numerico del articulo: ")

        libro["nombre"] = input("Ingrese el nombre del libro: ")

        libro["cantidad"] = input("Ingrese la cantidad: ")
        while libro.get("cantidad").isnumeric() == False:
            print("Debe ingresar un numero")
            libro["cantidad"] = input("Ingrese la cantidad: ")

        libro["precio"] = input("Ingrese el precio unitario: ")
        while libro.get("precio").isnumeric() == False:
            print("Debe ingresar un numero")
            libro["precio"] = input("Ingrese el precio unitario: ")

        libro["genero"] = input("Ingrese el genero: ")

        print(libro)
        alta_bd(libro)
        time.sleep(1)


def alta_bd(libro):
    print("aqui se realizara el alta en la base de datos y se devolvera al usuario la confirmacion")
    time.sleep(2)
    return


def baja():
    opc = True
    while opc == True:
        os.system('cls')
        print("\x1b[1;97;41m" +
              "***  Baja de Registro  ***" + "\x1b[0m" + "\n")
        print(
            "Aqui podra eliminar libros de la base de datos. Para ello el stock debe ser 0.")

        print("1. Baja de articulo por Codigo")
        print("2. Baja de articulo por Nombre")
        print("3. Volver al menu anterior\n")
        opc = input(
            "Seleccione una opcion, debe ingresar el número de opcion: ")
        if opc == "1":
            codigo = input("Ingrese el codigo del articulo: ")
            time.sleep(2)
            while codigo.isnumeric() == False:
                print("Debe ingresar un numero")
                codigo = input("Ingrese el codigo del articulo: ")
            time.sleep(2)
            baja_bd(codigo)
            opc = True
        elif opc == "2":
            nombre = print("Ingrese el nombre del articulo")
            time.sleep(2)
            baja_bd(nombre)
            opc = True
        elif opc == "3":
            return
        else:
            print("La opcion elegida es invalida")
            time.sleep(2)
            opc = True


def baja_bd(codigo=0, nombre=""):
    print("aqui se realizara la baja en la base de datos y se devolvera al usuario la confirmacion")
    print("lo busca, si lo encuentra y el stock esta en 0 lo elimina")
    time.sleep(3)
    return


def modificacion():
    print("aqui se podran realizar modificaciones en el stock, cantidades o precios, o corregir errores de tipeo en el nombre")
    time.sleep(3)
    return


def menu_consultas():
    print("aqui se podran realizar consultas")
    time.sleep(3)
    return


menu_principal()
