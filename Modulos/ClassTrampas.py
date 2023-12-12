import pygame
from pygame import *
from Configuraciones.config import *
from Modulos.ClassPersonaje import Personaje



class Trampas:
    def __init__(self,x,y,tamano,pantalla,animacion,movil=False,punto_inicio = None, punto_final = None,velocidad = 3,arriba_y_abajo=False):
        self.animacion_actual = animacion
        reescalar_imagenes_lista(self.animacion_actual,*tamano)
        self.rectangulo_principal = self.animacion_actual[0].get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.pantalla = pantalla
        self.movil = movil
        self.punto_inicio = punto_inicio 
        self.punto_final = punto_final
        self.speed = velocidad
        self.arriba_y_abajo = arriba_y_abajo

        self.contador_pasos = 0
        self.mini_cuadrados = {}

        self.mini_cuadrados["bottom"] = self.obtener_bottom_cuadrado()
        self.mini_cuadrados["top"] = self.obtener_top_cuadrado()
        self.mini_cuadrados["left"] = self.obtener_left_cuadrado()
        self.mini_cuadrados["right"] = self.obtener_right_cuadrado()

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
        right_rect = pygame.Rect(self.rectangulo_principal.right - 10, self.rectangulo_principal.y, 10, self.rectangulo_principal.height)
        return right_rect
    
    def obtener_left_cuadrado(self):
        # Definir un rectángulo que representa el "rigth" de la plataforma
        left_rect = pygame.Rect(self.rectangulo_principal.x, self.rectangulo_principal.y, 10, self.rectangulo_principal.height)
        return left_rect

    def actualizar_mini_cuadrados(self):
        if self.movil:
            if self.arriba_y_abajo:
                self.rectangulo_principal.y += self.speed
                if self.rectangulo_principal.bottom > self.punto_final or self.rectangulo_principal.top < self.punto_inicio:
                    self.speed = -self.speed
            else:
                self.rectangulo_principal.x += self.speed

                if self.rectangulo_principal.right > self.punto_final or self.rectangulo_principal.left < self.punto_inicio:
                    self.speed = -self.speed
            
            if self.arriba_y_abajo:
                for key in self.mini_cuadrados:
                    mini_cuadrado = self.mini_cuadrados[key]
                    if key == "bottom":
                        mini_cuadrado.y += self.speed
                    elif key == "top":
                        mini_cuadrado.y += self.speed
                    elif key == "left":
                        mini_cuadrado.y += self.speed
                    elif key == "right":
                        mini_cuadrado.y += self.speed
            else:
                for key in self.mini_cuadrados:
                    mini_cuadrado = self.mini_cuadrados[key]
                    if key == "bottom":
                        mini_cuadrado.x += self.speed
                    elif key == "top":
                        mini_cuadrado.x += self.speed
                    elif key == "left":
                        mini_cuadrado.x += self.speed
                    elif key == "right":
                        mini_cuadrado.x += self.speed        
        
    def actualizar(self,pantalla,personaje:Personaje):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(self.animacion_actual[self.contador_pasos],self.rectangulo_principal)
        self.colision_con_personaje(personaje,pantalla)
        self.contador_pasos += 1
        if self.movil:
            self.actualizar_mini_cuadrados()


    def colision_con_personaje(self,personaje:Personaje,pantalla):
        if personaje.rectangulo_principal.colliderect(self.rectangulo_principal):
            if personaje.vulnerabilidad == False:
                personaje.vidas -=1
                personaje.animacion_actual = personaje.animaciones["danado"]
                personaje.animar(pantalla)
                pygame.time.set_timer(pygame.USEREVENT,3000,1)
                personaje.vulnerabilidad = True