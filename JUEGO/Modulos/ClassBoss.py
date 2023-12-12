from Configuraciones.config import *
from Modulos.ClassVidas import Vidas
from Configuraciones.sonidos import *
from Configuraciones.colores_y_fonts import *
import random

from Modulos.ClassDisparoBoss import DisparoBoss
class Boss():
    def __init__(self,animaciones,x,y,tamaño,speed):
        self.tamaño = tamaño
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones,*tamaño)
        self.rectangulo = self.animaciones["Quieto_izquierda"][0].get_rect()
        self.animacion_actual = self.animaciones["Quieto_izquierda"]
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.speed = speed
        self.contador_pasos = 0
        self.vidas = 12
        self.vidas_class = Vidas(400,100,50,50,self.vidas)
        # Grupos de sprites
        self.proyectiles = pygame.sprite.Group()
        self.tiempo_vul = False
        self.tiempo_disparo = False
        self.atac = False
        self.muriendo = False

    def actualizar(self,pantalla,personaje,lista_plataformas):
        self.actualizar_vidas(pantalla)
        if  self.tiempo_disparo:
            self.animacion_actual = self.animaciones["ataque_especial_izquierda"]
        else:
            self.animacion_actual = self.animaciones["Quieto_izquierda"]
        if self.atac:
            self.animacion_actual = self.animaciones["atacado_izquierda"]
            self.atac = False
        if self.muriendo:
            self.animacion_actual = self.animaciones["muriendo_izquierda"]
            self.rectangulo.y += 100
        self.animar(pantalla)
            
        self.disparar(personaje,lista_plataformas)
        self.colision_con_personaje(personaje)


    def actualizar_vidas(self,pantalla):
        if self.vidas > 0:
            self.vidas_class.actualizar(pantalla,self.vidas)
        else:
            self.muriendo = True


    def disparar(self,personaje,lista_plataformas):
        if self.muriendo == False:
            if pygame.time.get_ticks() % 10000 < 50:
                if self.tiempo_disparo == False:
                    pygame.time.set_timer(pygame.USEREVENT + 6,1000,1)
                    self.tiempo_disparo = True
                for i in range(0,20):
                    proyectil = DisparoBoss()
                    self.proyectiles.add(proyectil)
                    i+=1
            # else:
            #     self.animacion_actual = self.animaciones["Quieto_izquierda"]

            self.proyectiles.update(personaje,lista_plataformas)
            self.proyectiles.draw(PANTALLA)

    def animar(self,pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(self.animacion_actual[self.contador_pasos],self.rectangulo)
        self.contador_pasos += 1
    
    def colision_con_personaje(self,personaje):
        if self.rectangulo.colliderect(personaje.rectangulo_principal):
            if personaje.atacar:
                if self.tiempo_vul == False:
                    self.vidas -= 1
                    self.atac = True
                    pygame.time.set_timer(pygame.USEREVENT + 7,3000,1)
                    self.tiempo_vul = True
            else:
                if personaje.vulnerabilidad == False:
                    personaje.tiempo_ant_atacado = pygame.time.get_ticks()
                    personaje.atacado = True
                    personaje.vidas -=1
                    pygame.time.set_timer(pygame.USEREVENT,3000,1)
                    personaje.vulnerabilidad = True

