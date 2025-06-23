"""
# [M4.L1] Carrera de tortugas - Actividad # 3: "Campo de carrera"
# NOTA: Ésta es la primera actividad práctica del Proyecto, (1 y 2 son teoría)

# Objetivo: Crear una tortuga y programar el dibujo de la pista de carreras

Paso Nº 1) Importar turtle y crear nuestra tortuga
Paso Nº 2) Dibujar nuestra pista de carreras
            -> Definir la cant. de carriles
            -> Definir el ancho de cada carril
            *entre ambos valores van a definir la lognitud de la pista*

            -> Definir espacio para corredores
            *tener en cuenta la cantidad de tortugas que participarán y dejar espacio entre ellas*
            
# Link al repo de GitHub: https://github.com/rodrigovittori/Carrera-de-Tortugas-6646
"""
import turtle

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

######################################

# Colorín colorado el código ha terminado :D