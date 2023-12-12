import pygame
from pygame import *
from Modulos.Modo import *
from Configuraciones.colores_y_fonts import *
from Modulos.ClassPuntaje import Puntaje
from Configuraciones.config import boton_cuadrado
from Modulos.ClassItem import item
from Modulos.ClassBoss import Boss
import sys
class Nivel:
    def __init__(self,activen,pantalla,personaje_principal,lista_plataformas,lista_items,lista_enemigos,lista_trampas,imagen_fondo,tiempo_restante,musica,punt_max = 2000,nivel_final = False,animaciones_boss = ""):
        self.flag_play = True
        self.volumen = 0.2
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.items = lista_items
        self.enemigos = lista_enemigos
        self.trampas = lista_trampas
        self.img_fondo = imagen_fondo
        self.tiempo = tiempo_restante
        self.music = musica
        self.item_final = False
        self.nivel_ganado = False
        self.nivel_perdido = False
        self.puntaje_maximo = punt_max
        self.active = activen
        self.Nivel_final = nivel_final
        self.puntaje_nivel = 0
        if self.Nivel_final:
            self.boss = Boss(animaciones_boss,1200,400,(70,60),3)

        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

    def update(self,lista_eventos):
        if self.active:
            for evento in lista_eventos:
                if evento.type == pygame.QUIT:
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_TAB:
                        cambiar_modo()
                elif evento.type == pygame.USEREVENT:
                    self.jugador.vulnerabilidad = False
                elif evento.type == pygame.USEREVENT + 2:
                    self.jugador.atacar = False
                elif evento.type == pygame.USEREVENT + 3:
                    for i in self.items:
                        i.ben = False
                elif evento.type == pygame.USEREVENT + 4:
                    self.jugador.habilidad_especial_espada = False
                elif evento.type == pygame.USEREVENT + 6:
                    self.boss.tiempo_disparo = False
                elif evento.type == pygame.USEREVENT + 7:
                    self.boss.tiempo_vul = False
                elif evento.type == pygame.USEREVENT + 9:
                    self.items.append(item(100,100,"Imagenes_Sprites\items\item_final.png",False,False,False,True))
            
            self.actualizar_pantalla()
            self.actualizar_puntaje()
            self.actualizar_tiempo()

            if self.Nivel_final:
                self.boss.actualizar(self._slave,self.jugador,self.plataformas)

            self.dibujar_rectangulos()

            if self.jugador.vidas == 0 or self.tiempo == 0: 
                self.nivel_perdido = True

    def actualizar_pantalla(self):
        if self.active:
            self._slave.blit(self.img_fondo,(0,0))
            if self.Nivel_final:
                self.jugador.actualizar(self._slave,self.plataformas,self.enemigos,self.boss)
            else:
                self.jugador.actualizar(self._slave,self.plataformas,self.enemigos)

            for it in self.items:
                it.actualizar(self._slave,self.jugador)
                if it.item_final and it.nivel_terminado:
                    self.nivel_ganado = True

            for plat in self.plataformas:
                plat.actualizar(self._slave)
            
            for tramp in self.trampas:
                tramp.actualizar(self._slave,self.jugador)

            for ene in self.enemigos:
                ene.actualizar(self._slave)
                if ene.esta_muerto:
                    del ene
    
    def actualizar_puntaje(self):
        if self.active:
            puntaje = Puntaje(950,10,200,50,BLANCO,font1,self.items,self._slave,BORDO)
            if self.nivel_ganado == False and self.nivel_perdido == False:
                self.puntaje_nivel = puntaje.puntaje_actual

            if puntaje.puntaje_actual >= self.puntaje_maximo:
                pygame.event.post(pygame.event.Event(pygame.USEREVENT + 9))
                
            
    def get_puntaje_nivel(self):
        return str(self.puntaje_nivel)

    def reiniciar_puntaje(self):
        self.puntaje_nivel = 0

    def actualizar_tiempo(self):
        if self.active:
            boton_cuadrado(self._slave,Rect(550,10,100,50),f"{int(self.tiempo)}",font1,BORDO)
            self.tiempo -=1/60.0

    def dibujar_rectangulos(self):
        if self.active:
            if obtener_modo():
                pygame.draw.rect(self._slave,"yellow",self.jugador.rectangulo_principal,3)
                pygame.draw.rect(self._slave,"white",self.jugador.obtener_left_cuadrado(),3)
                pygame.draw.rect(self._slave,"black",self.jugador.obtener_right_cuadrado(),3)
                pygame.draw.rect(self._slave,"yellow",self.jugador.obtener_top_cuadrado(),3)
                pygame.draw.rect(self._slave,"red",self.jugador.obtener_bottom_cuadrado(),3)

                for enemigo in self.enemigos:
                    pygame.draw.rect(self._slave,"white",enemigo.obtener_left_cuadrado(),3)
                    pygame.draw.rect(self._slave,"black",enemigo.obtener_right_cuadrado(),3)
                    pygame.draw.rect(self._slave,"yellow",enemigo.obtener_top_cuadrado(),3)
                    pygame.draw.rect(self._slave,"red",enemigo.obtener_bottom_cuadrado(),3)

                for plataforma in self.plataformas:
                    pygame.draw.rect(self._slave,"blue",plataforma.obtener_bottom_cuadrado(),3)
                    pygame.draw.rect(self._slave,"white",plataforma.obtener_top_cuadrado(),3)
                    pygame.draw.rect(self._slave,"black",plataforma.obtener_left_cuadrado(),3)
                    pygame.draw.rect(self._slave,"pink",plataforma.obtener_right_cuadrado(),3)

                for trampa in self.trampas:
                    pygame.draw.rect(self._slave,"blue",trampa.obtener_bottom_cuadrado(),3)
                    pygame.draw.rect(self._slave,"white",trampa.obtener_top_cuadrado(),3)
                    pygame.draw.rect(self._slave,"black",trampa.obtener_left_cuadrado(),3)
                    pygame.draw.rect(self._slave,"pink",trampa.obtener_right_cuadrado(),3)    
       
    def reiniciar_nivel(self,activenR,pantallaR,personaje_principalR,lista_plataformasR,lista_itemsR,lista_enemigosR,lista_trampasR,imagen_fondoR,tiempo_restanteR,musicaR,punt_maxR,nivel_finalR,animaciones_bossR):
        self.__init__(activenR,pantallaR,personaje_principalR,lista_plataformasR,lista_itemsR,lista_enemigosR,lista_trampasR,imagen_fondoR,tiempo_restanteR,musicaR,punt_maxR,nivel_finalR,animaciones_bossR)

    def pausar_musica(self):
        if self.flag_play:
            pygame.mixer.pause()
        else:
            pygame.mixer.unpause()

        self.flag_play = not self.flag_play

