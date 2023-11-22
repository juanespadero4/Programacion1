import pygame
import sys


#Personaje
quieto = pygame.image.load('imagenes/principal/idle1.png')

caminaDerecha = [pygame.image.load('imagenes/principal/run1.png'),
                 pygame.image.load('imagenes/principal/run2.png'),
                 pygame.image.load('imagenes/principal/run3.png'),
                 pygame.image.load('imagenes/principal/run4.png'),
                 pygame.image.load('imagenes/principal/run5.png'),
                 pygame.image.load('imagenes/principal/run6.png')]

caminaIzquierda = [pygame.image.load('imagenes/principal/run1-izq.png'),
                   pygame.image.load('imagenes/principal/run2-izq.png'),
                   pygame.image.load('imagenes/principal/run3-izq.png'),
                   pygame.image.load('imagenes/principal/run4-izq.png'),
                   pygame.image.load('imagenes/principal/run5-izq.png'),
                   pygame.image.load('imagenes/principal/run6-izq.png')]

salta = [pygame.image.load('imagenes/principal/jump1.png'),
         pygame.image.load('imagenes/principal/jump2.png')]


x=0
px = 50
py = 200
ancho = 40
velocidad = 10

#Control de FPS
reloj = pygame.time.Clock()

#Variables dirección
izquierda = False
derecha = False

#Pasos
cuentaPasos = 0

#Movimiento
def recargaPantalla():
    #Variables globales
    global cuentaPasos
    global x

    #Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5
    #Contador de pasos
    if cuentaPasos + 1 >= 6:
        cuentaPasos = 0
    #Movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

        # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    elif salto + 1 >= 2:
        PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True

#Bucle de acciones y controles
while ejecuta:
    #FPS
    reloj.tick(18)

    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    #Opción tecla pulsada
    keys = pygame.key.get_pressed()

    #Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    #Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

    #Personaje quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    #Tecla W - Moviemiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad

    #Tecla S - Moviemiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad
    #Tecla SPACE - Salto
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False

    # Control del audio
    #Baja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        PANTALLA.blit(sonido_abajo, (850, 25))
    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        PANTALLA.blit(sonido_mute, (850, 25))

    #Sube volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        PANTALLA.blit(sonido_arriba, (850, 25))
    elif keys [pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
            PANTALLA.blit(sonido_max, (850, 25))

    #Desactivar sonido
    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(sonido_mute, (850, 25))

    #Reactivar sonido
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(sonido_max, (850, 25))

    # Actualización de la ventana
    pygame.display.update()
    #Llamada a la función de actualización de la ventana
    recargaPantalla()

#Salida del juego
pygame.quit()