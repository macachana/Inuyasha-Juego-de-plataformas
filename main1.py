'''

ALUMNA : MACARENA CHANAMPA
PRIMER AÑO Y DIVISION B
AÑO : 2023

'''

import pygame
from Configuraciones.config import *
from Modulos.Modo import *
from Configuraciones.plataformas import *
from Configuraciones.fondos import *
from Configuraciones.colores_y_fonts import *
import sys
from formularios.form_escribir_n import FormEscribirNombre
from formularios.Form_ranking import FormRanking
from formularios.Form_config import FormConfig
from Configuraciones.sonidos import *
from Niveles.ClassNivell import Nivel

pygame.init()
RELOJ = pygame.time.Clock()
volv_nivel1 = False
volv_nivel2 = False
volv_nivel3 = False
nivelUno = False
nivelUnoRestaurado = False
nivelDos = False
nivelTres = False

nivel_uno_restaurado = Nivel(True,PANTALLA,inuyasha1,plataformas_nivel_1,lista_items_nivel_1,lista_enemigos_nivel_1,lista_trampas_nivel_1,fondo_nivel_uno,60,"Sonidos\musica_nivel_1.mp3",2160)

nivel_dos_restaurado = Nivel(True,PANTALLA,inuyasha2,plataformas_nivel_2,lista_items_nivel_2,lista_enemigos_nivel_2,lista_trampas_nivel_2,fondo_nivel_dos,60,"Sonidos\musica_nivel_2.mp3",2000)

nivel_tres_restaurado = Nivel(True,PANTALLA,inuyasha3,plataformas_nivel_3,lista_items_nivel_3,lista_enemigos_nivel_3,lista_trampas_nivel_3,fondo_nivel_tres,80,"Sonidos\musica_nivel_tres.mp3",1500,True,acciones_boss)

nivel_uno = Nivel(True,PANTALLA,inuyasha1,plataformas_nivel_1,lista_items_nivel_1
                  ,lista_enemigos_nivel_1,lista_trampas_nivel_1,fondo_nivel_uno,60,"Sonidos\musica_nivel_1.mp3",1980)
nivel_dos = Nivel(True,PANTALLA,inuyasha2,plataformas_nivel_2,lista_items_nivel_2
                  ,lista_enemigos_nivel_2,lista_trampas_nivel_2,fondo_nivel_dos,60,"Sonidos\musica_nivel_2.mp3",2500)
nivel_tres = Nivel(True,PANTALLA,inuyasha3,plataformas_nivel_3,lista_items_nivel_3
                   ,lista_enemigos_nivel_3,lista_trampas_nivel_3,fondo_nivel_tres,80,"Sonidos\musica_nivel_tres.mp3",1380,True,acciones_boss)

contador_pasos = 0
bandera = True
inicio = True
ingresar_nombre = False
controles = False
ranking = False

reinicio_nivel = False
seleccion_nivel = False
gano = False
perdio = False
pausa = False
config = False

diccionario = [{"Jugador":"Macarena","score":100}]
form_ingrese_n = FormEscribirNombre(PANTALLA,406,287,542,297,PURPURA,PURPURA,3,True)
form_ranking = FormRanking(PANTALLA,0,0,1300,700,r"Imagenes_Sprites\fondos\fondo_ranking.jpg",diccionario,330,320,10,True)
form_config = FormConfig(PANTALLA,0,0,1300,700,r"Imagenes_Sprites\fondos\configuracion__.jpg",True)



while True:

    while inicio:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                #boton play
                if Rect(456,390,402,105).collidepoint(mouse.get_pos()):
                    sonido.play()
                    inicio = False
                    ingresar_nombre = True  
                #boton controles
                elif Rect(67,540,513,133).collidepoint(mouse.get_pos()):
                    sonido.play()
                    inicio = False
                    controles = True
                #boton ranking
                elif Rect(716,540,513,133).collidepoint(mouse.get_pos()):
                    sonido.play()
                    inicio = False
                    ranking = True
        
        PANTALLA.blit(fondo_inicio,(0,0))

        btn_play = pygame.Surface((402,105))
        btn_controles = pygame.Surface((513,133))
        btn_ranking = pygame.Surface((513,133))

        boton_invisible_doble_color(PANTALLA,btn_play,456,390,DORADO,BLANCO)
        boton_invisible_doble_color(PANTALLA,btn_controles,67,540,DORADO,BLANCO)
        boton_invisible_doble_color(PANTALLA,btn_ranking,716,540,DORADO,BLANCO)
        pygame.display.update()   

    while ingresar_nombre:
        lista_eventos = pygame.event.get() 
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()      
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if Rect(640,494,110,80).collidepoint(mouse.get_pos()):
                    sonido.play()
                    ingresar_nombre = False
                    seleccion_nivel = True
        PANTALLA.blit(fondo_ingresar_nombre,(0,0))
        form_ingrese_n.update(lista_eventos)
        pygame.display.update()

    while seleccion_nivel:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()                  
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if Rect(400,184,530,131).collidepoint(mouse.get_pos()):
                    sonido.play()
                    seleccion_nivel = False
                    nivelUno = True
                if Rect(400,345,530,131).collidepoint(mouse.get_pos()):
                    if nivel_uno.nivel_ganado == True and nivel_dos.nivel_perdido == False:
                        sonido.play()
                        seleccion_nivel = False
                        nivelDos = True
                if Rect(400,507,530,131).collidepoint(mouse.get_pos()):
                    if nivel_dos.nivel_ganado == True and nivel_tres.nivel_perdido == False:
                        sonido.play()
                        seleccion_nivel = False
                        nivelTres = True

        PANTALLA.blit(fondo_seleccion_niveles,(0,0))
        btn_nivel_uno = pygame.Surface((530,131))
        btn_nivel_dos = pygame.Surface((530,131))
        btn_nivel_tres = pygame.Surface((530,131))

        boton_invisible_doble_color(PANTALLA,btn_nivel_uno,400,184,MORADO_CLARITO,BLANCO)
        if nivel_uno.nivel_ganado == True and nivel_dos.nivel_perdido == False:
            boton_invisible_doble_color(PANTALLA,btn_nivel_dos,400,345,MORADO_CLARITO,BLANCO)
        if nivel_dos.nivel_ganado == True and nivel_tres.nivel_perdido == False:
            boton_invisible_doble_color(PANTALLA,btn_nivel_tres,400,507,MORADO_CLARITO,BLANCO)

        pygame.display.update() 

    while nivelUno:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()      
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                print(mouse.get_pos())
                if Rect(33,15,100,40).collidepoint(mouse.get_pos()):
                    sonido.play()
                    volv_nivel1 = True
                    nivelUno = False
                    pausa = True

        nivel_uno.update(lista_eventos)

        if nivel_uno.nivel_ganado:
            nivelUno = False
            gano = True
        if nivel_uno.nivel_perdido:
            nivelUno = False
            perdio = True


        boton_cuadrado(PANTALLA,Rect(33,15,100,40),"Pausa",font1,MORADO)
        pygame.display.update()

    while nivelDos:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()  
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                print(mouse.get_pos())
                if Rect(33,15,100,40).collidepoint(mouse.get_pos()):
                    volv_nivel2 = True
                    nivelDos = False
                    pausa = True
        
        nivel_dos.update(lista_eventos)

        if nivel_dos.nivel_ganado:
            nivelDos = False
            gano = True
        if nivel_dos.nivel_perdido:
            nivelDos = False
            perdio = True


        boton_cuadrado(PANTALLA,Rect(33,15,100,40),"Pausa",font1,MORADO)
        pygame.display.update()



    while nivelTres:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit() 
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                print(mouse.get_pos())
                if Rect(33,15,100,40).collidepoint(mouse.get_pos()):
                    sonido.play()
                    volv_nivel3 = True
                    nivelTres = False
                    pausa = True

        nivel_tres.update(lista_eventos)

        if nivel_tres.nivel_ganado:
            nivelTres = False
            gano = True
        if nivel_tres.nivel_perdido:
            nivelTres = False
            perdio = True

        boton_cuadrado(PANTALLA,Rect(33,15,100,40),"Pausa",font1,MORADO)
        pygame.display.update()                 


    while perdio:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()      
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # print(mouse.get_pos())
                if Rect(307,555,161,75).collidepoint(mouse.get_pos()):
                    perdio = False
                    seleccion_nivel = True
                if Rect(838,555,200,75).collidepoint(mouse.get_pos()):
                    if nivel_uno.nivel_perdido:
                        perdio = False
                        nivelUno = True
                    if nivel_dos.nivel_perdido:
                        perdio = False
                        nivelDos = True
                    if nivel_tres.nivel_perdido:
                        perdio = False
                        nivelTres = True
                
        PANTALLA.blit(fondo_perdio,(0,0))

        if nivel_uno.nivel_perdido:
            boton_cuadrado(PANTALLA,Rect(450,300,400,250),nivel_uno.get_puntaje_nivel(),font3,MORADO_CLARITO)
        elif nivel_dos.nivel_perdido:
            boton_cuadrado(PANTALLA,Rect(450,300,400,250),nivel_dos.get_puntaje_nivel(),font3,MORADO_CLARITO)
        elif nivel_tres.nivel_perdido:
            boton_cuadrado(PANTALLA,Rect(450,300,400,250),nivel_tres.get_puntaje_nivel(),font3,MORADO_CLARITO)

        boton_cuadrado(PANTALLA,Rect(307,555,161,75),"Niveles",font1,MORADO)
        boton_cuadrado(PANTALLA,Rect(838,555,200,75),"Reiniciar nivel",font1,MORADO)
        pygame.display.update() 

    while gano:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()      
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if Rect(307,555,161,75).collidepoint(mouse.get_pos()):
                    gano = False
                    seleccion_nivel = True
                if Rect(838,555,161,75).collidepoint(mouse.get_pos()):
                    if nivel_uno.nivel_ganado:
                        gano = False
                        nivelDos = True
                        nivel_uno.reiniciar_puntaje()
                    if nivel_dos.nivel_ganado:
                        gano = False
                        nivelTres = True
                    if nivel_tres.nivel_ganado:
                        gano = False
                        seleccion_nivel = True
        PANTALLA.blit(fondo_gano,(0,0))
        
        if nivel_uno.nivel_ganado:
            boton_cuadrado(PANTALLA,Rect(450,300,400,250),nivel_uno.get_puntaje_nivel(),font3,MORADO_CLARITO)
        if nivel_dos.nivel_ganado:
            boton_cuadrado(PANTALLA,Rect(450,300,400,250),nivel_dos.get_puntaje_nivel(),font3,MORADO_CLARITO)
        if nivel_tres.nivel_ganado:
            boton_cuadrado(PANTALLA,Rect(450,300,400,250),nivel_tres.get_puntaje_nivel(),font3,MORADO_CLARITO)

        boton_cuadrado(PANTALLA,Rect(307,555,161,75),"Niveles",font1,MORADO)
        boton_cuadrado(PANTALLA,Rect(838,555,161,75),"Sig. nivel",font1,MORADO)
        pygame.display.update() 

    while pausa:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()      
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if Rect(530,190,310,80).collidepoint(mouse.get_pos()):
                    sonido.play()
                    pausa = False
                    seleccion_nivel = True
                if Rect(530,295,310,80).collidepoint(mouse.get_pos()):
                    sonido.play()
                    pausa = False
                    config = True
                if Rect(530,395,310,80).collidepoint(mouse.get_pos()):
                    sonido.play()
                    pausa = False
                    if volv_nivel1:
                        nivelUno = True
                    elif volv_nivel2:
                        nivelDos = True
                    elif volv_nivel3:
                        nivelTres = True
        PANTALLA.blit(fondo_de_pausa,(0,0))
        pygame.display.update()       

    while config:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()      
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if Rect(25,25,135,50).collidepoint(mouse.get_pos()):
                    sonido.play()
                    config = False
                    pausa = True
        form_config.update(lista_eventos)
        boton_cuadrado(PANTALLA,Rect(25,25,135,50),"VOLVER",font1,MORADO_CLARITO)
        pygame.display.update()         

    while ranking:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()      
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if Rect(25,25,135,50).collidepoint(mouse.get_pos()):
                    sonido.play()
                    ranking = False
                    inicio = True
        form_ranking.update(lista_eventos)
        boton_cuadrado(PANTALLA,Rect(25,25,135,50),"VOLVER",font1,MORADO_CLARITO)
        pygame.display.update() 

    while controles:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                sys.exit()      
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if Rect(25,25,135,50).collidepoint(mouse.get_pos()):
                    sonido.play()
                    controles = False
                    inicio = True
        PANTALLA.blit(fondo_controles,(0,0))
        boton_cuadrado(PANTALLA,Rect(25,25,135,50),"VOLVER",font1,DORADO)
        pygame.display.update() 
    RELOJ.tick(FPS)
    pygame.display.update()

