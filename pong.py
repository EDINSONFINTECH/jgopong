# A continuacion esta el desarrollo del problema, Agregare nuevamente el Enunciado, pero 
# la recomendacion es ver el Archivo de texto anexo llamado: jgoarcadepong.py
# ----******-----
# JUEGO ARCADE PONG:  Reproduce el clásico juego de arcade Pong.
# Para ello puedes usar el módulo "turtle" para crear los componentes 
# del juego y detectar las colisiones de la pelota con las paletas de los jugadores.
# También puedes definir una serie de asignaciones de teclas para establecer los 
# controles del usuario para las paletas de los jugadores izquierda y derecha. 
# --- *** ---

# Primero Importamos: "import turtle"  ya es una funcion incorporada
import turtle  
# Recuerde que> Este módulo te permitirá crear la ventana del juego, las paletas, la pelota y el marcador.
# Crear la ventana del juego
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Crear las paletas de los jugadores
paleta_a = turtle.Turtle()
paleta_a.speed(0)
paleta_a.shape("square")
paleta_a.color("white")
paleta_a.shapesize(stretch_wid=5, stretch_len=1)
paleta_a.penup()
paleta_a.goto(-350, 0)

paleta_b = turtle.Turtle()
paleta_b.speed(0)
paleta_b.shape("square")
paleta_b.color("white")
paleta_b.shapesize(stretch_wid=5, stretch_len=1)
paleta_b.penup()
paleta_b.goto(350, 0)

# Crear la pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.3 # desplazamiento en x
pelota.dy = 0.3 # desplazamiento en y

# Crear las variables para la puntuación de los jugadores
marcador_a = 0
marcador_b = 0

# Crear el marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write(f"Jugador A: {marcador_a} Jugador B: {marcador_b}", align="center", font=("Courier", 24, "normal"))

# Definir las funciones para mover las paletas hacia arriba y hacia abajo
def paleta_a_arriba():
    y = paleta_a.ycor() # obtiene la coordenada y de la paleta a
    y += 20 # le suma 20 unidades
    paleta_a.sety(y) # actualiza la coordenada y de la paleta a

def paleta_a_abajo():
    y = paleta_a.ycor() # obtiene la coordenada y de la paleta a
    y -= 20 # le resta 20 unidades
    paleta_a.sety(y) # actualiza la coordenada y de la paleta a

def paleta_b_arriba():
    y = paleta_b.ycor() # obtiene la coordenada y de la paleta b
    y += 20 # le suma 20 unidades
    paleta_b.sety(y) # actualiza la coordenada y de la paleta b

def paleta_b_abajo():
    y = paleta_b.ycor() # obtiene la coordenada y de la paleta b
    y -= 20 # le resta 20 unidades
    paleta_b.sety(y) # actualiza la coordenada y de la paleta b

# Asignar las teclas para controlar el movimiento de las paletas
ventana.listen()
ventana.onkeypress(paleta_a_arriba, "w")
ventana.onkeypress(paleta_a_abajo, "s")
ventana.onkeypress(paleta_b_arriba, "Up")
ventana.onkeypress(paleta_b_abajo, "Down")

# Crear un bucle infinito para actualizar el juego
while True:
    ventana.update()

    # Actualizar la posición de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Detectar las colisiones con los bordes de la pantalla
    if pelota.ycor() > 290: # borde superior
        pelota.sety(290)
        pelota.dy *= -1 # cambiar el signo del desplazamiento en y
    
    if pelota.ycor() < -290: # borde inferior
        pelota.sety(-290)
        pelota.dy *= -1 # cambiar el signo del desplazamiento en y
    
    if pelota.xcor() > 390: # borde derecho
        pelota.goto(0, 0) # volver al centro de la pantalla
        pelota.dx *= -1 # cambiar el signo del desplazamiento en x
        marcador_a += 1 # incrementar el marcador del jugador a
        marcador.clear() # borrar el texto anterior del marcador
        marcador.write(f"Jugador A: {marcador_a} Jugador B: {marcador_b}", align="center", font=("Courier", 24, "normal")) # escribir el nuevo texto del marcador
    
    if pelota.xcor() < -390: # borde izquierdo
        pelota.goto(0, 0) # volver al centro de la pantalla
        pelota.dx *= -1 # cambiar el signo del desplazamiento en x
        marcador_b += 1 # incrementar el marcador del jugador b
        marcador.clear() # borrar el texto anterior del marcador
        marcador.write(f"Jugador A: {marcador_a} Jugador B: {marcador_b}", align="center", font=("Courier", 24, "normal")) # escribir el nuevo texto del marcador

    # Detectar las colisiones con las paletas de los jugadores
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < paleta_b.ycor() + 50 and pelota.ycor() > paleta_b.ycor() - 50): # lado derecho de la paleta b
        pelota.setx(340)
        pelota.dx *= -1 # cambiar el signo del desplazamiento en x
    
    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < paleta_a.ycor() + 50 and pelota.ycor() > paleta_a.ycor() - 50): # lado izquierdo de la paleta a
        pelota.setx(-340)
        pelota.dx *= -1 # cambiar el signo del desplazamiento en x


