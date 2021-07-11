import os
import time
import mysql.connector
import re

# variable global creo el nbombre de la base de datos
DB_NOMBRE = "tp1_pythoninicialutn"
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""


def menu_principal():
    os.system("cls")
    opc = True
    while opc == True:
        os.system("cls")
        print(
            "\x1b[1;97;41m" + "***   Stock de Venta de Libros   ***" + "\x1b[0m" + "\n"
        )

        print("1. Alta / Baja / Modificacion")
        print("2. Consultas")
        print("3. Bases de datos")
        print("4. Salir\n")
        print("Seleccione una opcion, debe ingresar el número de opcion:")
        opc = input("Ingrese seleccion: ")

        if opc == "1":
            menu_abm()
            opc = True
        elif opc == "2":
            menu_consultas()
            opc = True
        elif opc == "3":
            menu_db()
            opc = True
        elif opc == "4":
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
        os.system("cls")
        print(
            "\x1b[1;97;41m"
            + "***   Alta / Baja / Modificacion   ***"
            + "\x1b[0m"
            + "\n"
        )
        print("1. Alta (Ingresa un libro nuevo)")
        print("2. Baja (Elimina un libro de la base de datos)")
        print(
            "3. Modificacion (Modifica un libro de la base de datos, el precio, la cantidad o el genero)"
        )
        print("4. Volver al menu anterior\n")
        print("Seleccione una opcion, debe ingresar el número de opcion:")
        opc = input("Ingrese seleccion: ")
        if opc == "1":
            print(
                "¿Cuantos ingresos de registro va a realizar? Ingrese un numero entre 1 y 20: "
            )
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

        os.system("cls")
        print(
            "\x1b[1;97;41m"
            + "***  Alta de Registro número "
            + str(cont)
            + "   ***"
            + "\x1b[0m"
            + "\n"
        )
        cont += 1
        libro = {}
        patron = re.compile("^[a-zA-Z0-9 ]*$")

        libro["codigo"] = input("Ingrese el codigo numerico del articulo: ")

        while libro.get("codigo").isnumeric() == False:
            print("Debe ingresar un numero")
            libro["codigo"] = input("Ingrese el codigo numerico del articulo: ")

        libro["nombre"] = input("Ingrese el nombre del libro: ")
        while patron.match(libro["nombre"]) is None:
            print("El nombre no debe contener caracteres especiales como $%& etc.:")
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
        while patron.match(libro["genero"]) is None:
            print("El genero no debe contener caracteres especiales como $%& etc.:")
            libro["genero"] = input("Ingrese el genero: ")

        # en un futuro este valor debera ser seleccionable de una tabla

        # deberia chequear si el codigo ingresado ya existe, de ser asi,
        # no le permitiria ingresar otro articulo con el mismo codigo
        alta_bd(libro)
        time.sleep(1)


def alta_bd(libro):
    libro["codigo"] = int(libro["codigo"])
    libro["precio"] = int(libro["precio"])
    libro["cantidad"] = int(libro["cantidad"])
    sent = (  # id , CODIGO, NOMBRE, CANTIDAD, PRECIO, GENERO
        "INSERT INTO productos "
        "(codigo, nombre, cantidad, precio, genero) "
        "VALUES (%(codigo)s, "
        + "'"
        + libro["nombre"]
        + "'"
        + ", %(cantidad)s, %(precio)s,"
        + "'"
        + libro["genero"]
        + "')"
    )
    # me conectgo a la base de datos
    db = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, passwd=DB_PASS, database=DB_NOMBRE
    )
    # creo cursor
    micursor = db.cursor()
    # inserto los valores en la base de datos
    # de acuerdo a la sentencia armada, y al libro pasado por parametro
    micursor.execute(sent, libro)
    db.commit()

    # me desconecto de la base de datos
    db.close()
    print("Agregando registro a la base de datos")
    time.sleep(2)
    print("Registro Agregado")
    time.sleep(2)
    return


def baja():
    opc = True
    while opc == True:
        os.system("cls")
        print("\x1b[1;97;41m" + "***  Baja de Registro  ***" + "\x1b[0m" + "\n")
        print(
            "Aqui podra eliminar libros de la base de datos. Para ello el stock debe ser 0."
        )

        print("1. Baja de articulo por Codigo")
        print("2. Baja de articulo por Nombre")
        print("3. Volver al menu anterior\n")
        opc = input("Seleccione una opcion, debe ingresar el número de opcion: ")
        if opc == "1":
            codigo = input("Ingrese el codigo del articulo: ")
            time.sleep(2)
            while codigo.isnumeric() == False:
                print("Debe ingresar un numero")
                codigo = input("Ingrese el codigo del articulo: ")
            time.sleep(2)
            baja_bd(codigo, tabla="productos")
            opc = True
        elif opc == "2":
            # nombre = input("Ingrese el nombre del articulo: ")
            print("Herramienta en desarrollo, aun no disponible")
            time.sleep(2)
            # baja_bd(nombre, tabla="productos")
            opc = True
        elif opc == "3":
            return
        else:
            print("La opcion elegida es invalida")
            time.sleep(2)
            opc = True


def baja_bd(codigo=0, nombre="", genero="", tabla=""):
    if codigo != 0:
        cod = existe("codigo", int(codigo), tabla)
        if cod:
            for x in cod:
                if x[3] > 0:
                    print("No se puede eliminar el articulo dado que aun hay stock.")
                    time.sleep(2)
                else:
                    print("Esta por eliminar el libro " + x[2])
                    print(
                        "¿Realmente desea ELIMINAR el articulo de la base de datos? (si/NO): "
                    )
                    resp = input()
                    if resp.lower() == "si":
                        baja_registro("codigo", int(codigo), tabla)
                        print("Eliminando Registro...")
                        time.sleep(2)
                        print("Registro eliminado con exito de la base de datos")
                        time.sleep(2)
        else:
            print("no se encontraron resultados")
            time.sleep(2)
    elif nombre != "":
        nom = existe("nombre", nombre, tabla)
        if nom:
            for x in nom:
                print(x)
                time.sleep(2)
        else:
            print("no se encontraron resultados")
            time.sleep(3)
    elif genero != "":
        gen = existe("genero", genero, tabla)
        if gen:
            for x in gen:
                print(x)
                time.sleep(2)
        else:
            print("no se encontraron resultados")
            time.sleep(3)

    return


def modificacion():
    opc = True
    while opc == True:
        os.system("cls")
        print("\x1b[1;97;41m" + "***  Modificacion de Registro  ***" + "\x1b[0m" + "\n")
        print("Aqui podra modificar la cantidad o precio de un articulo")

        codigo = input("Ingrese el codigo del articulo que desea modificar: ")
        while codigo.isnumeric() == False:
            print("Debe ingresar un numero")
            codigo = input("Ingrese el codigo del articulo: ")
        time.sleep(2)

        cod = existe("codigo", int(codigo), "productos")
        print("1. Modificar Cantidad")
        print("2. Modificar Precio")
        print("3. Volver al menu anterior\n")
        opc = input("Seleccione una opcion, debe ingresar el número de opcion: ")

        if opc == "1":
            if cod:
                nueva_cant = input(
                    "Ingrese la nueva cantidad para el articulo seleccionado: "
                )
                while nueva_cant.isnumeric() == False:
                    print("Debe ingresar un numero")
                    nueva_cantidad = input(
                        "Ingrese la nueva cantidad para el articulo seleccionado: "
                    )
                modificacion_registro("cantidad", nueva_cant, "productos", int(codigo))
                print("Modificando registro a la base de datos")
                time.sleep(2)
                print("Registro Modificado")
                time.sleep(2)
            else:
                print("no se encontraron resultados")
                time.sleep(2)
                opc = True
        elif opc == "2":
            if cod:
                nuevo_precio = input(
                    "Ingrese el nuevo precio para el articulo seleccionado: "
                )
                while nuevo_precio.isnumeric() == False:
                    print("Debe ingresar un numero")
                    nuevo_precio = input(
                        "Ingrese el nuevo precio para el articulo seleccionado: "
                    )

                modificacion_registro("precio", nuevo_precio, "productos", int(codigo))
                print("Modificando registro a la base de datos")
                time.sleep(2)
                print("Registro Modificado")
                time.sleep(2)
            else:
                print("no se encontraron resultados")
                time.sleep(2)
            opc = True
        elif opc == "3":
            return
        else:
            print("La opcion elegida es invalida")
            time.sleep(2)
            opc = True


def menu_consultas():
    print("aqui se podran realizar consultas")
    print("Herramienta en desarrollo, aun no disponible")
    time.sleep(3)
    return


def menu_db():
    opc = True
    while opc == True:
        os.system("cls")
        print("\x1b[1;97;41m" + "***   Menu Bases de Datos   ***" + "\x1b[0m" + "\n")
        print("1. Crear Bases de Datos")
        print(
            "2. Eliminar Bases de datos"
            + "\x1b[1;97;41m"
            + "***   ALERTA: ESTO ELIMINARA TODA LA INFORMACION   ***"
            + "\x1b[0m"
            + "\n"
        )
        print("3. Volver al menu anterior\n")
        print("Seleccione una opcion, debe ingresar el número de opcion:")
        opc = input("Ingrese seleccion: ")
        if opc == "1":
            print(
                "Verificando si las bases de datos existen, de no ser asi seran creadas."
            )
            crea_db()
            opc = True
        elif opc == "2":
            print("¿Realmente desea ELIMINAR las bases de datos? (si/NO): ")
            resp = input()
            if resp.lower() == "si":
                print("¿Esta Seguro? (si/NO): ")
                resp = input()
                if resp.lower() == "si":
                    borra_db()
            else:
                opc = True
        elif opc == "3":
            return
        else:
            print("La opcion elegida es invalida")
            time.sleep(2)
            opc = True

    return


def crea_db():  # crea base de datos si no existen

    db_tablas = {}  # creo un diccionario con las tablas que contendra la base de datos

    db_tablas["productos"] = (  # id , CODIGO, NOMBRE, CANTIDAD, PRECIO, GENERO
        "CREATE TABLE IF NOT EXISTS productos ("
        "id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, "
        "codigo int(11) NOT NULL, "
        "nombre varchar(40) NOT NULL, "
        "cantidad int(11) NOT NULL, "
        "precio int(11) NOT NULL , "
        "genero varchar(40) NOT NULL)"
    )

    db_tablas["generos"] = (  # id, genero
        "CREATE TABLE IF NOT EXISTS generos ("
        "id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, "
        "genero varchar(40) NOT NULL)"
    )

    db = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, passwd=DB_PASS
    )  # conexion a base de datos

    # creo cursos para trabajar con el metodo execute
    micursor = db.cursor()
    # creo la base de datos si no existe
    sent = "CREATE DATABASE IF NOT EXISTS " + DB_NOMBRE
    micursor.execute(sent)
    # una vez creada la base de datos, le digo que lavoy a usar
    micursor.execute("USE {}".format(DB_NOMBRE))
    # recorro el diccionario db_tablas con un for para ir creando todas las tablas e imprimiendo un cartel indicando que fue creada
    # podria haber un mensaje diciendo que ya existian??
    for nombre_tablas in db_tablas:
        desc_tabla = db_tablas[nombre_tablas]
        print("Creando tabla {}: ".format(nombre_tablas), end="")
        micursor.execute(desc_tabla)
        print("OK")
        time.sleep(1)

    # disconnect from server
    db.close()


def borra_db():  # elimina base de datos si existen
    print("Eliminando Bases de datos...")
    time.sleep(2)
    # me conectgo a la base de datos
    db = mysql.connector.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS)
    # creo cursos para trabajar con el metodo execute
    micursor = db.cursor()
    # creo la base de datos si no existe
    sent = "DROP DATABASE IF EXISTS " + DB_NOMBRE
    micursor.execute(sent)
    # me desconecto de la base de datos
    db.close()
    print("Bases de datos eliminada. Deberá crearlas nuevamente...")
    time.sleep(2)


def existe(col, par, tab):  # verifica si existe
    sent = "SELECT * FROM " + tab + " WHERE " + col + " = %s"
    val = (par,)
    db = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, passwd=DB_PASS, database=DB_NOMBRE
    )
    micursor = db.cursor()
    micursor.execute(sent, val)
    resultado = micursor.fetchall()
    db.close()
    return resultado


def baja_registro(col, par, tab):
    sent = "DELETE FROM " + tab + " WHERE " + col + " = %s"
    val = (par,)
    db = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, passwd=DB_PASS, database=DB_NOMBRE
    )
    micursor = db.cursor()
    micursor.execute(sent, val)
    db.commit()
    db.close()
    return


def modificacion_registro(col, par, tab, cod):
    sent = "UPDATE " + tab + " SET " + col + " = %s" + " WHERE codigo = %s"
    val = (
        par,
        cod,
    )
    db = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, passwd=DB_PASS, database=DB_NOMBRE
    )
    micursor = db.cursor()
    micursor.execute(sent, val)
    db.commit()
    db.close()
    return


menu_principal()
