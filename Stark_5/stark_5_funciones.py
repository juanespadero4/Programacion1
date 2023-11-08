import json
import re
from data_stark import lista_personajes
from sanitizar import *

heroe = {}

def imprimir_dato(dato: str):
    print(dato)

'''1.1'''
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

'''1.2'''
def stark_menu_principal_desafio_5() -> str:
    imprimir_menu_desafio_5()
    opcion = input("Opcion: ")
    str_txt = r'^[a-zA-Z\s]$'
    if re.match(str_txt, opcion):
        return opcion
    else:
        return -1

# def stark_marvel_app_5(data):      DEJAR PARA LO ULTIMO

'''1.4'''
def leer_archivo(nombre_archivo: str) -> list:
    with open('data_stark.json') as file:
        lista_personajes = json.load(file)
    return lista_personajes

'''1.5'''
def guardar_archivo(nombre_archivo: str, contenido: str) -> bool:
    try:
        archivo = open(nombre_archivo, "w+")
        archivo.write(contenido)
        archivo.close()
        print(f"Se creo el archivo: {nombre_archivo}")
        return True
    except:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False

'''1.6'''
def capitalizar_palabras(frase: str) -> str:
    palabras = frase.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return ' '.join(palabras_capitalizadas)

'''1.7'''
def obtener_nombre_capitalizado(heroe: dict) -> str:
    nombre = heroe["nombre"]
    nombre_formateado = capitalizar_palabras(nombre)
    return f"Nombre: {nombre_formateado}"

'''1.8'''
def obtener_nombre_y_dato(heroe: dict, clave: str) -> str:
    nombre_formateado = obtener_nombre_capitalizado(heroe)
    if clave in heroe:
        dato = heroe[clave]  # str
        return f"{nombre_formateado} | {clave.capitalize()}: {dato}"
    else:
        return f"{nombre_formateado} | {clave.capitalize()}: No disponible"

'''2.1'''
def es_genero(heroe: dict, genero: str) -> bool:
    if genero == heroe["genero"]:
        return True
    else:
        return False

'''2.2'''
def stark_guardar_heroe_genero(lista_heroes: list, genero: str) -> bool:
    heroes_coincidentes = []
    for heroe in lista_heroes:
        if es_genero(heroe, genero):
            nombre_formateado = obtener_nombre_capitalizado(heroe)
            imprimir_dato(nombre_formateado)
            heroes_coincidentes.append(nombre_formateado)
    nombre_archivo = f"heroes_{genero}.csv" 
    contenido = ",".join(heroes_coincidentes) 
    if guardar_archivo(nombre_archivo, contenido):
        return True
    else:
        return False

'''3.1'''
def calcular_min(lista_personajes: list, key: str) -> dict:
    min_value = float('inf')
    minimo_heroe = None
    for personaje in lista_personajes:
        if key in personaje:
            dato = float(personaje[key])
            if dato < min_value:
                min_value = dato
                minimo_heroe = personaje
    return minimo_heroe

def calcular_min_genero(lista_personajes: list, key: str, genero: str) -> dict:
    min_value = float('inf')
    min_hero = None
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            if key in personaje:
                dato = float(personaje[key])
                if dato < min_value:
                    min_value = dato
                    min_hero = personaje
    if min_hero is not None:
        return min_hero
    else:
        return None

'''3.2'''
def calcular_max(lista_personajes: list, key: str) -> dict:
    max_value = float('-inf')
    maximo_heroe = None
    for personaje in lista_personajes:
        if key in personaje:
            dato = float(personaje[key])
            if dato > max_value:
                max_value = dato
                maximo_heroe = personaje
    return maximo_heroe

def calcular_max_genero(lista_personajes: list, key: str, genero: str) -> dict:
    max_value = float('-inf')
    max_hero = None
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            if key in personaje:
                dato = float(personaje[key])
                if dato > max_value:
                    max_value = dato
                    max_hero = personaje
    if max_hero is not None:
        return max_hero
    else:
        return None

'''3.3'''
def calcular_max_min_dato_genero(genero: str, max_o_min: str, key: str) -> dict: 
    if genero in ["M", "F", "NB"]:
        if max_o_min == "minimo":
            return calcular_min_genero(lista_personajes, key, genero)
        elif max_o_min == "maximo":
            return calcular_max_genero(lista_personajes, key, genero)
        else:
            return "Opción inválida: max_o_min debe ser 'minimo' o 'maximo'"
    else:
        return "Género inválido: debe ser 'M', 'F' o 'NB'"

'''3.4'''
def stark_calcular_imprimir_guardar_heroe_genero(lista_personajes: list, genero: str, max_o_min: str, key: str) -> bool: 
    heroe = calcular_max_min_dato_genero(lista_personajes, genero, max_o_min, key)
    if heroe is not None:
        mensaje = obtener_nombre_y_dato(heroe, key)
        imprimir_dato(mensaje)
        nombre_archivo = f"heroes_{max_o_min}_{key}_{genero}.csv" 
        contenido = mensaje
        guardar_archivo(nombre_archivo, contenido)
        return True
    else:
        return False

'''4.1'''
def sumar_dato_heroe_genero(lista_heroes: list, key: str, genero: str) -> int:
    for heroe in lista_heroes:
        if isinstance(heroe, dict) and heroe and heroe.get('genero') == genero:
            if key in heroe and isinstance(heroe[key], (int, float)):
                suma += heroe[key]
    if suma > 0:
        return suma
    else:
        return -1

def cantidad_heroes_genero(lista_heroes: list, genero: str) -> int:
    count = 0
    for heroe in lista_heroes:
        if heroe['genero'] == genero:
            count += 1
    return count

'''4.2'''
def calcular_promedio_genero(lista_personajes: list, genero: str, key: str) -> float:
    suma = sumar_dato_heroe_genero(lista_personajes, key, genero)
    cantidad = cantidad_heroes_genero(lista_personajes, genero)
    if suma != -1 and cantidad != 0:
        promedio = dividir(suma, cantidad)
        return promedio
    else:
        return -1

'''4.4'''
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes: list, genero: str) -> bool:
    if len(lista_personajes) > 0:
        promedio = calcular_promedio_genero(lista_personajes, 'altura', genero)
        if promedio != -1:
            mensaje = f"Altura promedio género {genero}: {promedio:.2f}"
            imprimir_dato(mensaje)
            nombre_archivo = f"heroes_promedioaltura{genero}.csv" 
            contenido = mensaje 
            return guardar_archivo(nombre_archivo, contenido)
        else:
            imprimir_dato("Error: No se pudo calcular el promedio")
            return False
    else:
        imprimir_dato("Error: Lista de héroes vacía")
        return False

'''5.1'''
def calcular_cantidad_tipo(lista_heroes: list, tipo_dato: str) -> dict: 
    if not lista_heroes:
        return {"Error": "La lista se encuentra vacía"}
    cantidad_tipo = {}
    for heroe in lista_heroes:
        if tipo_dato in heroe:
            valor = heroe[tipo_dato] 
            valor_capitalizado = capitalizar_palabras(valor)
            if valor_capitalizado in cantidad_tipo:
                cantidad_tipo[valor_capitalizado] += 1
            else:
                cantidad_tipo[valor_capitalizado] = 1
    diccionario_salteado = json.dumps(cantidad_tipo, indent=4) 
    dict_final = json.loads(diccionario_salteado) 
    return dict_final

'''5.2'''
def guardar_cantidad_heroes_tipo(diccionario: dict, tipo_dato: str) -> bool: 
    mensaje = ""
    if isinstance(diccionario, dict):
        for key, value in diccionario.items():
            mensaje += f"Caracteristica: {tipo_dato} {key} - Cantidad de heroes: {value}\n"
        nombre_archivo = f"heroes_cantidad_{tipo_dato}.csv"
        if guardar_archivo(nombre_archivo, mensaje):
            return True
        else:
            return False
    else:
        return False

'''5.3.'''
def stark_calcular_cantidad_por_tipo(lista_heroes: list, tipo_dato: str) -> bool: 
    cantidad_tipo = calcular_cantidad_tipo(lista_heroes, tipo_dato)
    if guardar_cantidad_heroes_tipo(cantidad_tipo, tipo_dato) == True:
        return True
    else:
        return False

'''6.1'''
def obtener_lista_de_tipos(lista_heroes: list, dato: str) -> set: 
    lista_valores = []
    for heroe in lista_heroes:
        valor = heroe.get(dato, "")
        if not valor:
            valor = "N/A"
        lista_valores.append(valor)
    lista_valores = set([capitalizar_palabras(valor) for valor in lista_valores])
    return lista_valores

print(obtener_lista_de_tipos(lista_personajes, "color_pelo"))

'''6.2'''
def normalizar_dato(dato: str, valor_default: str) -> str: 
    if not dato:
        return valor_default
    else:
        return dato

'''6.3'''
def normalizar_heroe(heroe: dict, clave: str) -> dict:  
    if clave in heroe:
        valor = heroe[clave]
        valor_normalizado = normalizar_dato(valor, "N/A")
        valor_normalizado = capitalizar_palabras(valor_normalizado)
        heroe[clave] = valor_normalizado
    if "nombre" in heroe:
        nombre = heroe["nombre"]
        nombre_capitalizado = capitalizar_palabras(nombre)
        heroe["nombre"] = nombre_capitalizado
    return heroe

