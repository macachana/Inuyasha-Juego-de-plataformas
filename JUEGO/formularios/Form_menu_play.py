from UI.GUI_form import *
from formularios.FormContenedor_niveles import *
from Niveles.Manejador_niveles import Manejador_niveles

class FormMenuPlay(Form):
    def __init__(self,screen,x,y,w,h,color_background,color_border,active,path_image):
        super().__init__(screen,x,y,w,h,color_background,color_border,active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        self._btn_level_1 = Button_Image(screen = self._slave,
                            x = 400,
                            y = 184,
                            master_x= x,
                            master_y=y,
                            w = 530,
                            h = 131,
                            onclick=self.entrar_nivel,
                            onclick_param="nivel_uno",
                            path_image="Imagenes_Sprites\\botones\\btn_nivel_uno.png")

        self._btn_level_2 = Button_Image(screen = self._slave,
                            x = 400,
                            y = 345,
                            master_x= x,
                            master_y=y,
                            w = 530,
                            h = 131,
                            onclick=self.entrar_nivel,
                            onclick_param="nivel_dos",
                            path_image="Imagenes_Sprites\\botones\\btn_nivel_dos.png")
        
        self._btn_level_3 = Button_Image(screen = self._slave,
                            x = 400,
                            y = 507,
                            master_x= x,
                            master_y=y,
                            w = 530,
                            h = 131,
                            onclick=self.entrar_nivel,
                            onclick_param="nivel_tres",
                            path_image="Imagenes_Sprites\\botones\\btn_nivel_tres.png")
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)

        

    def on(self,param):
        print("hola",param)

    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        frm_contenedor_nivel = FormContenedorNivel(self._slave,nivel)
        self.show_dialog(frm_contenedor_nivel)

    def btn_home_click(self,param):
        self.end_dialog()

