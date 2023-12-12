import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from Configuraciones.colores_y_fonts import *

class FormConfig(Form):
    def __init__(self, screen, x,y,w,h,path_image, active = True):
        super().__init__(screen, x,y,w,h, active)
        self.flag_play = True
        aux_image = pygame.image.load(path_image)
        self.aux_image_e = pygame.transform.scale(aux_image,(w,h))
        self._slave = self.aux_image_e
        self.lista_widgets = []  

        self.volumen = 0.2

        pygame.mixer.init()

        pygame.mixer.music.load(r"Sonidos\Futari No Kimochi.mp3")

        pygame.mixer.music.set_volume(self.volumen)

        pygame.mixer.music.play(-1)        

        self.btn_play = Button(self._slave,x,y,786,235,150,80,MORADO_CLARITO,MORADO_CLARITO,self.pausar_musica_config,"","PAUSAR","Comic Sans",20,NEGRO)
        self.slider_volumen = Slider(self._slave,x,y,353,470,650,50,self.volumen,BORDO,BLANCO)
        porcentaje_volumen = f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave,620,540,120,120,porcentaje_volumen,"Comic Sans",30,"black",r"Recursos\circulo_casilla.png")
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.btn_play)

    def render(self):
        self._slave.blit(self.aux_image_e,(self._slave.get_width(),self._slave.get_height()))

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)#POLIMORFISMO
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def update_volumen(self, lista_eventos):

        self.volumen = self.slider_volumen.value
        # nivel_uno.volumen = self.slider_volumen.value
        # nivel_dos.volumen = self.slider_volumen.value
        # nivel_tres.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)


    def pausar_musica_config(self,param):
        if self.flag_play:
            self.btn_play._color_background = MORADO_CLARITO
            self.btn_play.set_text("DESPAUSAR")
            pygame.mixer.music.pause()
        else:
            self.btn_play._color_background = MORADO_CLARITO
            self.btn_play.set_text("PAUSAR")
            pygame.mixer.music.unpause()

        self.flag_play = not self.flag_play

