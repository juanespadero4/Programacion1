from data_stark import lista_personajes

# A
def recorrido_lista_nb (lista):
    '''Recorre la lista en busqueda de personajes de genero no binario.'''
    contador_nb = 0
    for personaje in lista:
        if personaje ["genero"] == "NB":
            contador_nb +=1
            print(f"El personaje {personaje['nombre']} es de genero NB")
    if contador_nb == 0:
        print("No hay personajes de genero NB")


# B + C
def mas_alto_genero (lista, genero):
    '''Se busca en la lista de personajes el que posea mas altura, dependiendo del genero asignado'''
    maximo_altura = 0
    identidad_maximo_altura = None
    for personaje in lista:
        if personaje["genero"] == genero and float(personaje ["altura"]) > maximo_altura:
            maximo_altura = float(personaje ["altura"])
            identidad_maximo_altura = personaje["identidad"]
    print(f"El personaje mas alto de genero {genero} es {identidad_maximo_altura} midiendo {maximo_altura}")

# D + E
def mas_debil_genero(lista, genero):
    '''Recorre la lista en busqueda del personaje mas debil segun el genero asignado.'''
    minimo_fuerza = 999999 
    identidad_minimo_fuerza = None
    for personaje in lista:
        if personaje["genero"] == genero and int(personaje["fuerza"]) < minimo_fuerza:
            minimo_fuerza = int(personaje["fuerza"])
            identidad_minimo_fuerza = personaje["nombre"]
    
    if identidad_minimo_fuerza is not None:
        print(f"El personaje más débil de género {genero} es {identidad_minimo_fuerza}.")
    else:
        print(f"No se encontraron personajes de genero {genero}.")

#F
def promedio_fuerza_nb(lista):
    acumulador_fuerza_nb = 0
    cantidad_super_nb = 0
    for personaje in lista:
        if personaje["genero"] == "NB":
            cantidad_super_nb +=1
            acumulador_fuerza_nb += int(personaje["fuerza"])
    cuenta_promedio = acumulador_fuerza_nb / cantidad_super_nb
    mensaje = print(f"El promedio de fuerza de los personajes de genero NB es de {cuenta_promedio}")
    return mensaje
