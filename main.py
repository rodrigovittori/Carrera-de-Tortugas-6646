"""
# [M4.L1] Carrera de tortugas - Actividad # 6 "Moviendo a las dos"
# Objetivo: Configurar el avance de nuestras tortugas

NOTA: El movimiento de la tercer tortuga lo implementaremos en el próximo ejercicio

Paso Nº 1: Crear variable que contenga la distancia que debe recorrer una tortuga para ganar
Paso Nº 2: Agregar bucle donde pidamos predicción del resultado al jugador
Paso Nº 3: Agregamos variables que registren el avance de CADA tortuga
Paso Nº 4: Agregamos OTRA variable que registrará si una tortuga ya ha cruzado la meta (tenemos_ganadora)
Paso Nº 5: Agregamos el bucle de la carrera: while(not tenemos_ganadora)
-> incluír random
Paso Nº 6: En cada iteración del bucle:
            1º) Verificamos (if) si alguna cruzó la meta -> hay ganadora
            2º) Si NINGUNA ha cruzado la meta... las haremos avanzar un cantidad random cada ronda
Paso Nº 7: Agregamos una condición para mostrar el resultado de la carrera
            
# Link al repo de GitHub: https://github.com/rodrigovittori/Carrera-de-Tortugas-6646
"""
import turtle
import random

"""   ##########################
     # > VARIABLES GLOBALES < #
    ##########################    """

velocidad_corredores = 5        # Controla la velocidad de la animación (no a la que "corren", sino a la que las dibujamos)
cant_tortugas = 0               # Contador con la cantidad de corredores (hasta ahora)
distancia_entre_tortugas = 40   # Distancia (en px) que hay verticalmente entre corredoras
y_inicial_tortugas = 80
x_inicial_tortugas = -230

"""   #########################
     # > PISTA DE CARRERAS < #
    #########################    """

# Tortuga que dibuja el tablero 🐢 (t)
t = turtle.Turtle() # Creamos la tortuga
t.penup()           # Levantamos el trazo
t.goto(-200, 100)   # Buscamos más espacio para la pista
t.pendown()         # Volvemos a dibujar
t.speed(0)          # Aceleramos la animiación de la tortuga
t.color(0,0,0)      # Seteo el color de dibujo a negro

# Pista de carreras
cant_secciones_pista = 15
ancho_secciones_pista = 20
# ¿Cuántos píxeles tiene que recorrer la tortuga hasta cruzar la meta?
# Distancia de carrera = cant_secciones_pista * ancho_secciones_pista
long_secciones_pista = 150 # "altura" de la pista

# Bucle que dibuja la pista:
for pista in range(1, (1 + cant_secciones_pista)):
    t.write(str(pista))         # Escribe el Nº de la sección (1~15)
    t.right(90)                 # Gira 90º (mirando hacia abajo)
    t.fd(long_secciones_pista)  # Dibuja la línea vertical de la sección
    t.bk(long_secciones_pista)  # Retrocede y "vuelve" arriba
    t.left(90)                  # Reposiciona la tortuga para que mire a la dcha
    t.fd(ancho_secciones_pista) # Avanza el ancho hasta la próxima sección

# -> Inserte aquí código bandera meta
t.color(255, 0, 0)
t.right(90)
t.fd(long_secciones_pista)
t.bk(long_secciones_pista)
t.left(90)
t.color("black")

""" ************************************************************************************************ """

"""   #############################
     # > CORREDORAS (TORTUGAS) < #
    #############################    """

# PRIMERA
primera = turtle.Turtle()              # Creamos una nueva tortuga
cant_tortugas += 1                     # La registramos como corredora
primera.shape("turtle")                # Le damos forma de tortuga
primera.color("crimson")               # Le asignamos otro color (ROJO)
primera.speed(0)                       # Aceleramos su animación
primera.penup()                        # Levantamos el trazo para reubicarla

# La posicionamos DETRÁS de la línea de partida
#primera.goto(-230, 80)
primera.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
primera.speed(velocidad_corredores)    # Cambiamos su velocidad de animación para la carrera

########################################
# SEGUNDA
segunda = turtle.Turtle()              # Creamos una nueva tortuga
cant_tortugas += 1                     # La registramos como corredora
segunda.shape("turtle")                # Le damos forma de tortuga
segunda.color("navy")                  # Le asignamos otro color (AZUL)
segunda.speed(0)                       # Aceleramos su animación
segunda.penup()                        # Levantamos el trazo para reubicarla

# La posicionamos DETRÁS de la línea de partida
#segunda.goto(-230, 40)
segunda.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
segunda.speed(velocidad_corredores)    # Cambiamos su velocidad de animación para la carrera

########################################

# TERCERA
tercera = turtle.Turtle()              # Creamos una nueva tortuga
cant_tortugas += 1                     # La registramos como corredora
tercera.shape("turtle")                # Le damos forma de tortuga
tercera.color("gold")                  # Le asignamos otro color (AZUL)
tercera.speed(0)                       # Aceleramos su animación
tercera.penup()                        # Levantamos el trazo para reubicarla

# La posicionamos DETRÁS de la línea de partida
#tercera.goto(-230, 0)
tercera.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
tercera.speed(velocidad_corredores)    # Cambiamos su velocidad de animación para la carrera

########################################

"""   ###############
     # > CARRERA < #
    ###############    """

distancia_a_la_meta = ((cant_secciones_pista + 1) * ancho_secciones_pista)

##################### >>> PREDICCIÓN DEL USUARIO <<< #####################

opcion_jugador = 0 # Vble global pero la declaramos acá por legibilidad del código

# Si es un num negativo, o un num no-asignado, pedimos de nuevo
while (opcion_jugador <= 0 or opcion_jugador > cant_tortugas):
    opcion_jugador = int(input("Cual tortuga cree que ganara? (1/2/3): "))

# Nota: Usaremos la predicción del usuario para mostrar un mensaje
# Reutilizaremos la tortuga t (que dibujó nuestra pista de carreras)
t.penup()
t.goto((x_inicial_tortugas + distancia_a_la_meta /2), (distancia_entre_tortugas * cant_tortugas) )
t.write( ("Apostaste por la tortuga #" + str(opcion_jugador)), align = 'center')
t.hideturtle() # Escondemos nuestra tortuga por cuestiones estéticas

##########################################################################

tenemos_ganadora = False # Vble de control que detendrá el bucle de la carrera cuando haya una ganadora
tortuga_ganadora = 0     # Vable que contiene la id de nuestra ganadora

paso_tortuga = 0         # Variable que randomizamos para cada tortuga en cada ronda de "avances"

# agregamos variables acumuladoras que registren la distancia total recorrida por cada tortuga
distancia_recorrida_tortuga_1 = 0
distancia_recorrida_tortuga_2 = 0
distancia_recorrida_tortuga_3 = 0

"""
Paso Nº 5: Agregamos el bucle de la carrera: while(not tenemos_ganadora)
-> incluír random
Paso Nº 6: En cada iteración del bucle:
            1º) Verificamos (if) si alguna cruzó la meta -> hay ganadora
            2º) Si NINGUNA ha cruzado la meta... las haremos avanzar un cantidad random cada ronda"""

######################### >>> BUCLE PRINCIPAL <<< ########################
while (not tenemos_ganadora):
    # Verificamos si ALGUNA tortuga ya cruzó la meta:
    if (distancia_recorrida_tortuga_1 > distancia_a_la_meta):
        # Si la primera tortuga pasó la línea de meta:
        tortuga_ganadora = 1
        tenemos_ganadora = True

    elif (distancia_recorrida_tortuga_2 > distancia_a_la_meta):
        # Si la segunda tortuga pasó la línea de meta:
        tortuga_ganadora = 2
        tenemos_ganadora = True

    elif (distancia_recorrida_tortuga_3 > distancia_a_la_meta):
        # Si la tercera tortuga pasó la línea de meta:
        tortuga_ganadora = 3
        tenemos_ganadora = True

    else: # NO HAY GANADORA -> LA CARRERA CONTINÚA

        paso_tortuga = random.randint(1, velocidad_corredores) # Cant de px que avanzará la tortuga esta ronda
        primera.fd(paso_tortuga)                               # Avanza en la pista
        distancia_recorrida_tortuga_1 += paso_tortuga          # registro la distancia recorrida

        paso_tortuga = random.randint(1, velocidad_corredores) # Cant de px que avanzará la tortuga esta ronda
        segunda.fd(paso_tortuga)                               # Avanza en la pista
        distancia_recorrida_tortuga_2 += paso_tortuga          # registro la distancia recorridaç

        # ** IMPLEMENTAR TERCER TORTUGA AQUÍ **

##########################################################################

# > Si estás aquí, la carrera terminó :D

# MOSTRAR TORTUGA GANADORA:
t.penup()
t.goto(x_inicial_tortugas + 100, -80)
win_text = "¡La tortuga #" + str(tortuga_ganadora) + " ha ganado!"
t.write(win_text)

# To-do: agregar condición que compare nuestra predicción con el resultado

""" Colorín colorado el código ha terminado :D """