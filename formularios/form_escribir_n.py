import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from Configuraciones.colores_y_fonts import *
class FormEscribirNombre(Form):
    def __init__(self, screen, x,y,w,h,color_background,color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h, color_background,color_border, border_size, active)

        self.volumen = 0.2
        self.x = x
        self.y = y

        self.flag_play = True    
        pygame.mixer.init()    
        pygame.mixer.music.load(r"Sonidos\Futari No Kimochi.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.txt_nombre = TextBox(self._slave,self.x,self.y,20,20,502,100,"white","pink","pink","red",3,"Comic Sans",30,"black")

        self.btn_ok = Button_Image(self._slave,x,y,230,200,100,100,r"Imagenes_Sprites\botones\boton_ok.png",self.btn_ok_click,"")
        # self.btn_no = Button_Image(self._slave,x,y,322,200,100,100,r"Imagenes_Sprites\botones\boton_x.png",self.btn_no_click,"")

        self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.btn_ok)
        # self.lista_widgets.append(self.btn_no)
    
    
    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.active:
            self.draw()
            self.render()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)#POLIMORFISMO
                
        else:
            self.hijo.update(lista_eventos)


    def btn_ok_click(self,param):
        pass

    def obtener_nombre(self):
        return self.txt_nombre.get_text()
    # def btn_play_click(self, param):
    #     if self.flag_play:
    #         self.btn_play._color_background = "blue"
    #         self.btn_play.set_text("Play")
    #         #pone en pausa la musica
    #         pygame.mixer.music.pause()

    #     else:
    #         #cambiamos el texto del boton a pause
    #         self.btn_play._color_background = "green"
    #         self.btn_play.set_text("Pause")
    #         #despausa la musica
    #         pygame.mixer.music.unpause()


    #     self.flag_play = not self.flag_play
