import pygame
class Disparo:
    def __init__(self,x,y,direccion):
        self.direccion = direccion

        if self.direccion == "ataque_especial_derecha":
            self.imagen = pygame.transform.flip(pygame.image.load(r"Imagenes_Sprites\proyectiles\0.png"),True,False)
            self.superficie = pygame.transform.scale(self.imagen,(50,30))
            self.rectangulo = self.superficie.get_rect()
        else:    
            self.imagen = pygame.image.load(r"Imagenes_Sprites\proyectiles\0.png")
            self.superficie = pygame.transform.scale(self.imagen,(50,30))
            self.rectangulo = self.superficie.get_rect()
            
        self.rectangulo.x = x
        self.rectangulo.centery = y
    

    def actualizar(self):
        if self.direccion == "ataque_especial_derecha":
            self.rectangulo.x += 10
        elif self.direccion == "ataque_especial_izquierda":
            self.rectangulo.x -= 10