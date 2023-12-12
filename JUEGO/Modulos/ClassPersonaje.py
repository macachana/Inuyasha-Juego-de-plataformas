from Configuraciones.config import *
import pygame
from Modulos.ClassPlataformas import *
from Modulos.ClassEnemigo import Enemigo
from Modulos.ClassVidas import Vidas
from Configuraciones.sonidos import *
from Modulos.ClassDisparo import Disparo
from Configuraciones.colores_y_fonts import *

class Personaje:
    def __init__(self,animaciones,tamaño,pos_x,pos_y,velocidad):
        self.animaciones = animaciones

        reescalar_imagenes(self.animaciones,*tamaño)
        self.rectangulo_principal = self.animaciones["Quieto_derecha"][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.velocidad = velocidad
        self.que_hace = "Quieto_derecha"
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Quieto_derecha"]
        #Giovanni dijo que hay que hacer clase pantalla
        self.desplazamiento_y = 0
        self.potencia_salto = -18
        self.limite_velocidad_salto = 18
        self.gravedad = 1
        self.esta_saltando = False
        #agregue yo, banderas, que me indiquen cuando va para una direccion o la otra 
        #asi se a que direccion va a saltar
        self.direccion_derecha = False
        self.direccion_izquierda = False
        #habilidad que obtiene si es que captura un item de espada
        self.habilidad_especial_espada = False
        self.tiempo_habilidad_especial = 15
        self.tiempo_ant_atacado = 0
        self.atacar = False
        self.danado = False
        self.vidas = 3
        self.vidas_class = Vidas(150,10,50,50,3)
        self.muerto = False
        self.vulnerabilidad = False
        self.flag_disparo = False
        self.tiempo_ultimo_disparo = 0
        self.lista_proyectiles = []
        self.atacado = False
        self.cant_enemigos_muertos = 0
        self.cant_ataque_boss = 0


    def vidas_actualizacion(self,pantalla):
        self.vidas_class.actualizar(pantalla,self.vidas)

    def actualizar(self,pantalla,plataforma,lista_enemigos:list["Enemigo"],boss = ""):
        self.tecla_presionada()
        self.vidas_actualizacion(pantalla)
        self.verificar_colision_enemigo(lista_enemigos,pantalla)
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual > self.tiempo_ant_atacado + 6000:
            self.atacado = False

        if self.atacado:
            match self.que_hace:
                case "Derecha":
                    accion = "camina_danado"
                case "Izquierda":
                    accion = "camina_danado_izquierda"
                case "Quieto_derecha":
                    accion = "danado"
                case "Quieto_izquierda":
                    accion = "danado_izquierda"
                case "Saltar_derecha":
                    accion = "danado_saltar"
                case "Saltar_izquierda":
                    accion = "danado_saltar_izquierda"
                case "ataque_derecha":
                    accion = "danado"
                case "ataque_izquierda":
                    accion = "danado_izquierda"
                case "ataque_especial_derecha":
                    accion = "camina_danado"
                case "ataque_especial_izquierda":
                    accion = "camina_danado"
            self.animacion_actual = self.animaciones[accion]
        else:
            self.animacion_actual = self.animaciones[self.que_hace]

        match self.que_hace:
            case "Derecha":
                if self.esta_saltando == False:
                    self.direccion_derecha = True
                    self.direccion_izquierda = False
                    self.animacion_actual = self.animaciones["Derecha"]
                    self.animar(pantalla)  
                sonido_caminar.play()                   
                self.caminar(pantalla)
            case "Izquierda":
                if self.esta_saltando == False:
                    self.direccion_izquierda = True
                    self.direccion_derecha = False
                    self.animacion_actual = self.animaciones["Izquierda"]
                    self.animar(pantalla)   
                sonido_caminar.play()
                self.caminar(pantalla)


            case "Quieto_derecha":
                if self.esta_saltando == False:
                    self.direccion_derecha = True
                    self.direccion_izquierda = False
                    self.animacion_actual = self.animaciones["Quieto_derecha"]
                    self.animar(pantalla)

            case "Quieto_izquierda":
                if self.esta_saltando == False:
                    self.direccion_izquierda = True
                    self.direccion_derecha = False           
                    self.animacion_actual = self.animaciones["Quieto_izquierda"]
                    self.animar(pantalla)   
            
            case "Saltar_derecha":
                if self.esta_saltando == False:
                    self.direccion_derecha = True
                    self.direccion_izquierda = False
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_actual = self.animaciones["Saltar_derecha"]
                    self.animar(pantalla)
                    sonido_salto.play()
            
            case "Saltar_izquierda":
                if self.esta_saltando == False:
                    self.direccion_izquierda = True
                    self.direccion_derecha = False
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_actual = self.animaciones["Saltar_izquierda"]
                    self.animar(pantalla)
                    sonido_salto.play()
            
            case "ataque_derecha":
                if self.esta_saltando == False and self.atacar == False and self.atacado == False:
                    self.direccion_izquierda = False
                    self.direccion_derecha = True
                    self.atacar = True
                    self.animacion_actual = self.animaciones["ataque_derecha"]
                    self.animar_ataque(pantalla,self.animaciones["ataque_derecha"],100,60)
                    pygame.time.set_timer(pygame.USEREVENT + 2,500,1) 
            
            case "ataque_izquierda":
                if self.esta_saltando == False and self.atacar== False and self.atacado:
                    self.direccion_izquierda = True
                    self.direccion_derecha = False                   
                    self.animacion_actual = self.animaciones["ataque_izquierda"]
                    self.animar_ataque(pantalla,self.animaciones["ataque_izquierda"],100,60)
                    pygame.time.set_timer(pygame.USEREVENT + 2,500,1) 
                    self.atacar = True

            case "ataque_especial_derecha":
                if self.esta_saltando == False and self.habilidad_especial_espada:
                    self.direccion_derecha = True                   
                    self.direccion_izquierda = False                   
                    sonido_ataque_espada.play()
                    self.animacion_actual = self.animaciones["ataque_especial_derecha"]
                    self.animar_ataque(pantalla,self.animaciones["ataque_especial_derecha"],100,60)

            case "ataque_especial_izquierda":
                if self.esta_saltando == False and self.habilidad_especial_espada:
                    self.direccion_izquierda = True      
                    self.direccion_derecha = False 
                    sonido_ataque_espada.play()
                    self.animacion_actual = self.animaciones["ataque_especial_izquierda"]
                    self.animar_ataque(pantalla,self.animaciones["ataque_especial_izquierda"],100,60)
                               
        self.actualizar_proyectiles(pantalla,lista_enemigos,plataforma,boss)
        self.aplicar_gravedad(pantalla,plataforma)
    
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

    def animar_ataque(self,pantalla,lista_animacion,x,y):
        reescalar_imagenes_lista(lista_animacion,x,y)
        for e in range(len(lista_animacion)):
            pantalla.blit(lista_animacion[e],self.rectangulo_principal)
            

    def animar(self,pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(self.animacion_actual[self.contador_pasos],self.rectangulo_principal)
        self.contador_pasos += 1

    def animar_atacado(self,pantalla,cant):
        for i in range(0,cant):
            largo = len(self.animacion_actual)
            if self.contador_pasos >= largo:
                self.contador_pasos = 0

            pantalla.blit(self.animacion_actual[self.contador_pasos],self.rectangulo_principal)
            self.contador_pasos += 1
            i+=1

    def caminar(self,pantalla):
        velocidad_actual = self.velocidad
        if self.que_hace == "Izquierda":
            
            velocidad_actual *= -1
        
        nueva_x = self.rectangulo_principal.x + velocidad_actual
        if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width:
            self.rectangulo_principal.x += velocidad_actual

        
    def aplicar_gravedad(self, pantalla, plataforma: list["Plataformas"]):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
        for piso in plataforma:
            if piso.movil == False:
                if self.rectangulo_principal.colliderect(piso.rectangulo_principal):
                    if self.obtener_right_cuadrado().colliderect(piso.obtener_left_cuadrado()):
                        self.rectangulo_principal.x = piso.rectangulo_principal.x - self.rectangulo_principal.width
                        self.desplazamiento_y = 0


                    elif self.obtener_left_cuadrado().colliderect(piso.obtener_right_cuadrado()):
                        self.rectangulo_principal.x = piso.rectangulo_principal.x + piso.rectangulo_principal.width
                        self.desplazamiento_y = 0
                    if self.obtener_top_cuadrado().colliderect(piso.obtener_bottom_cuadrado()):
                        self.desplazamiento_y = 0
                        self.esta_saltando = False
                        self.rectangulo_principal.top = piso.rectangulo_principal.bottom
                        break
                    else:
                        if self.obtener_bottom_cuadrado().colliderect(piso.obtener_top_cuadrado()):
                            self.desplazamiento_y = 0 
                            self.esta_saltando = False
                            self.rectangulo_principal.bottom = piso.rectangulo_principal.top
                            break
                    

                else:
                    self.esta_saltando = True
            else:
                    if piso.arriba_y_abajo == False:
                        if self.rectangulo_principal.colliderect(piso.rectangulo_principal):
                            if self.obtener_right_cuadrado().colliderect(piso.obtener_left_cuadrado()):
                                # Colisión con el lado izquierdo de la plataforma
                                self.rectangulo_principal.x = piso.rectangulo_principal.x - self.rectangulo_principal.width
                                self.desplazamiento_y = 0


                            elif self.obtener_left_cuadrado().colliderect(piso.obtener_right_cuadrado()):
                                # Colisión con el lado derecho de la plataforma
                                self.rectangulo_principal.x = piso.rectangulo_principal.x + piso.rectangulo_principal.width
                                self.desplazamiento_y = 0
                            else:
                                if self.obtener_bottom_cuadrado().colliderect(piso.obtener_top_cuadrado()):
                                    self.rectangulo_principal.bottom = piso.rectangulo_principal.top                                    
                                    self.rectangulo_principal.x = piso.rectangulo_principal.x
                                    self.desplazamiento_y = 0 
                                    self.esta_saltando = False
                                    break
                        else:
                            self.esta_saltando = True
                    else:
                        if self.rectangulo_principal.colliderect(piso.rectangulo_principal):
                            if self.obtener_right_cuadrado().colliderect(piso.obtener_left_cuadrado()):
                                # Colisión con el lado izquierdo de la plataforma
                                self.rectangulo_principal.x = piso.rectangulo_principal.x - self.rectangulo_principal.width
                                self.desplazamiento_y = 0


                            elif self.obtener_left_cuadrado().colliderect(piso.obtener_right_cuadrado()):
                                # Colisión con el lado derecho de la plataforma
                                self.rectangulo_principal.x = piso.rectangulo_principal.x + piso.rectangulo_principal.width
                                self.desplazamiento_y = 0
                            else:
                                if self.obtener_bottom_cuadrado().colliderect(piso.obtener_top_cuadrado()):
                                    self.desplazamiento_y = 0 
                                    self.esta_saltando = False
                                    self.rectangulo_principal.bottom = piso.rectangulo_principal.top
                                    break
                        else:
                            self.esta_saltando = True     
        
        # Evitar que el personaje se pase de la parte superior de la pantalla
        if self.rectangulo_principal.top < 70:
            self.rectangulo_principal.top = 70
            self.desplazamiento_y = 0
            self.esta_saltando = False

    def verificar_colision_enemigo(self,lista_enemigo:list["Enemigo"],pantalla):
        for enemigo in lista_enemigo:
            if self.rectangulo_principal.colliderect(enemigo.rectangulo_principal):
                if self.atacar:
                    enemigo.rectangulo_principal.y+=pantalla.get_height()
                    enemigo.animacion_actual = enemigo.animaciones["atacado"]
                    enemigo.muriendo = True
                    enemigo.animar(pantalla)  
                    self.cant_enemigos_muertos +=1
                    self.atacar = True
                else:
                    if self.vulnerabilidad == False:
                        self.tiempo_ant_atacado = pygame.time.get_ticks()
                        self.atacado = True
                        self.vidas -=1
                        pygame.time.set_timer(pygame.USEREVENT,3000,1)
                        self.vulnerabilidad = True

    def tecla_presionada(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            self.direccion_derecha = True
            self.que_hace = "Derecha"
        elif teclas[pygame.K_LEFT]:
            self.direccion_izquierda = True
            self.que_hace = "Izquierda"
        elif teclas[pygame.K_SPACE]:
            if self.direccion_izquierda:
                self.que_hace = "Saltar_izquierda"
            else:
                self.que_hace = "Saltar_derecha"
        elif teclas[pygame.K_z]:
            if self.direccion_izquierda:
                self.que_hace = "ataque_izquierda"
            else:
                self.que_hace = "ataque_derecha"
        elif teclas[pygame.K_x]:
            if self.habilidad_especial_espada:
                if self.direccion_izquierda:
                    self.que_hace = "ataque_especial_izquierda"
                else:
                    self.que_hace = "ataque_especial_derecha"
        else:
            if self.direccion_izquierda:
                self.que_hace = "Quieto_izquierda"
            else:
                self.que_hace = "Quieto_derecha"

        if self.habilidad_especial_espada:
            self.flag_disparo = True  
        else:
            self.flag_disparo = False 

        if self.flag_disparo and teclas[pygame.K_x] and int(self.tiempo_habilidad_especial)>0:
            self.lanzar_proyectil()
            self.flag_disparo = False

                

    def lanzar_proyectil(self):
        #posicion en x de donde va a salir el proyectil
        x = None
        margen = 47
        #busco la pósicion y desde donde va a salir el disparo
        y = self.rectangulo_principal.centery + 10
        if self.que_hace == "ataque_especial_derecha":
            #calculo para que el disparo no sea unos pixeles despues del right del personaje sino que sea 
            #desde un punto mas adentro del personaje
            x = self.rectangulo_principal.right - margen
        elif self.que_hace == "ataque_especial_izquierda":
            x = self.rectangulo_principal.left - 100 + margen
        if x is not None:
            self.lista_proyectiles.append(Disparo(x,y,self.que_hace))
    
    def actualizar_proyectiles(self,pantalla,lista_enemigos:list["Enemigo"],lista_plataformas,boss = ""):
        if self.habilidad_especial_espada and int(self.tiempo_habilidad_especial) >=0.0:
            self.tiempo_habilidad_especial -= 1/60.0

        if int(self.tiempo_habilidad_especial) == 0:
            self.tiempo_habilidad_especial = 0
            self.habilidad_especial_espada = False

        if self.habilidad_especial_espada and int(self.tiempo_habilidad_especial) > 0:
            boton_cuadrado(pantalla,Rect(680,10,100,50),f"{int(self.tiempo_habilidad_especial)}",font1,BORDO)
        else:
            self.habilidad_especial_espada = False
        i = 0
        while i < len(self.lista_proyectiles)-1 :
            p = self.lista_proyectiles[i]
            pantalla.blit(p.superficie,p.rectangulo)
            p.actualizar()
            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1
            
            if boss != "":
                if boss.rectangulo.colliderect(p.rectangulo):
                    self.cant_ataque_boss += 1
                    if self.cant_ataque_boss == 3:
                        self.cant_ataque_boss = 0
                        boss.vidas -= 1
                        boss.atac = True

                    self.lista_proyectiles.pop(i)
                    i-=1


            for plat in lista_plataformas:
                if plat.rectangulo_principal.colliderect(p.rectangulo):
                    self.lista_proyectiles.pop(i)
                    i-=1

            for enemigo in lista_enemigos:
                if enemigo.rectangulo_principal.colliderect(p.rectangulo):
                    enemigo.muriendo = True
                    self.cant_enemigos_muertos +=1
                    enemigo.rectangulo_principal.y+=pantalla.get_height()
                    enemigo.animacion_actual = enemigo.animaciones["atacado"]
                    enemigo.animar(pantalla)
                    self.lista_proyectiles.pop(i)
                    i-=1
            i+=1
        

