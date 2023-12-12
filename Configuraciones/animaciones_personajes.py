from Configuraciones.config import *

#PERSONAJE PRINCIPAL
acciones = {}
acciones["Quieto_derecha"] = personaje_quieto_derecha
acciones["Quieto_izquierda"] = personaje_quieto_izquierda
acciones["Derecha"] = personaje_camina_derecha  
acciones["Izquierda"] = personaje_camina_izquierda
acciones["Saltar_derecha"] = personaje_salta_derecha
acciones["Saltar_izquierda"] = personaje_salta_izquierda
acciones["ataque_derecha"] = personaje_ataca_derecha
acciones["ataque_izquierda"] = personaje_ataca_izquierda
acciones["ataque_especial_derecha"] = personaje_ataque_especial_derecha
acciones["ataque_especial_izquierda"] = personaje_ataque_especial_izquierda
acciones["danado"] = personaje_danado
acciones["danado_izquierda"] = personaje_danado_izquierda
acciones["camina_danado"] = personaje_danado_camina
acciones["camina_danado_izquierda"] = personaje_danado_camina_izquierda
acciones["danado_saltar"] = personaje_danado_saltar
acciones["danado_saltar_izquierda"] = personaje_danado_saltar_izquierda

#ENEMIGOS
#enemigo 1
diccionario_enemigo = {}
diccionario_enemigo["izquierda"] = enemigo_camina
diccionario_enemigo["derecha"] = enemigo_camina_derecha
diccionario_enemigo["atacado"] = enemigo_atacado

#enemigo 2
diccionario_enemigo_2 = {}
diccionario_enemigo_2["izquierda"] = enemigo_2_camina
diccionario_enemigo_2["derecha"] = enemigo_2_camina_derecha
diccionario_enemigo_2["atacado"] = enemigo_2_atacado

#enemigo 3
diccionario_enemigo_3 = {}
diccionario_enemigo_3["izquierda"] = enemigo_3_camina_izquierda
diccionario_enemigo_3["derecha"] = enemigo_3_camina
diccionario_enemigo_3["atacado"] = enemigo_3_atacado

#BOSS FINAL
acciones_boss = {}
acciones_boss["Quieto_izquierda"] = boss_final_quieto_izquierda
acciones_boss["Saltar_derecha"] = boss_final_salta
acciones_boss["Saltar_izquierda"] = boss_final_salta_izquierda
acciones_boss["ataque_especial_izquierda"] = boss_final_ataca_izquierda

acciones_boss["atacado_izquierda"] = boss_final_atacado_izquierda
acciones_boss["muriendo_izquierda"] = boss_final_muriendo_izquierda


disparo = {}
disparo["izquierda"] = disparo_izquierda
disparo["derecha"] = disparo_derecha