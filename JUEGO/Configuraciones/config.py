import pygame
from pygame import *
W,H = 1300,700
PANTALLA = pygame.display.set_mode((W,H))
FPS = 30

pygame.mixer.init()
sonido = pygame.mixer.Sound("Sonidos\OST_boton_click.mp3")

def boton_invisible_doble_color(screen,surface,x,y,color_antes,color_despues): 
    boton = Rect(x,y,surface.get_width(),surface.get_height()) 
    if boton.collidepoint(mouse.get_pos()):
        surface.set_alpha(100)
        surface.fill(color_despues)           # this fills the entire surface
        screen.blit(surface, (x,y))    # (0,0) are the top-left coordinates
    else:
        surface.set_alpha(10)
        surface.fill(color_antes)
        screen.blit(surface,(x,y))


def boton_cuadrado(screen:str,boton,palabra:str,font,color):
    draw.rect(screen,color,boton,0,10)
    texto = font.render(palabra,True,(0,0,0))
    screen.blit(texto,(boton.x+(boton.width-texto.get_width())/2,
                       boton.y+(boton.height-texto.get_height())/2))
    
def escalar_imagen_a_pantalla(imagen):
    imagen_cargada = pygame.image.load(imagen)
    imagen_escalada = pygame.transform.scale(imagen_cargada,(1300,700))
    return imagen_escalada

def reescalar_imagenes(diccionario_animaciones,ancho,alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img,(ancho,alto))

def reescalar_imagenes_lista(lista_animaciones,ancho,alto):
    for picture in range(len(lista_animaciones)):
        img = lista_animaciones[picture]
        lista_animaciones[picture] = pygame.transform.scale(img,(ancho,alto))


def invertir_imagen(lista:list)->list:
    lista_transformada = []
    for i in range(len(lista)):
        img = lista[i]
        lista_transformada.append(pygame.transform.flip(img,True,False))
    return lista_transformada

personaje_quieto_derecha = [pygame.image.load(r"Imagenes_Sprites\inuyasha\2.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\3.png")]

personaje_quieto_izquierda = invertir_imagen(personaje_quieto_derecha)

personaje_camina_derecha = [pygame.image.load(r"Imagenes_Sprites\inuyasha\13.png"),
                            pygame.image.load(r"Imagenes_Sprites\inuyasha\14.png"),
                            pygame.image.load(r"Imagenes_Sprites\inuyasha\15.png"),
                            pygame.image.load(r"Imagenes_Sprites\inuyasha\16.png"),
                            pygame.image.load(r"Imagenes_Sprites\inuyasha\17.png")]
personaje_camina_izquierda = invertir_imagen(personaje_camina_derecha)


### PERSONAJE NORMAL ###
#personaje salta para la izquierda y derecha
personaje_salta_derecha = [pygame.image.load(r"Imagenes_Sprites\inuyasha\6.png")]

personaje_salta_izquierda = invertir_imagen(personaje_salta_derecha)

#ataque con garras, cuerpo a cuerpo con el enemigo
personaje_ataca_derecha = [pygame.image.load(r"Imagenes_Sprites\inuyasha\43.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\44.png"),
                           pygame.image.load(r"Imagenes_Sprites\inuyasha\45.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\46.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\47.png")]
personaje_ataca_izquierda = invertir_imagen(personaje_ataca_derecha)

#ataque con espada especial,a distancia
personaje_ataque_especial_derecha = [pygame.image.load(r"Imagenes_Sprites\inuyasha\25.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\26.png"),
                                     pygame.image.load(r"Imagenes_Sprites\inuyasha\27.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\28.png"),
                                     pygame.image.load(r"Imagenes_Sprites\inuyasha\29.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\30.png")]
personaje_ataque_especial_izquierda = invertir_imagen(personaje_ataque_especial_derecha)


### PERSONAJE DAÑADO ###
personaje_danado = [pygame.image.load(r"Imagenes_Sprites\inuyasha\1_ataque.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\2_ataque.png")]

personaje_danado_izquierda = invertir_imagen(personaje_danado)

personaje_danado_camina = [pygame.image.load(r"Imagenes_Sprites\inuyasha\13_caminar1.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\14_caminar2.png"),
                           pygame.image.load(r"Imagenes_Sprites\inuyasha\15_caminar3.png"),pygame.image.load(r"Imagenes_Sprites\inuyasha\16_caminar4.png"),
                           pygame.image.load(r"Imagenes_Sprites\inuyasha\17_caminar5.png")]

personaje_danado_camina_izquierda = invertir_imagen(personaje_danado_camina)

personaje_danado_saltar = [pygame.image.load(r"Imagenes_Sprites\inuyasha\6_saltar1.png")]

personaje_danado_saltar_izquierda = invertir_imagen(personaje_danado_saltar)

### BOSS FINAL ###
boss_final_quieto = [pygame.image.load(r"Imagenes_Sprites\boss\0.png"),pygame.image.load(r"Imagenes_Sprites\boss\1.png"),
                     pygame.image.load(r"Imagenes_Sprites\boss\2.png")]

boss_final_quieto_izquierda = invertir_imagen(boss_final_quieto)

boss_final_salta = [pygame.image.load(r"Imagenes_Sprites\boss\12.png"),pygame.image.load(r"Imagenes_Sprites\boss\13.png")]

boss_final_salta_izquierda =  invertir_imagen(boss_final_salta)

# pygame.image.load(r"Imagenes_Sprites\boss\32.png"),pygame.image.load(r"Imagenes_Sprites\boss\29.png"),
#                     pygame.image.load(r"Imagenes_Sprites\boss\30.png"),pygame.image.load(r"Imagenes_Sprites\boss\31.png")
boss_final_ataca = [pygame.image.load(r"Imagenes_Sprites\boss\23.png")]

boss_final_ataca_izquierda = invertir_imagen(boss_final_ataca)

boss_final_atacado = [pygame.image.load(r"Imagenes_Sprites\boss\39.png")]

boss_final_atacado_izquierda = invertir_imagen(boss_final_atacado)

boss_final_muriendo = [pygame.image.load(r"Imagenes_Sprites\boss\40.png")]

boss_final_muriendo_izquierda = invertir_imagen(boss_final_muriendo)



#enemigo 1
enemigo_camina = [pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_1\0.png"),
                 pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_1\1.png"),
                 pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_1\2.png"),
                 pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_1\3.png")]

enemigo_camina_derecha = invertir_imagen(enemigo_camina)

enemigo_atacado = [pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_1\4.png"),
                   pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_1\5.png")]

#enemigo 2
enemigo_2_camina = [pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_2\4.png"),
                 pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_2\5.png"),
                 pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_2\6.png"),
                 pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_2\7.png"),
                 pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_2\8.png")]

enemigo_2_camina_derecha = invertir_imagen(enemigo_2_camina)

enemigo_2_atacado = [pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_2\10.png"),
                     pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_2\11.png"),
                     pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_2\12.png")]

#enemigo 3
enemigo_3_camina = [pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_3\0.png"),
                    pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_3\1.png"),
                    pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_3\2.png"),
                    pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_3\3.png"),
                    pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_3\4.png"),]

enemigo_3_camina_izquierda = invertir_imagen(enemigo_3_camina)

enemigo_3_atacado = [pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_3\7.png"),
                     pygame.image.load(r"Imagenes_Sprites\enemigos\enemigo_3\8.png")]

#TRAMPAS
trampa = [pygame.image.load(r"Imagenes_Sprites\trampas\0.png"),pygame.image.load(r"Imagenes_Sprites\trampas\1.png"),
          pygame.image.load(r"Imagenes_Sprites\trampas\2.png"),pygame.image.load(r"Imagenes_Sprites\trampas\3.png"),
          pygame.image.load(r"Imagenes_Sprites\trampas\4.png"),]


disparo_derecha = [pygame.image.load(r"Imagenes_Sprites\proyectiles\0.png"),pygame.image.load(r"Imagenes_Sprites\proyectiles\1.png")]

disparo_izquierda = invertir_imagen(disparo_derecha)