import pygame
from pygame import *
class Vidas:
    def __init__(self,x,y,w,h,total_vidas):
        self.imagen = pygame.image.load(r"Imagenes_Sprites\items\vidas.png") 
        self.superficie = pygame.transform.scale(self.imagen,(w,h))
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.total_vidas = total_vidas



    def actualizar(self,pantalla,total_vidas):
        x = self.x
        for i in range(0,total_vidas):
            rect = Rect(x,self.y,self.width,self.height)
            pantalla.blit(self.superficie,rect)
            x+=(self.width+10)
            i+=1
        