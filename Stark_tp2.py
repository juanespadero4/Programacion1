from data_stark import lista_personajes
from FuncionesTP2 import *

while True:
    menu = int(input("""
    Seleccione cual de los siguientes datos quiere mostrar poniendo el numero asignado:
                
    (1) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
    (2) Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    (3) Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    (4) Recorrer la lista y determinar cuál es el superhéroe más débil de género M
    (5) Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
    (6)Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
    (7)Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    (8)Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    (9)Listar todos los superhéroes agrupados por color de ojos.
    (10)Listar todos los superhéroes agrupados por tipo de inteligencia
    (11) Salir.
    """))

    match menu:
        case 1:
            recorrido_lista_nb (lista_personajes)
        case 2:
            mas_alto_genero (lista_personajes, "F")
        case 3:
            mas_alto_genero (lista_personajes, "M")
        case 4:
            mas_debil_genero(lista_personajes, "M")
        case 5:
            mas_debil_genero(lista_personajes, "NB")
        case 6:
            promedio_fuerza_nb(lista_personajes)
        case 7:
            color_de_ojos_super(lista_personajes)
        case 8:
            color_de_pelo_super(lista_personajes)
        case 9:
            listar_personajes_por_color_de_ojos(lista_personajes)
        case 10:
            listar_personajes_por_inteligencia(lista_personajes)
        case 11:
            print("Usted salio del programa.")
            break