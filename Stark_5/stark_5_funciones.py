import json
import re
from sanitizar import *

heroe = {}

def imprimir_dato(dato: str):
    #imprime el dato asado por parametro, debe ser un str.
    print(dato)

'''1.1'''
def imprimir_menu_desafio_5():
    #Imprime menu y sus opciones.
    print("BIENVENIDO A INDUSTRIAS STARK \n", 
            "A)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M \n", 
            "B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n",
            "C) Recorrer la lista y determinar cuál es el superhéroe más alto de género M \n", 
            "D) Recorrer la lista y determinar cuál es el superhéroe más alto de género F \n",
            "E) Recorrer la lista y determinar cuál es el superhéroe más bajo de género M \n",
            "F) Recorrer la lista y determinar cuál es el superhéroe más bajo de género F \n",
            "G) Recorrer la lista y determinar la altura promedio de los superhéroes de género M \n",
            "H) Recorrer la lista y determinar la altura promedio de los superhéroes de género F \n",
            "I) Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F) \n",
            "J) Determinar cuántos superhéroes tienen cada tipo de color de ojos. \n",
            "K) Determinar cuántos superhéroes tienen cada tipo de color de pelo. \n",
            "L) Determinar cuántos superhéroes tienen cada tipo de inteligencia \n",
            "M) Listar todos los superhéroes agrupados por color de ojos. \n",
            "N) Listar todos los superhéroes agrupados por color de pelo. \n",
            "O) Listar todos los superhéroes agrupados por tipo de inteligencia \n",
            "Z) SALIR \n")

'''1.2'''
def stark_menu_principal_desafio_5() -> str:
    #Imprime el menu con su funcion y luego nos da la opcion de poner una letra la cual corresponde a una opcion del menu.
    imprimir_menu_desafio_5()
    opcion = input("Opcion: ")
    str_txt = r'^[a-zA-Z\s]$'
    if re.match(str_txt, opcion):
        return opcion
    else:
        return -1

'''1.3'''
def stark_marvel_app_5(lista_personajes):
    #Funcion principal del programa, se le pasa la lista de personajes como parametro.
    stark_normalizar_datos(lista_personajes)
    while True:
        opcion = stark_menu_principal_desafio_5()
        if opcion == "A":
            stark_guardar_heroe_genero(lista_personajes, "M")
            print ("-----------------------------------------------------")
        elif opcion == "B":
            stark_guardar_heroe_genero(lista_personajes, "F")
            print ("-----------------------------------------------------")
        elif opcion == "C":
            stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "M", "maximo", "altura")
            print ("-----------------------------------------------------")
        elif opcion == "D":
            stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "F", "maximo", "altura")
            print ("-----------------------------------------------------")
        elif opcion == "E":
            stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "M", "minimo", "altura")
            print ("-----------------------------------------------------")
        elif opcion == "F":
            stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "F", "minimo", "altura")
            print ("-----------------------------------------------------")
        elif opcion == "G":
            stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes, "M")
            print ("-----------------------------------------------------")
        elif opcion == "H":
            stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes, "F")
            print ("-----------------------------------------------------")
        elif opcion == "I":
            stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "M", "maximo", "altura")
            stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "F", "maximo", "altura")
            stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "M", "minimo", "altura")
            stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, "F", "minimo", "altura")
        elif opcion == "J":
            stark_calcular_cantidad_por_tipo(lista_personajes, "color_ojos")
            archivo = open('heroes_cantidad_color_ojos.csv', 'r+')
            texto = archivo.read()
            print(texto)
            archivo.close()
        elif opcion == "K":
            stark_calcular_cantidad_por_tipo(lista_personajes, "color_pelo")
            archivo = open('heroes_cantidad_color_pelo.csv', 'r+')
            texto = archivo.read()
            print(texto)
            archivo.close()
        elif opcion == "L":
            stark_calcular_cantidad_por_tipo(lista_personajes, "inteligencia")
            archivo = open('heroes_cantidad_inteligencia.csv', 'r+')
            texto = archivo.read()
            print(texto)
            archivo.close()
        elif opcion == "M":
            tipos_color_ojos = obtener_lista_de_tipos(lista_personajes, "color_ojos")
            diccionario_heroes_por_color_ojos = obtener_heroes_por_tipo(lista_personajes, tipos_color_ojos, "color_ojos")
            for color_ojos, heroes in diccionario_heroes_por_color_ojos.items():
                print(f"Color de ojos: {color_ojos}")
                for heroe in heroes:
                    print(heroe)
                print("--------------")
        elif opcion == "N":
            tipos_color_pelo = obtener_lista_de_tipos(lista_personajes, "color_pelo")
            diccionario_heroes_por_color_pelo = obtener_heroes_por_tipo(lista_personajes, tipos_color_pelo, "color_pelo")
            for color_pelo, heroes in diccionario_heroes_por_color_pelo.items():
                print(f"Color de pelo: {color_pelo}")
                for heroe in heroes:
                    print(heroe)
                print("--------------")
        elif opcion == "O":
            lista_de_tipos_set = obtener_lista_de_tipos(lista_personajes, "inteligencia")
            diccionario_heroes_por_inteligencia = obtener_heroes_por_tipo(lista_personajes, lista_de_tipos_set, "inteligencia")
            for inteligencia, heroes in diccionario_heroes_por_inteligencia.items():
                print(f"Nivel inteligencia: {inteligencia}")
                for heroe in heroes:
                    print(heroe)
                print("--------------")
        elif opcion == "Z":
            break
        else:
            imprimir_dato("Opción inválida")

'''1.4'''
def leer_archivo(nombre_archivo: str) -> list:
    #Lee el contenido de un archivo y lo devuelve como una lista.
    archivo = open(nombre_archivo, "r")
    diccionario = json.load(archivo)
    archivo.close()
    return diccionario["heroes"]


'''1.5'''
def guardar_archivo(nombre_archivo: str, contenido: str) -> bool:
    #Recibe un string que sera el nombre del archivo y guarda el archivo junto con  su extension ejemplo .csv
    try:
        archivo = open(nombre_archivo, "w+")
        archivo.write(contenido)
        archivo.close()
        return True
    except:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False

'''1.6'''
def capitalizar_palabras(frase: str) -> str:
    #La función capitalizar_palabras toma una cadena como entrada y capitaliza la primera letra de cada palabra en la cadena
    palabras = frase.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return ' '.join(palabras_capitalizadas)

'''1.7'''
def obtener_nombre_capitalizado(heroe: dict) -> str:
    #La función  obtener_nombre_capitalizado  toma como entrada un diccionario que representa a un héroe y devuelve una cadena formateada con el nombre del héroe capitalizado.
    nombre = heroe["nombre"]
    nombre_formateado = capitalizar_palabras(nombre)
    return f"Nombre: {nombre_formateado}"

'''1.8'''
def obtener_nombre_y_dato(heroe: dict, clave: str) -> str:
    # La función  obtener_nombre_y_dato  toma como entrada un diccionario  heroe  y una cadena  clave .
    # Devuelve una cadena formateada que incluye el nombre del héroe capitalizado, la clave capitalizada y el valor correspondiente del diccionario.
    # Si la clave no está presente en el diccionario, devuelve una cadena que indica que los datos no están disponibles.
    nombre_formateado = obtener_nombre_capitalizado(heroe)
    if clave in heroe:
        dato = heroe[clave]
        return f"{nombre_formateado} | {clave.capitalize()}: {dato}"
    else:
        return f"{nombre_formateado} | {clave.capitalize()}: No disponible"

'''2.1'''
def es_genero(heroe: dict, genero: str) -> bool:
    #La función es_genero verifica si el género de un héroe dado coincide con un género especificado.
    if genero ==  heroe["genero"]:
        return True
    else:
        return False

'''2.2'''
def stark_guardar_heroe_genero(lista_heroes: list, genero: str) -> bool:
    # Esta función toma una lista de héroes y un género como entradas.
    # Busca los héroes en la lista que coinciden con el género dado y guarda sus nombres de manera formateada.
    # Luego, la función crea un archivo CSV con los nombres guardados y devuelve True si el archivo 
    # se guarda correctamente, de lo contrario devuelve False.
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
    #La función calcular_min calcula el valor mínimo de una clave dada en una lista de diccionarios.
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
    #Esta función calcula el valor mínimo de una clave específica para un género dado en una lista de personajes.
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
    #La función calcular_max calcula el valor máximo de una clave dada en una lista de diccionarios.
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
    #La función calcular_max calcula el valor máximo de una clave 
    # específica para un género dado en una lista de personajes.
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
def calcular_max_min_dato_genero(lista_personajes , genero: str, max_o_min: str, key: str) -> dict:
    #Esta función calcula el valor máximo o mínimo de una clave 
    # específica para un género dado en una lista de personajes. 
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
    #Esta función calcula, imprime y guarda información sobre un héroe 
    # de un género específico basado en un criterio dado.
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
def sumar_dato_heroe_genero(lista, clave, genero):
    #La función sumar_dato_heroe_genero calcula la suma de un atributo de datos específico 
    # para todos los héroes de un género dado en una lista de diccionarios.
    if not lista:
        print('La lista está vacía')
        return -1
    suma = 0
    for heroe in lista:
        if isinstance(heroe, dict) and heroe and heroe.get('genero') == genero:
            if clave in heroe:
                valor = heroe[clave]
                if isinstance(valor, int) or isinstance(valor, float):
                    suma += valor
                else:
                    print('El valor no es numérico')
    if suma > 0:
        return suma
    else:
        return -1
    
def dividir(divisor,dividendo):
    #Esta función toma dos números como entrada, un divisor y un dividendo.
    #  Verifica si el divisor no es igual a cero.
    #  Si no es cero, realiza la división y devuelve el resultado.
    #  De lo contrario, devuelve False.
    if(divisor != 0):
        div = divisor/dividendo
        return div
    else:
        return False

def imprimir_heroe(dato: dict, datodos: str):
    if 'nombre' in dato and datodos in dato:
        print('nombre:', dato['nombre'])
        print(datodos + ':', dato[datodos])
    else:
        print('No se encontró el nombre o el dato ingresado en el diccionario.')
def cantidad_heroes_genero(lista_heroes: list, genero: str) -> int:
    count = 0
    for heroe in lista_heroes:
        if heroe['genero'] == genero:
            count += 1
    return count

'''4.2'''
def calcular_promedio_genero(lista_heroes, key, genero):
    #La función calcular_promedio_genero calcula el valor promedio de un atributo
    #  específico (clave) para un género dado en una lista de héroes.
    suma = sumar_dato_heroe_genero(lista_heroes, key, genero)
    cantidad = cantidad_heroes_genero(lista_heroes, genero)
    if suma != -1 and cantidad != 0:
        promedio = dividir(suma, cantidad)
        return promedio
    else:
        return -1

'''4.4'''
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes: list, genero: str) -> bool:
    #La función calcular_promedio_genero calcula la altura promedio de los héroes según su género,
    #  imprime el resultado y lo guarda en un archivo.
    if len(lista_personajes) > 0:
        promedio = calcular_promedio_genero(lista_personajes, 'altura', genero)
        if promedio != 0:
            mensaje = f"Altura promedio género {genero}: {promedio}"
            imprimir_dato(mensaje)
            nombre_archivo = f"heroes_promedio_altura{genero}.csv" 
            contenido = mensaje
            guardar_archivo(nombre_archivo, contenido) 
            return mensaje
        else:
            imprimir_dato("Error: No se pudo calcular el promedio")
            return False
    else:
        imprimir_dato("Error: Lista de héroes vacía")
        return False

'''5.1'''
def calcular_cantidad_tipo(lista_heroes: list, tipo_dato: str) -> dict: 
    #Esta función calcula la cantidad de un tipo de dato específico en una lista de héroes.
    #  Devuelve un diccionario con los valores en mayúscula del tipo de dato como claves
    #  y el recuento correspondiente como valores.
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
    #La función guardar_cantidad_heroes_tipo toma como entrada un diccionario y una cadena de texto.
    #  Verifica si la entrada es un diccionario y, de ser así, itera sobre los pares clave-valor en el diccionario.
    #  Para cada par, agrega una cadena formateada a una variable de mensaje. Luego, crea un nombre de archivo basado en la cadena de texto de entrada y
    #  guarda el mensaje en un archivo utilizando la función guardar_archivo.
    #  Si el archivo se guarda correctamente, devuelve True; de lo contrario, devuelve False.
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
    #La función calcular_cantidad_tipo_datos calcula la cantidad de un tipo de dato específico en una lista de héroes y lo guarda en un archivo.
    cantidad_tipo = calcular_cantidad_tipo(lista_heroes, tipo_dato)
    if guardar_cantidad_heroes_tipo(cantidad_tipo, tipo_dato) == True:
        return True
    else:
        return False
        
    

'''6.1'''
def obtener_lista_de_tipos(lista_heroes: list, dato: str) -> set: 
    #La función obtener_lista_de_tipos toma una lista de héroes y un tipo de dato como entrada, y devuelve un conjunto de valores únicos para ese tipo de dato.
    lista_valores = []
    for heroe in lista_heroes:
        valor = heroe.get(dato, "")
        if not valor:
            valor = "N/A"
        lista_valores.append(valor)
    lista_valores = set([capitalizar_palabras(valor) for valor in lista_valores])
    return lista_valores

'''6.2'''
def normalizar_dato(dato: str, valor_default: str) -> str: 
    #La función normalizar_dato toma como entrada una cadena de texto llamada dato y un valor predeterminado llamado valor_default.
    #  Verifica si el dato está vacío o no. Si está vacío, devuelve el valor por defecto valor_default.
    #  De lo contrario, devuelve el valor del dato.
    if not dato:
        return valor_default
    else:
        return dato

'''6.3'''
def normalizar_heroe(heroe: dict, clave: str) -> dict:  
    #El siguiente código define una función llamada normalizar_heroe que toma como entrada un diccionario heroe y una cadena de texto clave.
    #  La función normaliza los valores de la clave especificada en el diccionario aplicando dos funciones auxiliares: normalizar_dato y capitalizar_palabras.
    #  También capitaliza el valor de la clave "nombre" si existe en el diccionario. Finalmente, la función devuelve el diccionario modificado.
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

'''6.4'''
def obtener_heroes_por_tipo(lista_heroes:list, conjunto_tipos:set, clave_a_evaluar:str)-> dict:
    # La funcion recibe una lista de heroes, un conjunto de variedades y una clave. Recorre sobre el conjunto de tipos 
    # y por cada tipo verifica si existe como clave en un diccionario. Si no existe, la agrega a una lista vacia con el valor.
    # Dentro de la iteración de tipos, itera la lista de héroes normalizando el valor de la clave evaluada. Luego, verifica si el valor 
    # normalizado coincide con el tipo actual. Si coincide, agrega el nombre del héroe a la lista correspondiente en el diccionario.
    # Retorna un diccionario con cada variedad como clave y una lista de nombres como valor. 

    diccionario_variedades = {}

    for tipo in conjunto_tipos:
        diccionario_variedades[tipo] = []

    for heroe in lista_heroes:
        if clave_a_evaluar in heroe:
            valor = normalizar_dato(heroe[clave_a_evaluar], "N/A").lower() 
            for tipo in conjunto_tipos:
                if valor == tipo.lower():
                    diccionario_variedades[tipo].append(heroe["nombre"])

    return diccionario_variedades

'''6.5'''
def guardar_heroes_por_tipo(diccionario_variedades, tipo_dato):
    #La función guardar_heroes_por_tipo toma como entrada un diccionario de héroes categorizados por un tipo de dato específico y un tipo de dato.
    #  Itera sobre el diccionario y verifica si hay héroes para cada tipo de dato.
    #  Si los hay, une los nombres de los héroes con un símbolo de tubería y agrega el tipo de dato, los héroes y los nombres a una cadena de mensaje
    # . Luego, crea un nombre de archivo basado en el tipo de dato y guarda la cadena de mensaje en un archivo CSV utilizando la función guardar_archivo.
    mensaje = ""
    for tipo, heroes in diccionario_variedades.items():
        if heroes:
            nombres = " | ".join(heroes)
            mensaje += f"{tipo_dato} {tipo}: {nombres}\n"
    nombre_archivo = f"heroessegun{tipo_dato}.csv"
    return guardar_archivo(nombre_archivo, mensaje)

'''6.6'''
def stark_listar_heroes_por_dato(lista_heroes, tipo_dato):
    #La función stark_listar_heroes_por_dato toma una lista de héroes y un tipo de dato como entradas. Luego, recupera la lista de tipos de datos únicos de la lista de héroes.
    #  A continuación, crea un diccionario donde las claves son los tipos de datos únicos y los valores son listas de héroes que tienen ese tipo de dato. Finalmente, devuelve el diccionario.
    tipos = obtener_lista_de_tipos(lista_heroes, tipo_dato)
    diccionario_variedades = obtener_heroes_por_tipo(lista_heroes, tipos, tipo_dato)
    return guardar_heroes_por_tipo(diccionario_variedades, tipos)
