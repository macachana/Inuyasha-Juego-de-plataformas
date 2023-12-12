import pygame
import random
from Configuraciones.config import *
from Modulos.ClassPersonaje import Personaje
from Modulos.ClassPlataformas import Plataformas

class DisparoBoss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.lista_proyectil = [r"Imagenes_Sprites\proyectiles\2.png",r"Imagenes_Sprites\proyectiles\3.png",
                                r"Imagenes_Sprites\proyectiles\4.png",r"Imagenes_Sprites\proyectiles\5.png"]
        num_img = random.randrange(0,3)
        self.image = pygame.image.load(self.lista_proyectil[num_img])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W - self.rect.width)
        self.rect.y = 0
        self.speed = random.randrange(3,5) 

    def update(self,personaje:Personaje,lista_plataformas:list["Plataformas"]):
        self.rect.y += self.speed
        self.colision_con_personaje(personaje)
        self.colision_con_plataforma(lista_plataformas)
        if self.rect.y > H:
            self.kill()  # Eliminar proyectil cuando sale de la pantalla

    def colision_con_personaje(self,personaje:Personaje):
        if self.rect.colliderect(personaje.rectangulo_principal):
            self.kill()
            if personaje.vulnerabilidad == False:
                personaje.tiempo_ant_atacado = pygame.time.get_ticks()
                personaje.atacado = True
                personaje.vidas -=1
                pygame.time.set_timer(pygame.USEREVENT,3000,1)
                personaje.vulnerabilidad = True  

    def colision_con_plataforma(self,lista_plataformas:list["Plataformas"]):
        for plat in lista_plataformas:
            if self.rect.colliderect(plat.rectangulo_principal):
                self.kill()
