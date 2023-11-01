from data_stark import lista_personajes
import re

#_______________________________________________________________________________________________________________________________________________________________________

def extraer_iniciales(nombre_personaje: str) -> str:
    '''Extrae las iniciales de cada palabra que conforma el nombre del personaje y las pone seguidas por un punto, si no tiene nombre devuelve N/A'''
    nombre_sin_the = nombre_personaje.replace("the", "").replace("The", "")
    nombre_sin_guion = nombre_sin_the.replace("-", " ").replace("_", " ")
    palabras = nombre_sin_guion.split()
    if len(palabras) == 0:
        mensaje = "N/A"
        return mensaje
    else:
        iniciales = [palabra[0] + "." for palabra in palabras]
        resultado = "".join(iniciales)
        resultado = resultado.upper()
        return resultado

def definir_iniciales_nombre(heroe: dict) -> dict or bool:
    '''Agrega una nueva clave al diccionario con su nuevo valor sacado de la funcion extraer_iniciales.'''
    if isinstance(heroe, dict) and 'nombre' in heroe:
        nombre_personaje = heroe["nombre"]
        inicial_lista = extraer_iniciales(nombre_personaje)
        heroe["iniciales"] = inicial_lista
        return heroe
    else:
        return False

def agregar_iniciales_nombre(lista_personajes: list) -> bool:
    '''Itera la lista de personajes para poder asignarle a cada uno su clave con iniciales'''
    if not lista_personajes:
        return False
    else:
        for personaje in lista_personajes:
            iniciales = definir_iniciales_nombre(personaje)
            if iniciales == False:
                print("El origen de los datos no contiene el formato correcto")
            else:
                personaje.update(iniciales)
        return True

def stark_imprimir_nombres_con_iniciales(lista_personajes: list) -> str:
    '''se utiliza agregar_iniciales_nombre para añadir las iniciales a los diccionarios de la lista, e imprime la lista de los nombres con sus respectivas iniciales al lado'''
    agregar_iniciales_nombre(lista_personajes)
    if not lista_personajes:
        print("La lista está vacía, o no es un elemento del tipo 'lista'")
    else:
        mensajes = []
        for personaje in lista_personajes:
            mensaje = f"\n* {personaje['nombre']} ({personaje['iniciales']})"
            mensajes.append(mensaje)
        resultado = "\n".join(mensajes)
        return resultado + "\n"

def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    '''genera un id para el heroe, donde tambien se muestra su genero'''
    if not isinstance(id_heroe, int):
        return 'N/A'
    if genero_heroe not in ['M', 'F', 'NB']:
        return 'N/A'
    codigo_genero = genero_heroe + '-'
    codigo_id = str(id_heroe).zfill(8)
    codigo = codigo_genero + codigo_id
    return codigo

def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
    '''la funcion agrega una nueva clave llamada id_heroe, donde se agrega el codigo generado en generar_codigo_heroe'''
    if not heroe or not isinstance(heroe, dict):
        return False
    codigo_heroe = generar_codigo_heroe(id_heroe, heroe.get('genero', ''))
    if not codigo_heroe[-8:].isdigit():
        return False
    heroe['id_heroe'] = codigo_heroe
    return True

def stark_generar_codigos_heroes(lista_personajes: list) -> None:
    '''Itera la lista de los personajes y le asigna a cada uno su codigo.'''
    if not lista_personajes or not all(isinstance(heroe, dict) and 'genero' in heroe for heroe in lista_personajes):
        print("El origen de datos no contiene el formato correcto.")
        return
    for indice, personaje in enumerate(lista_personajes):
        if personaje["genero"] == "M":
            agregar_codigo_heroe(personaje, indice+1)
        elif personaje["genero"] == "F":
            agregar_codigo_heroe(personaje, indice+1)
        elif personaje["genero"] == "NB":
            agregar_codigo_heroe(personaje, indice+1)
    print(f"\nSe asignaron {len(lista_personajes)} códigos.")
    print(f"El código del primer héroe es: {lista_personajes[0]['id_heroe']}")
    print(f"El código del último héroe es: {lista_personajes[-1]['id_heroe']}\n")

def sanitizar_entero(numero_str: str) -> int or bool:
    '''analiza el string recibido para saber si tiene dentro un entero positivo, caso contrario retorna -1, -2, -3'''
    numero_str = numero_str.strip()
    if numero_str.startswith('-') and numero_str[1:].isdigit():
        return -2
    if not numero_str.isdigit():
        return -1
    if numero_str.isdigit():
        numero = int(numero_str)
        return numero
    else:
        return -3


def sanitizar_flotante(numero_str: str) -> float or bool:
    '''analiza el string recibido para saber si tiene dentro un flotante positivo, caso contrario retorna -1, -2, -3'''
    numero_str = numero_str.strip()
    flotante = r'^[-+]?[0-9]+(\.[0-9]+)?$'
    if numero_str.startswith('-') and re.match(flotante, numero_str):
        return -2
    if re.match(flotante, numero_str):
        numero = float(numero_str)
        return numero
    if not numero_str.isdigit():
        return -1
    else:
        return -3


def sanitizar_string(valor_str: str, valor_por_defecto: str) -> str:
    '''analiza el string para saber si sus caracteres son solo texto, en caso de ser otra cosa o contener numeros retorna N/A'''
    str_txt = r'^[a-zA-Z\s]+$'
    num = r'\d+'
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()
    valor_str_signo = valor_str.replace("/", "")
    if re.match(str_txt, valor_str_signo):
        txt_min = valor_str_signo.lower()
        return txt_min
    elif re.findall(num, valor_str):
        return "N/A"
    elif valor_str == "":
        return valor_por_defecto.lower()


def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str) -> bool:
    '''sanitiza en el diccionario del heroe asignado, el valor de la clave asignada segundo el tipo de dato que se le da'''
    tipo_dato = tipo_dato.lower()
    if tipo_dato not in ['string', 'entero', 'flotante']:
        print('Tipo de dato no reconocido')
        return False
    if clave.lower() not in heroe:
        print('La clave especificada no existe en el heroe')
        return False
    if tipo_dato == 'string':
        heroe[clave] = sanitizar_string(heroe[clave], "MAL")
        return True
    elif tipo_dato == 'entero':
        heroe[clave] = sanitizar_entero(heroe[clave])
        return True
    elif tipo_dato == 'flotante':
        heroe[clave] = sanitizar_flotante(heroe[clave])
        return True


def stark_normalizar_datos(lista_personajes: list) -> str:
    '''sanitiza todos los datos que pueden llegar a estar mal pra las validaciones en la lista.'''
    if not lista_personajes:
        return "ERROR: La lista está vacía"
    else:
        for personaje in lista_personajes:
            sanitizar_dato(personaje, "altura", "flotante")
            sanitizar_dato(personaje, "peso", "flotante")
            sanitizar_dato(personaje, "color_ojos", "string")
            sanitizar_dato(personaje, "color_pelo", "string")
            sanitizar_dato(personaje, "fuerza", "entero")
            sanitizar_dato(personaje, "inteligencia", "string")
        return "DATOS NORMALIZADOS."


def generar_indice_nombres(lista_personajes: list) -> list or str:
    '''itera la lista para separar palabra por palabra los nombres de los personajes'''
    lista_indice = []
    for personaje in lista_personajes:
        if not isinstance(personaje, dict) or "nombre" not in personaje:
            return "El origen de los datos no contiene el formato correcto"
        else:
            lista_indice.extend(personaje["nombre"].split())
    return lista_indice


def stark_imprimir_indice_nombre(lista_personajes: list) -> None:
    '''muestra el indice generado por la funcion, con todos los nombres separados por un -'''
    nombres = generar_indice_nombres(lista_personajes)
    if nombres:
        indice_nombre = '-'.join(nombres)
        print(f"\n{indice_nombre}\n")

def convertir_cm_a_mtrs(valor_cm: float)->bool:
    '''convierte el valor asignado a valor_cm, en un float. Simulando que pasa de centimentro a metros.'''
    flotante = r'^[-]?[0-9]+(\.[0-9]+)?$'
    valor_cm_str = str(valor_cm)
    if valor_cm_str.startswith('-') and re.match(flotante, valor_cm_str):
        return -1
    elif re.match(flotante, valor_cm_str):
        numero = float(valor_cm_str)
        numero_a_mts = numero/100
        return numero_a_mts
    
def generar_separador(patron: str, largo: int, imprimir=True)->bool:
    '''crea un separador del largo requerido y del patron que guste'''
    if len(patron) < 1 or len(patron) > 2:
        return 'N/A'
    if not isinstance(largo, int) or largo < 1 or largo > 235:
        return 'N/A'
    separador = patron * largo
    if imprimir:
        print(separador) 
    return separador

def generar_encabezado(titulo: str)->str:
    '''Devuelve un string que contiene el titulo asignado, separado por dos separadores'''
    print(generar_separador("*", 195, False))
    print(f"\n{titulo}\n")
    print(generar_separador("*", 195, False))

def imprimir_ficha_heroe(heroe: dict)->str:
    '''imprime la ficha del heroe asignado'''
    generar_encabezado("PRINCIPAL")
    print(f"NOMBRE DEL HEROE:                           {heroe['nombre']}({heroe['iniciales']})\n")
    print(f"IDENTIDAD SECRETA:                          {heroe['identidad']}\n")
    print(f"CONSULTORA:                                 {heroe['empresa']}\n")
    print(f"CODIGO DE HEROE:                            {heroe['id_heroe']}\n")
    generar_encabezado("FISICO")
    print(f"ALTURA:                                     {convertir_cm_a_mtrs(heroe['altura'])} Mtrs.\n")
    print(f"PESO:                                       {heroe['peso']} Kg.\n")
    print(f"FUERZA                                      {heroe['fuerza']} N\n")
    generar_encabezado("SEÑAS PARTICULARES")
    print(f"COLOR DE OJOS:                              {heroe['color_ojos']}\n")
    print(f"COLOR DE PELO:                              {heroe['color_pelo']}\n")

def stark_navegar_fichas(lista_personajes:list):
    '''Permite navegar a traves de las fichas de os personajes, pudiendo ir de izquierda a derecha, la otra opcion es salir'''
    posicion_lista = 0
    salir = False
    while not salir:
        personaje_actual = lista_personajes[posicion_lista]
        imprimir_ficha_heroe(personaje_actual)
        opcion = input("\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir\n")
        if opcion == '1':
            posicion_lista = (posicion_lista - 1) % len(lista_personajes)
        elif opcion == '2':
            posicion_lista = (posicion_lista + 1) % len(lista_personajes)
        elif opcion.upper() == 'S':
            salir = True
        else:
            print("Opcion invalida. Por favor, ingrese uno de los 3 numeros mostrados en pantalla")
        

def imprimir_menu():
    '''Imprime el menu y sus opciones'''
    print("Bienvenido al Menu Stark, por favor ingrese el numero de una de las opciones a continuacion:")
    print("(1) Imprimir la lista de nombres junto con sus iniciales")
    print("(2) Generar códigos de héroes")
    print("(3) Normalizar datos")
    print("(4) Imprimir índice de nombres")
    print("(5) Navegar fichas")
    print("(6) Salir.")
        
def stark_menu_principal():
    '''Imprime el menu y nos da la opcion de poner un numero'''
    imprimir_menu()
    opcion = int(input("Opcion elegida: "))
    return opcion

def stark_marvel_app3(lista_personajes: list):
    flag = True
    while flag:
        opcion = stark_menu_principal()
        match opcion:
            case 1:
                print(stark_imprimir_nombres_con_iniciales(lista_personajes))
            case 2:
                stark_generar_codigos_heroes(lista_personajes)
            case 3:
                print(f"\n{stark_normalizar_datos(lista_personajes)}\n")
            case 4:
                stark_imprimir_indice_nombre(lista_personajes)
            case 5:
                stark_navegar_fichas(lista_personajes)
            case 6:
                print("Eligio salir. Hasta la proxima!")
                break


