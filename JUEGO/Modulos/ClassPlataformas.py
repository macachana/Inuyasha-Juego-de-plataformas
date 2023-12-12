from Configuraciones.config import *

class Plataformas:
    def __init__(self,tamano,x,y,path="",visible=False,movil=False,punto_inicio = None, punto_final = None,velocidad = None,arriba_y_abajo=False):
        
        #BANDERAS PARA PLATAFORMAS NORMALES
        self.path = path
        self.visible = visible
        self.tamano = tamano

        if self.visible:
            self.imagen = pygame.image.load(self.path)
            self.superficie = pygame.transform.scale(self.imagen,self.tamano)      
    
        self.rectangulo_principal = self.superficie.get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y


        #BANDERAS SI ES PLATAFORMA MOVIL
        self.movil = movil
        self.speed = velocidad
        self.arriba_y_abajo = arriba_y_abajo
        self.punto_inicio = punto_inicio
        self.punto_final = punto_final

        self.mini_cuadrados = {}

        self.mini_cuadrados["bottom"] = self.obtener_bottom_cuadrado()
        self.mini_cuadrados["top"] = self.obtener_top_cuadrado()
        self.mini_cuadrados["left"] = self.obtener_left_cuadrado()
        self.mini_cuadrados["right"] = self.obtener_right_cuadrado()

    def update(self):
        if self.movil:
            if self.arriba_y_abajo:
                self.rectangulo_principal.y += self.speed
                if self.rectangulo_principal.bottom > self.punto_final or self.rectangulo_principal.top < self.punto_inicio:
                    self.speed = -self.speed
            else:
                self.rectangulo_principal.x += self.speed

                if self.rectangulo_principal.right > self.punto_final or self.rectangulo_principal.left < self.punto_inicio:
                    self.speed = -self.speed
            
            if self.arriba_y_abajo:
                for key in self.mini_cuadrados:
                    mini_cuadrado = self.mini_cuadrados[key]
                    if key == "bottom":
                        mini_cuadrado.y += self.speed
                    elif key == "top":
                        mini_cuadrado.y += self.speed
                    elif key == "left":
                        mini_cuadrado.y += self.speed
                    elif key == "right":
                        mini_cuadrado.y += self.speed
            else:
                for key in self.mini_cuadrados:
                    mini_cuadrado = self.mini_cuadrados[key]
                    if key == "bottom":
                        mini_cuadrado.x += self.speed
                    elif key == "top":
                        mini_cuadrado.x += self.speed
                    elif key == "left":
                        mini_cuadrado.x += self.speed
                    elif key == "right":
                        mini_cuadrado.x += self.speed



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


    def actualizar(self,pantalla):
        pantalla.blit(self.superficie,self.rectangulo_principal)
        if self.movil:
            pantalla.blit(self.superficie,self.rectangulo_principal)
            self.update()




