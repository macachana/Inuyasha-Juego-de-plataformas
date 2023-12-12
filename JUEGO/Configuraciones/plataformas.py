from Modulos.ClassPlataformas import Plataformas
from Configuraciones.config import *
from Modulos.ClassPersonaje import Personaje
from Modulos.ClassEnemigo import Enemigo
from Modulos.ClassTrampas import Trampas
from Modulos.ClassItem import item
from Modulos.ClassBoss import Boss
from Configuraciones.animaciones_personajes import *
# from Modulos.ClassBoss import Boss
################################ CONFIGURACION GENERAL ################################
#PERSONAJE

inuyasha1 = Personaje(acciones,(70,60),156,200,10)
inuyasha2 = Personaje(acciones,(70,60),156,588,10)
inuyasha3 = Personaje(acciones,(70,60),67,200,10)

################################ CONFIGURACION NIVEL 1 ################################
#PLATAFORMAS NIVEL 1
plataformas_nivel_1 = [Plataformas((130,30),0,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((130,30),130,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((130,30),260,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),
        Plataformas((130,30),390,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((130,30),520,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((130,30),650,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),
        Plataformas((130,30),780,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((130,30),910,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((130,30),1040,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),
        Plataformas((130,30),1170,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((130,30),1300,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((95,43),16,252,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True,True,252,590,2,True),
        Plataformas((122,59),149,249,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((122,59),271,249,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((122,59),393,249,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),
        Plataformas((122,59),515,249,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((122,59),637,249,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((100,50),200, 540,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),
        Plataformas((100,50),300,540,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((300,20),W-300,H-130,r"Imagenes_Sprites\Plataformas\plataforma_tierra.png",True),Plataformas((88,43),865,297,r"Imagenes_Sprites\Plataformas\plataforma_arbusto.png",True,True,857,1095,3),
        Plataformas((74,28),760,475,r"Imagenes_Sprites\Plataformas\plataforma_arbusto.png",True),Plataformas((74,28),797,475,r"Imagenes_Sprites\Plataformas\plataforma_arbusto.png",True),
        Plataformas((125,38),158,407,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((125,38),283,407,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((125,38),408,407,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((125,38),533,407,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True)]
#ENEMIGOS
lista_enemigos_nivel_1 = [Enemigo(diccionario_enemigo,500,630,100,20,0,1000),Enemigo(diccionario_enemigo,163,350,100,20,163,657),
                  Enemigo(diccionario_enemigo_2,1004,530,100,50,1004,1280),
                  Enemigo(diccionario_enemigo_2,500,620,100,50,0,1000),
                  Enemigo(diccionario_enemigo,500,630,100,20,0,1000),
                  Enemigo(diccionario_enemigo,163,350,100,20,163,657),Enemigo(diccionario_enemigo_2,1004,530,100,50,1004,1280),
                  Enemigo(diccionario_enemigo,163,350,100,20,163,657),
                  Enemigo(diccionario_enemigo_2,500,620,100,50,0,1000)]



#ITEMS
lista_items_nivel_1 = [item(715,390,r"Imagenes_Sprites\items\item_normal.png"),item(775,390,r"Imagenes_Sprites\items\item_normal.png"),item(835,390,r"Imagenes_Sprites\items\item_normal.png"),
                item(715,430,r"Imagenes_Sprites\items\item_normal.png"),item(775,430,r"Imagenes_Sprites\items\item_normal.png"),item(835,430,r"Imagenes_Sprites\items\item_normal.png"),
               item(338,200,r"Imagenes_Sprites\items\item_normal.png"),item(398,200,r"Imagenes_Sprites\items\item_normal.png"),item(458,200,r"Imagenes_Sprites\items\item_normal.png"),
               item(518,200,r"Imagenes_Sprites\items\item_normal.png"),item(578,200,r"Imagenes_Sprites\items\item_normal.png"),item(638,200,r"Imagenes_Sprites\items\item_normal.png"),
               item(698,200,r"Imagenes_Sprites\items\item_normal.png"),
               item(431,630,r"Imagenes_Sprites\items\item_normal.png"),item(491,630,r"Imagenes_Sprites\items\item_normal.png"),item(551,630,r"Imagenes_Sprites\items\item_normal.png"),
               item(611,630,r"Imagenes_Sprites\items\item_normal.png"),item(671,630,r"Imagenes_Sprites\items\item_normal.png"),item(731,630,r"Imagenes_Sprites\items\item_normal.png"),
               item(791,630,r"Imagenes_Sprites\items\item_normal.png"),item(851,630,r"Imagenes_Sprites\items\item_normal.png"),item(911,630,r"Imagenes_Sprites\items\item_normal.png"),
               item(180,500,r"Imagenes_Sprites\items\item_normal.png"),item(240,500,r"Imagenes_Sprites\items\item_normal.png"),item(300,500,r"Imagenes_Sprites\items\item_normal.png"),
               item(360,500,r"Imagenes_Sprites\items\item_normal.png"),item(1000,500,r"Imagenes_Sprites\items\item_especial_vidas.png",True,True),item(229,358,r"Imagenes_Sprites\items\item_espada.png",True,False,True),
               item(285,115,r"Imagenes_Sprites\items\item_normal.png"),item(345,115,r"Imagenes_Sprites\items\item_normal.png"),item(405,115,r"Imagenes_Sprites\items\item_normal.png"),
               item(465,115,r"Imagenes_Sprites\items\item_normal.png"),item(525,115,r"Imagenes_Sprites\items\item_normal.png"),item(585,115,r"Imagenes_Sprites\items\item_normal.png"),
               item(645,115,r"Imagenes_Sprites\items\item_normal.png"),item(705,115,r"Imagenes_Sprites\items\item_normal.png"),
               item(280,160,r"Imagenes_Sprites\items\item_normal.png"),item(340,160,r"Imagenes_Sprites\items\item_normal.png"),item(400,160,r"Imagenes_Sprites\items\item_normal.png"),
               item(460,160,r"Imagenes_Sprites\items\item_normal.png"),item(520,160,r"Imagenes_Sprites\items\item_normal.png"),item(580,160,r"Imagenes_Sprites\items\item_normal.png"),
               item(640,160,r"Imagenes_Sprites\items\item_normal.png"),item(700,160,r"Imagenes_Sprites\items\item_normal.png"),
               
               item(185,315,r"Imagenes_Sprites\items\item_normal.png"),item(245,315,r"Imagenes_Sprites\items\item_normal.png"),item(305,315,r"Imagenes_Sprites\items\item_normal.png"),
               item(365,315,r"Imagenes_Sprites\items\item_normal.png"),item(425,315,r"Imagenes_Sprites\items\item_normal.png"),item(485,315,r"Imagenes_Sprites\items\item_normal.png"),
               item(545,315,r"Imagenes_Sprites\items\item_normal.png"),item(605,315,r"Imagenes_Sprites\items\item_normal.png"),

               item(185,365,r"Imagenes_Sprites\items\item_normal.png"),item(245,365,r"Imagenes_Sprites\items\item_normal.png"),item(305,365,r"Imagenes_Sprites\items\item_normal.png"),
               item(365,365,r"Imagenes_Sprites\items\item_normal.png"),item(425,365,r"Imagenes_Sprites\items\item_normal.png"),item(485,365,r"Imagenes_Sprites\items\item_normal.png"),
               item(545,365,r"Imagenes_Sprites\items\item_normal.png"),item(605,365,r"Imagenes_Sprites\items\item_normal.png"),
               
               item(180,450,r"Imagenes_Sprites\items\item_normal.png"),item(240,450,r"Imagenes_Sprites\items\item_normal.png"),item(300,450,r"Imagenes_Sprites\items\item_normal.png"),
               item(360,450,r"Imagenes_Sprites\items\item_normal.png")
               
               ]
lista_trampas_nivel_1 = [Trampas(785,106,(50,50),PANTALLA,trampa,True,106,420,3,True),Trampas(169,473,(50,50),PANTALLA,trampa,True,169,640,3)]

################################# CONFIGURACION NIVEL 2 #################################

#PLATAFORMAS NIVEL 2
plataformas_nivel_2 = [Plataformas((130,30),0,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((130,30),130,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((130,30),260,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((130,30),390,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((130,30),520,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((130,30),650,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((130,30),780,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((130,30),910,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((130,30),1040,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((130,30),1170,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((130,30),1300,H-30,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        
        Plataformas((140,50),145,150,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((140,50),285,150,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((140,50),425,150,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((140,50),565,150,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((140,50),705,150,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((140,50),845,150,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((140,50),985,150,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((140,50),1125,150,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        
        Plataformas((86,30),150,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),236,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),322,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((86,30),408,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),494,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),580,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((86,30),752,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),838,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),924,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((50,30),1220,288,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True,True,288,640,3,True),

        Plataformas((86,30),150,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),236,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),322,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((86,30),408,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),494,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),580,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((86,30),752,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),838,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),924,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((86,30),1010,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),1096,406,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        
        Plataformas((86,30),150,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),236,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),322,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((86,30),408,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),494,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),580,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((86,30),752,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),838,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),924,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),
        Plataformas((86,30),1010,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),Plataformas((86,30),1096,523,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True),

        Plataformas((100,20),11,250,r"Imagenes_Sprites\Plataformas\plataforma_tronco.png",True,True,250,650,5,True)
        
]

#ENEMIGOS
lista_enemigos_nivel_2 = [Enemigo(diccionario_enemigo,250,630,100,20,250,1000),Enemigo(diccionario_enemigo,156,360,100,20,156,658),
                          Enemigo(diccionario_enemigo_2,149,238,100,50,149,658),Enemigo(diccionario_enemigo_3,250,560,100,100,250,1005),
                          Enemigo(diccionario_enemigo_2,753,360,100,50,753,1005)]


#ITEMS
lista_items_nivel_2 = [item(760,470,r"Imagenes_Sprites\items\item_normal.png"),item(820,470,r"Imagenes_Sprites\items\item_normal.png"),item(880,470,r"Imagenes_Sprites\items\item_normal.png"),
               item(940,470,r"Imagenes_Sprites\items\item_normal.png"),item(1000,470,r"Imagenes_Sprites\items\item_normal.png"),item(1060,470,r"Imagenes_Sprites\items\item_normal.png"),
               item(1120,470,r"Imagenes_Sprites\items\item_normal.png"),

               item(158,200,r"Imagenes_Sprites\items\item_normal.png"),item(218,200,r"Imagenes_Sprites\items\item_normal.png"),item(278,200,r"Imagenes_Sprites\items\item_normal.png"),
               item(338,200,r"Imagenes_Sprites\items\item_normal.png"),item(398,200,r"Imagenes_Sprites\items\item_normal.png"),item(458,200,r"Imagenes_Sprites\items\item_normal.png"),
               item(518,200,r"Imagenes_Sprites\items\item_normal.png"),item(578,200,r"Imagenes_Sprites\items\item_normal.png"),item(518,240,r"Imagenes_Sprites\items\item_especial_vidas.png",True,True),
               item(500,560,r"Imagenes_Sprites\items\item_espada.png",True,False,True),
               item(158,245,r"Imagenes_Sprites\items\item_normal.png"),item(218,245,r"Imagenes_Sprites\items\item_normal.png"),item(278,245,r"Imagenes_Sprites\items\item_normal.png"),
               item(338,245,r"Imagenes_Sprites\items\item_normal.png"),item(398,245,r"Imagenes_Sprites\items\item_normal.png"),item(458,245,r"Imagenes_Sprites\items\item_normal.png"),
               item(518,245,r"Imagenes_Sprites\items\item_normal.png"),item(578,245,r"Imagenes_Sprites\items\item_normal.png"),

               item(431,630,r"Imagenes_Sprites\items\item_normal.png"),item(491,630,r"Imagenes_Sprites\items\item_normal.png"),item(551,630,r"Imagenes_Sprites\items\item_normal.png"),
               item(611,630,r"Imagenes_Sprites\items\item_normal.png"),item(671,630,r"Imagenes_Sprites\items\item_normal.png"),item(731,630,r"Imagenes_Sprites\items\item_normal.png"),
               item(791,630,r"Imagenes_Sprites\items\item_normal.png"),item(851,630,r"Imagenes_Sprites\items\item_normal.png"),item(911,630,r"Imagenes_Sprites\items\item_normal.png"),

               item(180,470,r"Imagenes_Sprites\items\item_normal.png"),item(240,470,r"Imagenes_Sprites\items\item_normal.png"),item(300,470,r"Imagenes_Sprites\items\item_normal.png"),
               item(360,470,r"Imagenes_Sprites\items\item_normal.png"),item(420,470,r"Imagenes_Sprites\items\item_normal.png"),item(480,470,r"Imagenes_Sprites\items\item_normal.png"),
               item(540,470,r"Imagenes_Sprites\items\item_normal.png"),item(600,470,r"Imagenes_Sprites\items\item_normal.png"),

               item(164,102,r"Imagenes_Sprites\items\item_normal.png"),item(224,102,r"Imagenes_Sprites\items\item_normal.png"),item(284,102,r"Imagenes_Sprites\items\item_normal.png"),
               item(344,102,r"Imagenes_Sprites\items\item_normal.png"),item(404,102,r"Imagenes_Sprites\items\item_normal.png"),item(464,102,r"Imagenes_Sprites\items\item_normal.png"),
               item(524,102,r"Imagenes_Sprites\items\item_normal.png"),item(584,102,r"Imagenes_Sprites\items\item_normal.png"),item(644,102,r"Imagenes_Sprites\items\item_normal.png"),
               item(704,102,r"Imagenes_Sprites\items\item_normal.png"),item(764,102,r"Imagenes_Sprites\items\item_normal.png"),item(824,102,r"Imagenes_Sprites\items\item_normal.png"),
               item(884,102,r"Imagenes_Sprites\items\item_normal.png"),item(944,102,r"Imagenes_Sprites\items\item_normal.png"),item(1004,102,r"Imagenes_Sprites\items\item_normal.png"),
               item(1064,102,r"Imagenes_Sprites\items\item_normal.png"),item(1124,102,r"Imagenes_Sprites\items\item_normal.png"),
               

               item(760,240,r"Imagenes_Sprites\items\item_normal.png"),item(820,240,r"Imagenes_Sprites\items\item_normal.png"),item(880,240,r"Imagenes_Sprites\items\item_normal.png"),
               item(940,240,r"Imagenes_Sprites\items\item_normal.png"),

               item(760,313,r"Imagenes_Sprites\items\item_normal.png"),item(820,313,r"Imagenes_Sprites\items\item_normal.png"),item(880,313,r"Imagenes_Sprites\items\item_normal.png"),
               item(940,313,r"Imagenes_Sprites\items\item_normal.png"),

               item(760,360,r"Imagenes_Sprites\items\item_normal.png"),item(820,360,r"Imagenes_Sprites\items\item_normal.png"),item(880,360,r"Imagenes_Sprites\items\item_normal.png"),
               item(940,360,r"Imagenes_Sprites\items\item_normal.png"),

               item(158,328,r"Imagenes_Sprites\items\item_normal.png"),item(218,328,r"Imagenes_Sprites\items\item_normal.png"),item(278,328,r"Imagenes_Sprites\items\item_normal.png"),
               item(338,328,r"Imagenes_Sprites\items\item_normal.png"),item(398,328,r"Imagenes_Sprites\items\item_normal.png"),item(458,328,r"Imagenes_Sprites\items\item_normal.png"),
               item(518,328,r"Imagenes_Sprites\items\item_normal.png"),item(578,328,r"Imagenes_Sprites\items\item_normal.png"),

               item(158,370,r"Imagenes_Sprites\items\item_normal.png"),item(218,370,r"Imagenes_Sprites\items\item_normal.png"),item(278,370,r"Imagenes_Sprites\items\item_normal.png"),
               item(338,370,r"Imagenes_Sprites\items\item_normal.png"),item(398,370,r"Imagenes_Sprites\items\item_normal.png"),item(458,370,r"Imagenes_Sprites\items\item_normal.png"),
               item(518,370,r"Imagenes_Sprites\items\item_normal.png"),item(578,370,r"Imagenes_Sprites\items\item_normal.png")]

lista_trampas_nivel_2 = [Trampas(685,208,(50,50),PANTALLA,trampa,True,208,600,3,True),Trampas(169,470,(50,50),PANTALLA,trampa,True,169,640,3)]

################################# CONFIGURACION NIVEL 3 #################################
#BOSS
#boss = Boss(acciones_boss,850,150,(480,332),3)
#PLATAFORMAS NIVEL 3
plataformas_nivel_3 = [Plataformas((130,30),0,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((130,30),130,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((130,30),260,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),
        Plataformas((130,30),390,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((130,30),520,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((130,30),650,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),
        Plataformas((130,30),780,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((130,30),910,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((130,30),1040,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),
        Plataformas((130,30),1170,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((130,30),1300,H-30,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),
        Plataformas((86,30),150,406,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),236,406,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),322,406,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),
        Plataformas((86,30),408,406,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),494,406,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),580,406,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),
        Plataformas((86,30),666,440,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),155,543,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),241,543,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),
        Plataformas((86,30),16,290,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),102,290,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),17,200,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True,True,17,850,3),
        
        Plataformas((86,30),840,450,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),900,450,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),986,450,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),
        Plataformas((86,30),1072,450,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((86,30),1158,450,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True),Plataformas((41,20),776,522,r"Imagenes_Sprites\Plataformas\plataforma_piedra.png",True,True,522,641,2,True)]

#ENEMIGOS
lista_enemigos_nivel_3 = [Enemigo(diccionario_enemigo_3,100,550,100,100,100,1200),Enemigo(diccionario_enemigo,200,600,100,20,200,800),
                          Enemigo(diccionario_enemigo,100,610,100,20,100,800),Enemigo(diccionario_enemigo,400,600,100,20,400,1300)]


#ITEMS
lista_items_nivel_3 = [item(20,156,r"Imagenes_Sprites\items\item_normal.png"),item(80,156,r"Imagenes_Sprites\items\item_normal.png"),item(140,156,r"Imagenes_Sprites\items\item_normal.png"),
                       item(220,156,r"Imagenes_Sprites\items\item_normal.png"),
                       item(20,200,r"Imagenes_Sprites\items\item_normal.png"),item(80,200,r"Imagenes_Sprites\items\item_normal.png"),item(140,200,r"Imagenes_Sprites\items\item_normal.png"),
                       item(220,200,r"Imagenes_Sprites\items\item_normal.png"),
                       item(20,244,r"Imagenes_Sprites\items\item_normal.png"),item(80,244,r"Imagenes_Sprites\items\item_normal.png"),item(140,244,r"Imagenes_Sprites\items\item_normal.png"),
                       item(220,244,r"Imagenes_Sprites\items\item_normal.png"),item(760,417,r"Imagenes_Sprites\items\item_especial_vidas.png",True,True),
                       item(155,330,r"Imagenes_Sprites\items\item_normal.png"),item(215,330,r"Imagenes_Sprites\items\item_normal.png"),item(215,330,r"Imagenes_Sprites\items\item_normal.png"),
                       item(215,330,r"Imagenes_Sprites\items\item_normal.png"),item(275,330,r"Imagenes_Sprites\items\item_normal.png"),item(335,330,r"Imagenes_Sprites\items\item_normal.png"),
                       item(395,330,r"Imagenes_Sprites\items\item_normal.png"),item(455,330,r"Imagenes_Sprites\items\item_normal.png"),item(515,330,r"Imagenes_Sprites\items\item_normal.png"),
                       item(575,330,r"Imagenes_Sprites\items\item_normal.png"),item(635,330,r"Imagenes_Sprites\items\item_normal.png"),
                       item(155,370,r"Imagenes_Sprites\items\item_normal.png"),item(215,370,r"Imagenes_Sprites\items\item_normal.png"),item(215,370,r"Imagenes_Sprites\items\item_normal.png"),
                       item(215,370,r"Imagenes_Sprites\items\item_normal.png"),item(275,370,r"Imagenes_Sprites\items\item_normal.png"),item(335,370,r"Imagenes_Sprites\items\item_normal.png"),
                       item(395,370,r"Imagenes_Sprites\items\item_normal.png"),item(455,370,r"Imagenes_Sprites\items\item_normal.png"),item(515,370,r"Imagenes_Sprites\items\item_normal.png"),
                       item(575,370,r"Imagenes_Sprites\items\item_normal.png"),item(635,370,r"Imagenes_Sprites\items\item_normal.png"),item(161,447,r"Imagenes_Sprites\items\item_normal.png"),
                       item(221,447,r"Imagenes_Sprites\items\item_normal.png"),item(281,447,r"Imagenes_Sprites\items\item_normal.png"),item(341,447,r"Imagenes_Sprites\items\item_normal.png"),
                       item(161,491,r"Imagenes_Sprites\items\item_normal.png"),item(221,491,r"Imagenes_Sprites\items\item_normal.png"),item(281,491,r"Imagenes_Sprites\items\item_normal.png"),
                       item(341,491,r"Imagenes_Sprites\items\item_normal.png"),item(385,290,r"Imagenes_Sprites\items\item_espada.png",True,False,True)]

lista_trampas_nivel_3 = [Trampas(166,340,(50,50),PANTALLA,trampa,True,166,800,3),Trampas(396,448,(50,50),PANTALLA,trampa),Trampas(31,105,(50,50),PANTALLA,trampa,True,31,850,5),
                         Trampas(58,338,(50,50),PANTALLA,trampa,True,338,550,5,True)]
