import pygame
from pygame.locals import *

from UI.GUI_form import *
from UI.GUI_button_image import *
from Configuraciones.colores_y_fonts import *
from formularios.Form_menu_play import FormMenuPlay

class FormPrincipal(Form):
    def __init__(self,screen,x,y,w,h,color_background,color_border,border_size = -1,active=True):
        super().__init__(screen,x,y,w,h,color_background,color_border,border_size,active)
        self.flag_play = True


        self._btn_play = Button_Image(screen = self._slave,
                            x = 400,
                            y = 184,
                            master_x= x,
                            master_y=y,
                            w = 530,
                            h = 131,
                            onclick = self.btn_jugar_click,
                            onclick_param="a",
                            path_image="Imagenes_Sprites\\botones\\btn_play.jpg")

        self._btn_ranking = Button_Image(screen = self._slave,
                            x = 400,
                            y = 345,
                            master_x= x,
                            master_y=y,
                            w = 530,
                            h = 131,
                            onclick=self.btn_ranking_click,
                            onclick_param="Imagenes_Sprites\\botones\\btn_ranking.jpg",
                            path_image="")
        
        self._btn_controles = Button_Image(screen = self._slave,
                            x = 400,
                            y = 507,
                            master_x= x,
                            master_y=y,
                            w = 530,
                            h = 131,
                            onclick=self.btn_jugar_click,
                            onclick_param="a",
                            path_image="Imagenes_Sprites\\botones\\btn_controles.jpg")
        self.lista_widgets.append(self._btn_play)
        self.lista_widgets.append(self._btn_ranking)
        self.lista_widgets.append(self._btn_controles)

    def render(self):
        self._slave.fill(self.color_background)

    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_jugar_click(self,param):
        frm_jugar = FormMenuPlay(screen= self._master,
                                 x = self._master.get_width()/2-250,
                                 y = self._master.get_height()/2-250,
                                 w = 530,
                                 h = 131,
                                 color_background=PURPURA,
                                 color_border=ROJO,
                                 active = True,
                                 path_image = r"Imagenes_Sprites\animacion_inicio\fondo_inicio_s_0.jpg")
        self.show_dialog(frm_jugar)  

    def btn_ranking_click(self,param):
        print("ranking")

