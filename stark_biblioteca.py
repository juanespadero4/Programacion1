from data_stark import lista_personajes
import re
# 0. Crear la función 'stark_normalizar_datos()' la cual recibirá por parámetro la
# lista de héroes. La función deberá:
# ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
# las keys que representan datos numéricos) por ejemplo fuerza (int),
# altura (float), etc
# ● Validar primero que el tipo de dato no sea del tipo al cual será
# casteado. Por ejemplo si una key debería ser entero (ejemplo fuerza)
# verificar antes que no se encuentre ya en ese tipo de dato.
# ● Si al menos un dato fue modificado, la función deberá retornar el valor
# booleano True
# ● En caso de que la lista esté vacía o ya se hayan normalizado
# anteriormente los datos se deberá retornar el valor booleano False
# ● Crear una opción en el menú que me permita normalizar los datos (No
# se debería poder acceder a ninguna otra opción del menú hasta que
# los datos esten normalizados)
# ● En caso de que la llamada a la función retorne True mostrar un
# mensaje diciendo “Datos Normalizados” sino mostrar el mensaje
# “Hubo un error al normalizar los datos. Verifique que la lista no es

def stark_normalizar_datos(lista):
    respuesta = False
    for personaje in lista:
        for clave, valor in personaje.items():
            mensaje1 = "Datos Normalizados."
            mensaje2 = "Datos normalizados incorrectamente."
            if personaje[clave] == "":
                respuesta = mensaje2
            elif type(valor) == int or type(valor) == float:
                respuesta = mensaje2
            elif re.match(r'^[0-9]+.[0-9]+$', valor):
                personaje[clave] = float(valor)
                respuesta = True
            elif re.match(r'^[0-9]+$', valor):
                personaje[clave] = int(valor)
                respuesta = True
            
    return respuesta


# 1.1. Crear la función ”obtener_dato()” la cual recibirá por parámetro un
# diccionario el cual representara a un héroe y también recibirá un string que
# hace referencia a una “clave” del mismo
# Validar siempre que el diccionario no esté vacío y que el mismo tenga una key
# llamada “nombre”. Caso contrario la función retornara un False
# 1.2 Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el
# cual representara a un héroe y devolverá un string el cual contenga su nombre
# formateado de la siguiente manera:
# Nombre: Howard the Duck
# Validar siempre que el diccionario no este vacío y que la key que se pide exista. Caso
# contrario la función retornara un False


def obtener_dato(diccionario: dict, clave):
    if diccionario != {} and clave in diccionario:
        return diccionario[clave]
    else:
        return False

def obtener_nombre(diccionario: dict):
    nombre = obtener_dato(diccionario, "nombre")
    if nombre == False:
        print("ERROR")
    else:
        respuesta = nombre
    return respuesta

# 2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
# diccionario el cual representara a un héroe y una key (string) la cual
# representará el dato que se desea obtener.
# ● La función deberá devolver un string el cual contenga el nombre y dato
# (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
# CUALQUIER OTRO DATO.
# ● El string resultante debe estar formateado de la siguiente manera:
# (suponiendo que la key es fuerza)
# Nombre: Venom | fuerza: 500
# ● Validar siempre que la lista no este vacía. Caso contrario la función
# retornara un False

def obtener_nombre_y_dato(diccionario, clave):
    nombre = obtener_nombre(diccionario)
    dato = obtener_dato(diccionario, clave)
    if nombre is not False and dato is not False:
        print(f"Nombre: {nombre} | {clave}: {dato}")
    else:
        print("ERROR")
        return False


# 3.1 Crear la función “obtener_maximo()” la cual recibirá como parámetro una lista y
# una key (string) la cual representará el dato al cual se le debe calcular su cantidad
# MÁXIMA.
# ● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
# un int o un float. Caso contrario la función retornara un False
# ● En caso de que el dato que se está buscando en el diccionario es de tipo int o
# float retornar el mayor que haya encontrado en la búsqueda.
# 3.2 Crear la función “obtener_minimo()” la cual recibirá como parámetro una lista y
# una key (string) la cual representará el dato al cual se le debe calcular su cantidad
# MÍNIMA.
# ● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
# un int o un float. Caso contrario la función retornara un False
# ● En caso de que el dato que se está buscando en el diccionario es de tipo int o
# float retornar el menor que haya encontrado en la búsqueda.
# 3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:
# ● La lista de héroes
# ● Un número que me indique el valor a buscar (puede ser la altura
# máxima, la altura mínima o cualquier otro dato)
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# La función deberá retornar una lista con el héroe o los heroes que cumplan
# con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y
# 3.2
# Ejemplo de llamada:
# mayor_altura = obtener_maximo(lista_heroes,”altura”)
# lista_heroes_max_altura = 'obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)
# El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura
# correspondiente a la altura máxima, y la misma función me podria servir tanto como
# para altura menor, como la mayor o alguna altura que yo le especifique también.
# 3.4 Crear la función 'stark_imprimir_heroes' la cual recibirá un parametro:
# ● La lista de héroes
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
# contrario no hará nada y retornara False
# En caso de que la lista no este vacia imprimir la información completa de
# todos los heroes de la lista que se le pase
# Ejemplo de llamada:
# mas_pesado = obtener_maximo(lista_heroes,”peso”)
# lista_mas_pesados = 'obtener_dato_cantidad(lista_heroes,mas_pesado ,”peso”)
# stark_imprimir_heroes(lista_mas_pesados) -> Imprimo sólo los héroes más pesados
# stark_imprimir_heroes(lista_heroes) -> Imprimo todos los héroes

def obtener_maximo(lista, clave):
    if not lista:
        print("ERROR: La lista está vacía")
        return
    maximo = 0 
    identidad_maximo = None
    for personaje in lista:
        if type(personaje[clave]) != int and type(personaje[clave]) != float:
            print("ERROR: La clave no es un número (int o float)")
            return
        valor = personaje.get(clave, None)
        if isinstance(valor, (int, float)):
            if valor > maximo:
                maximo = valor
                identidad_maximo = personaje.get("nombre", None)
    if identidad_maximo is not None:
        print(f"El personaje {identidad_maximo} tiene el mayor valor de '{clave}': {maximo}")
    else:
        print("No se encontró ningún valor válido.")

stark_normalizar_datos(lista_personajes)
obtener_maximo(lista_personajes, "altura")
