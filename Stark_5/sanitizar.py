import re
def sanitizar_entero(numero:str):
    '''
    La funcion recibira como parametro un numero en string, con el metodo strip se le suprimiran los espacios vacios, se verificara si el numero empieza con - es negativo y retornara -2, se utiliza una expresion regular para buscar un caracter que no sea digito en el numero y si lo encuentra retornara -1 y si ninguna de las condiciones anteriores se cumple retornara -3.
    '''
    numero = numero.strip()
    if numero.startswith('-'):
        return -2
    elif re.search(r'[^0-9]', numero):
        return -1
    elif re.match(r'^\d+$', numero):
        return int(numero)
    else:
        return -3    

def sanitizar_flotante(numero:str):
    '''
    La funcion recibira como parametro un numero float de tipo string, con el metodo strip suprimiremos los espacios en blanco, se verifica que el numero string empiece con - y si el numero es flotante, en caso de que lo sea retornara -2, si el numero es flotante positivo se parseara a float y retornara el numero parseado, si el string contiene algun caracter que no sea un digito, retornara -1, en caso de que ninguna de las condiciones se cumpla retornara -3.
    '''
    numero = numero.strip()
    flotante = r'^[-+]?[0-9]*\.?[0-9]+([-+]?[0-9]+)?$'
    if numero.startswith('-') and re.match(flotante,numero):
        return -2
    elif re.match(flotante,numero):
        numero = float(numero)
        return numero
    elif re.search(r'[^0-9]', numero):
        return -1
    else:
        return -3

def sanitizar_string(valorstr:str,valorpd:str):
    '''
    La funcion recibira como parametro dos strings, valorstr y valorpd, se verifica que el valorstr contenga solo caracteres alfabeticos y espacios, si lo son, se convertira en minusculas retornara el texto, si el valorstr contiene algun digito retornara N/A, y si es una cadena vacia retornara el valor por defecto.
    '''
    valorstr = valorstr.strip()
    valorpd = valorpd.strip()
    if re.match('[a-zA-Z\s]+',valorstr):
        valorstr.replace("/","\s")
        texto = valorstr.lower()
        return texto
    elif re.findall(r'\d+',valorstr):
        return "N/A"
    elif valorstr == "":
        return valorpd.lower()

def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):
    '''
    La funcion recibe como parametro un diccionario(heroe), una clave y un tipo de dato en string, se convierte el tipo de dato en minuscula, se verifica que el tipo de dato sea string,entero o flotante, si no lo es retorna false, se verifica que la clave existe en el diccionario, si no lo esta se imprime un mensaje de error y retornara false, luego se verifica que el tipo de dato es un string, se llama a la funcion sanitizar string y se sanitiza el valor del diccionario, en caso de que sea entero se usa la funcion sanitizar entero y el valor, lo mismo en el al ser un flotante, se usa la funcion sanitizar flotante y el valor, la funcion retornara true.
    '''
    tipo_dato = tipo_dato.lower()
    if tipo_dato not in ['string', 'entero', 'flotante']:
        print('Tipo de dato no reconocido')
        return False
    if clave not in heroe:
        print('La clave especificada no existe en el héroe')
        return False
    valor = heroe[clave]
    if tipo_dato == 'string':
        heroe[clave] = sanitizar_string(valor,"pordefecto")
    elif tipo_dato == 'entero':
        heroe[clave] = sanitizar_entero(valor)
    elif tipo_dato == 'flotante':
        heroe[clave] = sanitizar_flotante(valor)
    
    return True

def stark_normalizar_datos(lista:list):
    '''
    La funcion recibe como parametro una lista, se verifica que la lista no este vacia, si lo esta se retorna un mensaje de error, si no, se sanitizan los datos solicitados con la funcion sanitizar dato y retornara un mensaje exitoso.
    '''
    if not lista:
        return "Error lista de heroes"
    else:
        for item in lista:
            sanitizar_dato(item,'altura','flotante')
            sanitizar_dato(item,'peso','flotante')
            sanitizar_dato(item,'fuerza','entero')
            sanitizar_dato(item,'color_ojos','string')
            sanitizar_dato(item,'color_pelo','string')
            sanitizar_dato(item,'inteligencia','string')
        return print('Datos normalizados :)')
    
def dividir(numero1:int or float, numero2:int or float)->bool:
    '''Su proposito es dividir los dos numeros que se le asigne, numero1 es el dividendo y numero2 el divisor'''
    numero_final = 0
    if numero2 != 0:
        numero_final = numero1 / numero2
    return numero_final