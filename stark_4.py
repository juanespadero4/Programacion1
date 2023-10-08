from data_stark import lista_personajes
import re


def stark_normalizar_datos(lista: list)->str:
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
#_______________________________________________________________________________________________________________________________________________________________________

def extraer_iniciales(nombre_personaje: str):
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

def definir_iniciales_nombre(heroe: dict):
    for personaje in heroe:
        if isinstance(heroe, dict) and 'nombre' in heroe:
            nombre_personaje = heroe["nombre"]
            inicial_lista = extraer_iniciales(nombre_personaje)
            heroe ["iniciales"] = inicial_lista
            return heroe
        else:
            return False

def agregar_iniciales_nombre(lista_personajes):
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
            
def stark_imprimir_nombres_con_iniciales(lista_personajes):
    agregar_iniciales_nombre(lista_personajes)
    if not lista_personajes:
        print("La lista esta vacia, o no es un elemento del tipo 'lista'")
    else:
        for personaje in lista_personajes:
            mensaje = f"* {personaje['nombre']} ({personaje['iniciales']})"
            print(mensaje)

def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    if not isinstance(id_heroe, int):
        return 'N/A'
    if genero_heroe not in ['M', 'F', 'NB']:
        return 'N/A'
    codigo_genero = genero_heroe + '-'
    codigo_id = str(id_heroe).zfill(10)
    codigo = codigo_genero + codigo_id
        
    return codigo

def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
    if not heroe or not isinstance(heroe, dict):
        return False
    
    codigo_heroe = generar_codigo_heroe(id_heroe, heroe.get('genero', ''))
    if not codigo_heroe[-10:].isdigit():
        return False
    
    heroe['codigo_heroe'] = codigo_heroe
    return True

