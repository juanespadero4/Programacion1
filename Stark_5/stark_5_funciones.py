import json
import re

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

