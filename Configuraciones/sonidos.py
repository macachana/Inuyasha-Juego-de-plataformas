import pygame

pygame.mixer.init()
volumen = 0.2

##########   EFECTOS   ###########

#ingresar sonido
sonido_salto = pygame.mixer.Sound(r"Sonidos\salto.mp3")

#SONIDO DE RECOGER ITEM
recoger_item_normal = pygame.mixer.Sound(r"Sonidos\bonus-143026.mp3")

#SONIDO DE APRETAR BOTON
apretar_boton = pygame.mixer.Sound(r"Sonidos\OST_boton_click.mp3")

#ATAQUE DE ESPADA 
sonido_ataque_espada = pygame.mixer.Sound(r"Sonidos\sword-hit-7160.mp3")

#SONIDO DE CAMINAR
sonido_caminar = pygame.mixer.Sound(r"Sonidos\snow-step-1-81064.mp3")

