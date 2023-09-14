from data_stark import lista_personajes

# A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe

# def imprimir_datos_personaje(personaje):
#     print(f"Nombre: {personaje['nombre']}")
#     print(f"Identidad: {personaje['identidad']}")
#     print(f"Empresa: {personaje['empresa']}")
#     print(f"Altura: {personaje['altura']} cm")
#     print(f"Peso: {personaje['peso']} kg")
#     print(f"Género: {personaje['genero']}")
#     print(f"Color de ojos: {personaje['color_ojos']}")
#     print(f"Color de pelo: {personaje['color_pelo']}")
#     print(f"Fuerza: {personaje['fuerza']}")
#     print(f"Inteligencia: {personaje['inteligencia']}")
#     print()  # Línea en blanco para separar cada personaje

# for personaje in lista_personajes:
#     imprimir_datos_personaje(personaje)

# B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
# fuerza (MÁXIMO)

# maximo_peso = 0
# identidad_maximo_peso = None
# for personaje in lista_personajes:
#     peso_actual = float(personaje["peso"])

#     if maximo_peso < peso_actual:
#         maximo_peso = peso_actual
#         identidad_maximo_peso = personaje["identidad"]
        
# print(f"El personaje de identidad {identidad_maximo_peso} tiene el mayor peso, que es de {maximo_peso} kg.")

# C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
# (MÍNIMO)

# minimo_altura = 0
# identidad_minimo_altura = None
# for personaje in lista_personajes:
#     altura_actual = float(personaje["altura"])

#     if minimo_altura < altura_actual:
#         minimo_altura = altura_actual
#         identidad_minimo_altura = personaje["identidad"]
        
# print(f"El personaje de identidad {identidad_minimo_altura} tiene el mayor altura, que es de {minimo_altura} cm.")

# D. Recorrer la lista y determinar el peso promedio de los superhéroes
# masculinos (PROMEDIO)

# listalen = len(lista_personajes)
# suma_peso = 0
# cantidad_masculinos = 0
# for personaje in lista_personajes:
#     if personaje["genero"] == "M":
#         suma_peso +=float(personaje["peso"])
#         cantidad_masculinos +=1
#     promedio_peso_masculino = suma_peso / cantidad_masculinos
# print(f"El promedio de peso de los personajes masculinos es {promedio_peso_masculino} ")


# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
# género) los cuales su fuerza supere a la fuerza promedio de todas las
# superhéroes de género femenino
suma_fuerza_femenino = 0
cantidad_femenino = 0
for personaje in lista_personajes:
    if personaje["genero"] == "F":
        suma_fuerza_femenino +=float(personaje["fuerza"])
        cantidad_femenino +=1
    promedio_fuerza_femenino = suma_fuerza_femenino / cantidad_femenino

    if float(personaje["fuerza"]) > promedio_fuerza_femenino:
        print("El nombre del personaje cuya fuerza es mayor al promedio de la fuerza de los personajes femeninos es ", personaje["nombre"], "y su pero es ", personaje["peso"])