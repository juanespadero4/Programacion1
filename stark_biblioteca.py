from data_stark import lista_personajes
import re

def stark_normalizar_datos(lista: list):
    '''Normaliza los datos y los vuelve in o float si son numeros enteros o con coma, si es str lo deja como esta'''
    exito = False
    for personaje in lista:
        for clave, valor in personaje.items():
            if personaje[clave] == "":
                continue

            if isinstance(valor, (int, float)):
                continue

            if re.match(r'^[0-9]+\.[0-9]+$', str(valor)):
                personaje[clave] = float(valor)

                exito = True
            elif re.match(r'^[0-9]+$', str(valor)):
                personaje[clave] = int(valor)
                exito = True

    if exito == True:
        return "Datos Normalizados."
    else:
        return "Datos normalizados incorrectamente."


def obtener_dato(diccionario: dict, clave):
    '''Obtiene un dato concreto de un diccionario'''
    if diccionario != {} and clave in diccionario:
        return diccionario[clave]
    else:
        return False


def obtener_nombre(diccionario: dict):
    nombre = obtener_dato(diccionario, "nombre")
    if nombre is not False:
        return nombre
    else:
        print("ERROR")
        return None


def obtener_nombre_y_dato(diccionario, clave):
    nombre = obtener_nombre(diccionario)
    dato = obtener_dato(diccionario, clave)
    if nombre is not None and dato is not False:
        print(f"Nombre: {nombre} | {clave}: {dato}")
    else:
        print("ERROR")
        return None

def obtener_maximo(lista, clave):
    if not lista:
        print("ERROR: La lista esta vacia")
        return
    maximo = None
    identidad_maximo = None
    for personaje in lista:
        valor = personaje.get(clave)
        if valor is None:
            print(f"ERROR: El personaje no tiene la clave '{clave}'")
            return
        if not isinstance(valor, (int, float)):
            print(f"ERROR: El valor de '{clave}' no es un numero (int o float)")
            return False
        if maximo is None or valor > maximo:
            maximo = valor
            identidad_maximo = personaje.get("nombre", "Nombre Desconocido")
    if identidad_maximo is not None:
        return maximo


def obtener_minimo(lista, clave):
    if not lista:
        print("ERROR: La lista está vacia")
        return
    minimo = 9999
    identidad_minimo = None
    for personaje in lista:
        if type(personaje[clave]) != int and type(personaje[clave]) != float:
            print("ERROR: La clave no es un numero (int o float)")
            return False
        valor = personaje.get(clave, None)
        if isinstance(valor, (int, float)):
            if valor < minimo:
                minimo = valor
                identidad_minimo = personaje.get("nombre", None)
    if identidad_minimo is not None:
        return minimo

def obtener_dato_cantidad(lista, variable, clave):
    personajes_list = []
    for personaje in lista:
        if personaje[clave] == variable:
            personajes_list.append(personaje)
    if not personajes_list:
        personajes_list = []

    return personajes_list


def stark_imprimir_heroes(lista):
    for personaje in lista:
        if not lista:
            return False
        else:
            print(f"Nombre: {personaje['nombre']}")
            print(f"Identidad: {personaje['identidad']}")
            print(f"Empresa: {personaje['empresa']}")
            print(f"Altura: {personaje['altura']}")
            print(f"Peso: {personaje['peso']}")
            print(f"Genero: {personaje['genero']}")
            print(f"Color de ojos: {personaje['color_ojos']}")
            print(f"Color de pelo: {personaje['color_pelo']}")
            print(f"Fuerza: {personaje['fuerza']}")
            print(f"Inteligencia: {(personaje['inteligencia']).capitalize()}")
            print("--------------------------------------------")

def stark_imprimir_nombre_genero(lista):
    for personaje in lista:
        if not lista:
            return False
        else:
            print(f"Nombre: {personaje['nombre']} | Genero: {personaje['genero']}")
            print("--------------------------------------------")

def sumar_dato_heroe(lista, clave):
    suma = 0
    for personaje in lista:
        if clave in personaje:
            valor = personaje.get(clave)
            if isinstance(valor, (int, float)):
                suma += valor
    return suma


def dividir(numero1, numero2):
    numero_final = 0
    if numero2 != 0:
        numero_final = numero1 / numero2
    return numero_final


def calcular_promedio(lista, clave):
    cantidad = len(lista)
    suma = sumar_dato_heroe(lista, clave)
    promedio = dividir(suma, cantidad)
    return promedio


def mostrar_promedio_dato(lista, clave):
    if not lista:
        return False

    for personaje in lista:
        if clave in personaje:
            dato = personaje.get(clave)
            if isinstance(dato, (int, float)):
                promedio = calcular_promedio(lista, clave)
                return promedio


def imprimir_menu():
    print("Bienvenido al Menu Stark, por favor ingrese el numero de una de las opciones a continuacion:")
    print("(1) Normalizar datos de la lista")
    print("(2) Recorrer la lista imprimiendo por consola el nombre de cada superheroe de genero NB")
    print("(3) Recorrer la lista y determinar cuál es el superheroe más alto de genero F")
    print("(4) Recorrer la lista y determinar cuál es el superheroe más alto de genero M")
    print("(5) Recorrer la lista y determinar cuál es el superheroe más débil de genero M")
    print("(6) Recorrer la lista y determinar cuál es el superheroe más débil de genero NB")
    print("(7) Recorrer la lista y determinar la fuerza promedio de los superheroes de genero NB")
    print("(8) Determinar cuántos superheroes tienen cada tipo de color de ojos.")
    print("(9) Determinar cuántos superheroes tienen cada tipo de color de pelo.")
    print("(10) Listar todos los superheroes agrupados por color de ojos.")
    print("(11) Listar todos los superheroes agrupados por tipo de inteligencia")
    print("(12) Salir.")


def validar_entero(numero):
    if numero.isdigit():
        return True
    else:
        return False


def stark_menu_principal():
    imprimir_menu()
    opcion = input("Opcion: ")
    while not validar_entero(opcion) or not (1 <= int(opcion) <= 12):
        print("Opcion no valida. Por favor, ingrese un numero valido del 1 al 12.")
        opcion = input("Opcion: ")
    return int(opcion)

def listar_personajes_por_color_de_ojos(lista):
    personajes_por_color = {}

    for personaje in lista:
        nombre = personaje["nombre"]
        color_ojos = personaje.get("color_ojos").lower()
        
        if color_ojos in personajes_por_color:
            personajes_por_color[color_ojos].append(nombre)
        else:
            personajes_por_color[color_ojos] = [nombre]

    for color_ojos, lista_personajes in personajes_por_color.items():
        print(f'Color de ojos: {color_ojos}')
        for personaje in lista_personajes:
            print(f'{personaje}')
        print("--------------------------")

    
def color_de_ojos_super(lista):
    conteo_colores = {}
    for personaje in lista:
        color = personaje["color_ojos"].lower()
        conteo_colores[color] = conteo_colores.get(color, 0) + 1
    for color, cantidad in conteo_colores.items():
        print(f'Color de ojos: {color}, Cantidad: {cantidad}')
        

def color_de_pelo_super(lista):
    conteo_colores = {}

    for personaje in lista:
        color_pelo = personaje["color_pelo"].lower()
        conteo_colores[color_pelo] = conteo_colores.get(color_pelo, 0) + 1

    for color, cantidad in conteo_colores.items():
        print(f'Color de pelo: {color}, Cantidad: {cantidad}')

def listar_personajes_por_inteligencia(lista):
    personajes_por_inteligencia = {}

    for personaje in lista:
        nombre = personaje["nombre"]
        inteligencia = personaje.get("inteligencia").lower()  
        if inteligencia in personajes_por_inteligencia:
            personajes_por_inteligencia[inteligencia].append(nombre)
        else:
            personajes_por_inteligencia[inteligencia] = [nombre]

    for inteligencia, lista_personajes in personajes_por_inteligencia.items():
        print(f'Nivel de inteligencia: {inteligencia}')
        for personaje in lista_personajes:
            print(f'{personaje}')
        print("--------------------------")


def stark_marvel_app(lista):
    flag = True
    personajes_nb = []
    personajes_m = []
    personajes_f = []
    while flag:
        opcion = stark_menu_principal()
        match opcion:
            case 1:
                print(stark_normalizar_datos(lista_personajes)) #HECHO
            case 2:
                personajes_nb = obtener_dato_cantidad(lista_personajes, "NB", "genero") #HECHO
                if not personajes_nb:
                    print("\nNo hay personajes del genero no binario.\n") 
                else:
                    stark_imprimir_heroes(personajes_nb)
            case 3:
                personajes_f = obtener_dato_cantidad(lista_personajes, "F", "genero")
                maxima_altura = obtener_maximo(personajes_f, "altura")
                personaje_f_alto = obtener_dato_cantidad(personajes_f, maxima_altura, "altura")
                for personaje in personaje_f_alto:
                    print(f"\nEl personaje mas alto del genero femenino es {personaje['nombre']}, y su altura es {personaje['altura']}\n")
            case 4:
                personajes_m = obtener_dato_cantidad(lista_personajes, "M", "genero")
                maxima_altura = obtener_maximo(personajes_m, "altura")
                personaje_m_alto = obtener_dato_cantidad(personajes_m, maxima_altura, "altura")
                for personaje in personaje_m_alto:
                    print(f"\nEl personaje mas alto del genero masculino es {personaje['nombre']}, y su altura es {personaje['altura']}\n")
            case 5:
                personajes_m = obtener_dato_cantidad(lista_personajes, "M", "genero")
                minima_fuerza = obtener_minimo(personajes_m, "fuerza")
                personaje_fuerza_minima = obtener_dato_cantidad(personajes_m, minima_fuerza, "fuerza")
                for personaje in personaje_fuerza_minima:
                    print(f"\nEl personaje {personaje['nombre']} tiene la menor fuerza, que es {personaje['fuerza']}\n")
            case 6: 
                personajes_nb = obtener_dato_cantidad(lista_personajes, "NB", "genero")
                if not personajes_nb:
                    print("\nNo hay personajes de ese genero en la lista.\n") 
                else:
                    minima_fuerza_nb = obtener_minimo(personajes_nb, "fuerza")
                    personaje_fuerza_minima_nb = obtener_dato_cantidad(personajes_nb, minima_fuerza_nb, "fuerza")
                    for personaje in personaje_fuerza_minima_nb:
                        print(f"\nEl personaje mas debil del genero NB es {personaje['nombre']}, y su fuerza es de {personaje['fuerza']}\n")
            case 7:
                personajes_nb = obtener_dato_cantidad(lista_personajes, "NB", "genero")
                promedio_fuerza_nb = mostrar_promedio_dato(personajes_nb, "fuerza")
                if not promedio_fuerza_nb:
                    print("No hay datos para promediar, es posible que no haya personajes no binarios.")
                else:
                    print(f"El promedio de fuerza de los no binarios es {promedio_fuerza_nb}")
            case 8:
                color_de_ojos_super(lista_personajes)
            case 9:
                color_de_pelo_super(lista_personajes)
            case 10:
                listar_personajes_por_color_de_ojos(lista_personajes)
            case 11:
                listar_personajes_por_inteligencia(lista_personajes)
            case 12:
                print("Usted eligio salir del programa, hasta la proxima!")
                break


stark_marvel_app(lista_personajes)
