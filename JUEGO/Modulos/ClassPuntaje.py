import pygame
from pygame import *
pygame.font.get_fonts()
from Modulos.ClassItem import item
from Configuraciones.colores_y_fonts import *
class Puntaje:
    def __init__(self,x,y,w,h,color,font,lista_items,pantalla,color_letra):
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.puntaje_actual = 0
        self.color = color
        self.font = font
        self.color_letra = color_letra
        self.obtener_puntos(lista_items,pantalla)

    def actualizar(self,pantalla):
        rect = Rect(self.x,self.y,self.width,self.height)
        self.boton_cuadrado(pantalla,rect,str(self.puntaje_actual),self.font,self.color,self.color_letra) 

    def obtener_puntos(self,lista_items:list["item"],pantalla):
        for i in lista_items:
            if i.capturado == True and i.especial == False:
                if i.item_final:
                    self.puntaje_actual +=100
                else:
                    self.puntaje_actual += 30
                    
            elif i.capturado == True and i.especial == True:
                self.puntaje_actual += 60
        self.actualizar(pantalla)

    def boton_cuadrado(self,pantalla,rect,palabra,font,color,color_letra):
        draw.rect(pantalla,color,rect,0,10)
        texto = font.render(palabra,True,color_letra)
        pantalla.blit(texto,(rect.x +(rect.width-texto.get_width())/2,
                        rect.y+(rect.height-texto.get_height())/2))

    def get_puntaje(self):
        return self.puntaje_actual

    def set_puntaje(self,puntaje_nuevo):
        self.puntaje_actual = puntaje_nuevo