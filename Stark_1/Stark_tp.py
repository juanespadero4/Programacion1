#Juan Ignacio Espadero 1F

from data_stark import lista_personajes

while True:
    menu = int(input("""
    Seleccione cual de los siguientes datos quiere mostrar poniendo el numero asignado:
                
    (1) Datos de todos los superheroes.
    (2) Identidad y peso del personaje con mas fuerza.
    (3) Nombre e identidad del personaje mas bajo de altura.
    (4) Peso promedio masculinos
    (5) Nombre y peso de los que su fuerza supera el promedio de fuerza femenino.
    (6) Salir.
    """))

    match menu:
        case 1:
            for personaje in lista_personajes:
                print(f"Nombre: {personaje['nombre']}")
                print(f"Identidad: {personaje['identidad']}")
                print(f"Empresa: {personaje['empresa']}")
                print(f"Altura: {personaje['altura']} cm")
                print(f"Peso: {personaje['peso']} kg")
                print(f"Género: {personaje['genero']}")
                print(f"Color de ojos: {personaje['color_ojos']}")
                print(f"Color de pelo: {personaje['color_pelo']}")
                print(f"Fuerza: {personaje['fuerza']}")
                print(f"Inteligencia: {personaje['inteligencia']}")
                print()
        case 2:
            identidad_maximo_fuerza = []
            maximo_fuerza = 0
            identidad_maximo_fuerza = None
            for personaje in lista_personajes:
                fuerza_actual = float(personaje["fuerza"])
                if maximo_fuerza < fuerza_actual:
                    maximo_fuerza = fuerza_actual
                    identidad_maximo_fuerza = [personaje["identidad"]]
                elif maximo_fuerza == fuerza_actual:
                    identidad_maximo_fuerza.append(personaje["identidad"])

            if len(identidad_maximo_fuerza) > 1:
                print(f"Los personajes con la mayor fuerza son: {identidad_maximo_fuerza[0]}, {identidad_maximo_fuerza[1]}")
            else:
                print(f"El personaje con la mayor fuerza es: {identidad_maximo_fuerza[0]}")
        case 3:
            minimo_altura = 0
            identidad_minimo_altura = None
            for personaje in lista_personajes:
                altura_actual = float(personaje["altura"])

                if minimo_altura < altura_actual:
                    minimo_altura = altura_actual
                    identidad_minimo_altura = personaje["identidad"]
                    
            print(f"El personaje de identidad {identidad_minimo_altura} tiene el mayor altura, que es de {minimo_altura} cm.")
        case 4:
            suma_peso = 0
            cantidad_masculinos = 0
            for personaje in lista_personajes:
                if personaje["genero"] == "M":
                    suma_peso +=float(personaje["peso"])
                    cantidad_masculinos +=1
                promedio_peso_masculino = suma_peso / cantidad_masculinos
            print(f"El promedio de peso de los personajes masculinos es {promedio_peso_masculino} ")
        case 5:
            suma_fuerza_femenino = 0
            cantidad_femenino = 0
            promedio_fuerza_femenino = 0
            for personaje in lista_personajes:
                if personaje["genero"] == "F":
                    suma_fuerza_femenino +=float(personaje["fuerza"])
                    cantidad_femenino +=1
                    promedio_fuerza_femenino = suma_fuerza_femenino / cantidad_femenino

                if float(personaje["fuerza"]) > promedio_fuerza_femenino:
                    print("El nombre del personaje cuya fuerza es mayor al promedio de la fuerza de los personajes femeninos es", personaje["nombre"], "y su peso es", personaje["peso"])
        case 6:
            print("Usted salio del programa.")
            break