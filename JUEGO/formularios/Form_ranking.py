import pygame
from pygame.locals import *

from UI.GUI_button_image import *
from UI.GUI_form import *
from UI.GUI_label import *

class FormRanking(Form):
    def __init__(self, screen, x,y,w,h,path_image,scoreboard,margen_y,margen_x, espacio,active = True):
        super().__init__(screen, x,y,w,h, active)
        self.flag_play = True
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        self._score = scoreboard
        self.lista_widgets = []  
        self._margen_y = margen_y
        self.volumen = 0.2
        pygame.mixer.init()
        pygame.mixer.music.load(r"Sonidos\Futari No Kimochi.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        
        #Encapsular esta logica en un metodo. Esto nos permite dibujar la tabla en pantalla
        pos_inicial_y = margen_y
        for j in self._score:
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = "" 
                cadena = f"{s}"
                pos = Label(screen=self._slave, x=pos_inicial_x,y=pos_inicial_y,
                            w=w/2-margen_x,h=100,text = cadena, font="arialblack",font_size=40,
                            font_color=(0,0,0),path_image="Recursos\casilla.png")
                self.lista_widgets.append(pos)
                pos_inicial_x += w/2-margen_x
            pos_inicial_y+=100 + espacio                  
        self.x = x
        self.y = y      


    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()     

    
    def detener_musica(self):
        if self.flag_play:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

        self.flaf_play = not self.flag_play


