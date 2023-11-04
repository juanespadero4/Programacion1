import json
import re
from data_stark import lista_personajes

heroe = {}


def imprimir_dato(dato):
    print(dato)

def imprimir_menu_desafio_5():
    imprimir_dato("A-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    imprimir_dato("B-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    imprimir_dato("C-Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    imprimir_dato("D-Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    imprimir_dato("E-Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    imprimir_dato("F-Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    imprimir_dato("G-Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    imprimir_dato("H-Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    imprimir_dato("I-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)")
    imprimir_dato("J-Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    imprimir_dato("K-Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    imprimir_dato("L-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).")
    imprimir_dato("M-Listar todos los superhéroes agrupados por color de ojos.")
    imprimir_dato("N-Listar todos los superhéroes agrupados por color de pelo.")
    imprimir_dato("O-Listar todos los superhéroes agrupados por tipo de inteligencia")
    imprimir_dato("Z-SALIR")

def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    opcion = input("Opcion: ")
    str_txt = r'^[a-zA-Z\s]$'
    if re.match(str_txt, opcion):
        return opcion
    else:
        return -1

# def stark_marvel_app_5(data):      DEJAR PARA LO ULTIMO
    
def leer_archivo(nombre_archivo):
    with open('data_stark.json') as file:
        lista_personajes = json.load(file)
    return lista_personajes


def guardar_archivo(nombre_archivo, contenido):
    try:
        archivo = open(nombre_archivo, "w+")
        archivo.write(contenido)
        archivo.close()
        print(f"Se creo el archivo: {nombre_archivo}")
        return True
    except:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False
    

# Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
# string que puede contener una o muchas palabras. La función deberá
# retornar dicho string en el cual todas y cada una de las palabras que
# contenga, deberán estar capitalizadas (Primera letra en mayúscula).

def capitalizar_palabras(frase):
    palabras = frase.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return ' '.join(palabras_capitalizadas)

# Crear la función 'obtener_nombre_capitalizado' la cual recibirá por
# parámetro un diccionario el cual representará a un héroe y devolverá
# un string el cual contenga su nombre formateado de la siguiente
# manera:
# Nombre: Venom
# Reutilizar 'capitalizar_palabras'
def obtener_nombre_capitalizado(heroe):
    nombre = heroe["nombre"]
    nombre_formateado = capitalizar_palabras(nombre)
    return f"Nombre: {nombre_formateado}"

# Crear la función 'obtener_nombre_y_dato' la cual recibirá por
# parámetro un diccionario el cual representará a un héroe y una key
# (string) la cual representará la key del héroe a imprimir. La función
# devolverá un string el cual contenga el nombre y dato (key) del héroe a
# imprimir.
# El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
# El string resultante debe estar formateado al estilo: (suponiendo que la
# key es fuerza)
# Nombre: Venom | Fuerza: 500
# Reutilizar 'obtener_nombre_capitalizado'

def obtener_nombre_y_dato(heroe, clave):
    nombre_formateado = obtener_nombre_capitalizado(heroe)
    if clave in heroe:
        dato = heroe[clave]
        return f"{nombre_formateado} | {clave.capitalize()}: {dato}"
    else:
        return f"{nombre_formateado} | {clave.capitalize()}: No disponible"

# Crear la función 'es_genero' la cual recibirá por parámetro un
# diccionario que representará un héroe y un string el cual será usado
# para evaluar si el héroe coincide con el género buscado (El string
# puede ser M, F o NB). retornará True en caso de que cumpla, False
# caso contrario.

def es_genero(heroe, genero):
    if genero == heroe["genero"]:
        return True
    else:
        return False
    

# Crear la función 'stark_guardar_heroe_genero' la cual recibira por
# parámetro la lista de héroes y un string el cual representará el género
# a evaluar (puede ser M o F). Deberá imprimir solamente los héroes o
# heroínas que coincidan con el género pasado por parámetro y
# además, deberá guardar dichos nombres en un archivo con extensión
# csv (cada nombre deberá ir separado por una coma)
# Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado',
# 'imprimir_dato' y 'guardar_archivo'.
# En el caso de 'guardar_archivo', cuando se llame a esta función el
# nombre de archivo a guardar deberá respetar el formato:
# heroes_M.csv, heroes_F.csv o heroes_NB según corresponda.
# La función retornará True si pudo guardar el archivo, False caso
# contrario.

def stark_guardar_heroe_genero(heroes, genero):
    heroes_genero = []
    for heroe in heroes:
        if es_genero(heroe, genero):
            nombre_formateado = obtener_nombre_capitalizado(heroe)
            heroes_genero.append(nombre_formateado)
    
    archivo_genero = f"heroes_{genero}.csv"
    contenido = ",".join(heroes_genero)
    
    if guardar_archivo(archivo_genero, contenido):
        print(f"Se creó el archivo: {archivo_genero}")
        return True
    else:
        print(f"Error al crear el archivo: {archivo_genero}")
        return False