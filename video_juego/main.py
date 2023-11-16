import pygame
import sqlite3
from pygame.locals import *

pygame.init()

ANCHO, ALTO = 1200, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('WAR MACHINE')

fuente_titulo = pygame.font.Font("video_juego/fuente/Wargate-Normal.otf", 72)
fuente_normal = pygame.font.Font("video_juego/fuente/Wargate-Normal.otf", 36)

fondo_menu = pygame.image.load("video_juego/imagenes/fondo_menu/the_sky_ruler_by_lhlclllx97_dcwycr9.jpg").convert()
salir_img = pygame.image.load("video_juego/imagenes/fondo_menu/pngegg (1).png").convert_alpha()
salir_img = pygame.transform.scale(salir_img, (40, 40))

fondo = pygame.transform.scale(fondo_menu, (1200, 800))

reloj = pygame.time.Clock()
BLANCO = (255, 255, 255)
GRIS_OSCURO = (128, 128, 128)
NEGRO = (0, 0, 0)

nombre_jugador = ''
rectangulo_entrada = pygame.Rect(ANCHO // 2 - 150, ALTO // 2 - 25, 300, 50)

def dibujar_texto(texto, fuente, color, x, y, centrado=False):
    img = fuente.render(texto, True, color)
    if centrado:
        x -= img.get_width() // 2
    ventana.blit(img, (x, y))

def crear_tabla():
    conexion = sqlite3.connect('data_base.db')
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS nombres (nombre TEXT)")
    conexion.commit()
    conexion.close()

def guardar_nombre(nombre):
    conexion = sqlite3.connect('data_base.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO nombres (nombre) VALUES (?)", (nombre,))
    conexion.commit()
    conexion.close()

def mostrar_pantalla_negra():
    ventana.fill(NEGRO)
    pygame.display.flip()
    pygame.time.wait(2000)  # Espera 2 segundos antes de salir

crear_tabla()

ejecutando = True
while ejecutando:
    ventana.blit(fondo, (0, 0))
    dibujar_texto('WAR MACHINE', fuente_titulo, BLANCO, ANCHO // 2, 100, centrado=True)
    dibujar_texto('Ingrese su nombre\npara jugar:', fuente_normal, BLANCO, ANCHO // 2, 300, centrado=True)
    pygame.draw.rect(ventana, GRIS_OSCURO, rectangulo_entrada)
    pygame.draw.rect(ventana, BLANCO, rectangulo_entrada, 2)
    dibujar_texto(nombre_jugador[:10], fuente_normal, BLANCO, rectangulo_entrada.x + 10, rectangulo_entrada.y + 10)
    ventana.blit(salir_img, (ANCHO - salir_img.get_width(), 0))
    pygame.display.flip()
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            ejecutando = False
        elif evento.type == KEYDOWN:
            if evento.key == K_BACKSPACE:
                nombre_jugador = nombre_jugador[:-1]
            elif evento.key == K_RETURN:
                guardar_nombre(nombre_jugador)
                mostrar_pantalla_negra()
                ejecutando = False
            elif len(nombre_jugador) < 10:
                nombre_jugador += evento.unicode
        elif evento.type == MOUSEBUTTONDOWN:
            if salir_img.get_rect(x=ANCHO - salir_img.get_width(), y=0).collidepoint(evento.pos):
                ejecutando = False

pygame.quit()