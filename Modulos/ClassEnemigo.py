import pygame
from Configuraciones.config import *
import random
class Enemigo:
    def __init__(self,animaciones,x,y,tamaño_x,tamaño_y,comienzo = 0,terminacion=1300) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones,tamaño_x,tamaño_y)
        self.rectangulo_principal = self.animaciones["derecha"][0].get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        #banderas de los estados del enemigo
        self.esta_muerto = False
        self.muriendo = False

        #contador de pasos
        self.pasos = 0
        

        
        #inicializo los valores para la iniciacion de donde 
        #comienza a caminar el enemigo, y donde termina
        self.comienzo = comienzo
        self.terminacion = terminacion
        self.speed = random.randrange(1,5)
        self.direccion = False #false es igual a izquierda y true derecha
        


    def avanzar(self):
        if self.muriendo == False:           
            self.rectangulo_principal.x += self.speed
            if self.rectangulo_principal.right > self.terminacion or self.rectangulo_principal.left < self.comienzo:
                self.direccion = not self.direccion
                self.speed = -self.speed

        else:
            self.rectangulo_principal.y += 10


    def animar(self,pantalla):
        largo = len(self.animacion_actual)
        if self.pasos >= largo:
            self.pasos = 0

        pantalla.blit(self.animacion_actual[self.pasos],self.rectangulo_principal)
        self.pasos += 1
        #verificamos si esta o no muriendo, y que el contador de pasos sea igual al largo
        #que en este caso el largo de la animacion es 10.
        if self.muriendo and self.pasos == largo:
            self.esta_muerto = True

    
    def actualizar(self,pantalla):
        if self.esta_muerto == False:
            if self.direccion:
                self.animacion_actual = self.animaciones["izquierda"]
                self.animar(pantalla)
            else:
                self.animacion_actual = self.animaciones["derecha"]
                self.animar(pantalla)

            self.avanzar()
         
    
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


        