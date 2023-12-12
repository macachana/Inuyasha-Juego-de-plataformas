import pygame
from Modulos.ClassPersonaje import Personaje
from Configuraciones.sonidos import recoger_item_normal
# from Configuraciones.sonidos import *
class item:
    def __init__(self,x,y,path,especial=False,item_vidas = False,item_espada = False,item_final = False):
        self.imagen = pygame.image.load(path)
        self.superficie = pygame.transform.scale(self.imagen,(50,50))
        self.rectangulo_principal = self.superficie.get_rect()
        self.rectangulo_principal.y = y
        self.rectangulo_principal.x = x
        self.especial = especial
        self.capturado = False
        self.tiempo_item_temp = 100000
        self.tiempo_actual_item_temp = 0
        self.item_vidas = item_vidas
        self.item_espada = item_espada
        self.item_final = item_final
        self.nivel_terminado = False
        #creo la siguiente variable para que me indique cuando el beneficio
        #del item especial esta disponibles y cuando no
        self.ben = False

    def obtener_top_cuadrado(self):
        # Definir un rectángulo que representa el "top" de la plataforma
        top_rect = pygame.Rect(self.rectangulo_principal.x +10, self.rectangulo_principal.y, self.rectangulo_principal.width - 10, 10)
        return top_rect

    def obtener_bottom_cuadrado(self):
        # Definir un rectángulo que representa el "bottom" de la plataforma
        bottom_rect = pygame.Rect(self.rectangulo_principal.x +10,self.rectangulo_principal.bottom - 10, self.rectangulo_principal.width - 10, 10)
        return bottom_rect

    def obtener_right_cuadrado(self):
        # Definir un rectángulo que representa el "left" de la plataforma
        left_rect = pygame.Rect(self.rectangulo_principal.x, self.rectangulo_principal.y, 10, self.rectangulo_principal.height)
        return left_rect
    
    def obtener_left_cuadrado(self):
        # Definir un rectángulo que representa el "rigth" de la plataforma
        right_rect = pygame.Rect(self.rectangulo_principal.right - 10, self.rectangulo_principal.y, 10, self.rectangulo_principal.height)
        return right_rect

    def actualizar(self,pantalla,personaje:Personaje):
        tiempo_actual = pygame.time.get_ticks()
        self.colision_con_personaje(personaje)
        if self.especial == False:
            if self.capturado == False:
                pantalla.blit(self.superficie,self.rectangulo_principal)

            if self.item_final and self.capturado == False:
                pantalla.blit(self.superficie,self.rectangulo_principal)
            else:
                self.nivel_terminado = True

        else:
            if self.capturado == False:
                if tiempo_actual < self.tiempo_actual_item_temp + self.tiempo_item_temp:
                    pantalla.blit(self.superficie,self.rectangulo_principal)
                    self.ben = True
                else:
                    self.ben = False
            else:
                if self.item_vidas == True and self.ben == True :
                    if personaje.vidas < 3:
                        personaje.vidas +=1
                        pygame.time.set_timer(pygame.USEREVENT + 3,10,1)
                        self.ben = True
                    else:
                        self.ben = False

                if self.item_espada and self.ben == True:
                    pygame.time.set_timer(pygame.USEREVENT + 4,10000,1)
                    personaje.habilidad_especial_espada = True
                    self.ben = True

    def colision_con_personaje(self,personaje:Personaje):
        if self.rectangulo_principal.colliderect(personaje.rectangulo_principal):
            self.capturado = True
    



