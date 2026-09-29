"""
RAZONABLEMENTE ENTENDIDA =========================
main.py
Punto de entrada del proyecto.

Primer paso (ya hecho): dibujar el terreno de juego y colocar 4
jugadores por equipo.

Este paso añade, reutilizando esa misma base: el balón (con posesión
inicial de un jugador), el cálculo del diagrama de Voronoi de los 8
jugadores, y el bucle de tiempo (todavía sin mover a nadie: solo
para comprobar que las piezas encajan y que simular() corre bien
sobre el escenario real).
"""

import matplotlib.pyplot as plt

from pitch import dibujar_campo
from players import crear_equipo_prueba
from ball import Ball, dar_posesion
from voronoi import calcular_voronoi, graficar_voronoi
from simulacion import simular


def main():
    ax = dibujar_campo()        #guardo en ax el terreno de juego

    # vector de posiciones de los jugadores en el campo (en este caso específico 4)
    posiciones_own = [
        (15, 34),
        (30, 15),
        (30, 53),
        (45, 34),
    ]
    own = crear_equipo_prueba("own", ids_inicio=1, posiciones=posiciones_own)

    # vector de posiciones de los jugadores rivales
    posiciones_opp = [
        (40, 20),
        (40, 48),
        (55, 30),
        (55, 40),
    ]
    opp = crear_equipo_prueba("opp", ids_inicio=101, posiciones=posiciones_opp)

    # Todos los jugadores en juego, útil para las funciones que necesitan
    # mirar a los dos equipos a la vez (posesión, Voronoi conjunto...)
    todos = own + opp

    # --- BALÓN Y POSESIÓN -------------------------------------------
    # De momento el balón empieza en los pies del jugador 1 (own).
    # dar_posesion mueve el balón a su posición y marca tiene_balon=True
    # solo en él (y False en el resto de "todos").
    balon = Ball(x=own[0].x, y=own[0].y)
    dar_posesion(balon, own[0], todos)

    # --- VORONOI ------------------------------------------------------
    # Se calcula con los 8 jugadores a la vez (own y opp juntos), para
    # que las áreas de cada equipo ya "choquen" contra las del rival.
    # calcular_voronoi rellena el campo `area` de cada Player in-place.
    calcular_voronoi(own, opp)

    # --- BUCLE DE TIEMPO ------------------------------------------------
    # Todavía nadie se mueve: paso_fn es un marcador de posición para la
    # lógica que irá aquí más adelante (mover jugadores, mover el balón,
    # comprobar si cambia la posesión...). Por ahora solo confirma que
    # el bucle corre sobre el escenario real.
    def paso_fn(tiempo, dt):
        pass  # aquí irá la lógica de movimiento en el siguiente paso

    simular(paso_fn, dt=0.1, duracion=1.0)

    # Dibujar las áreas de Voronoi por debajo de los jugadores
    graficar_voronoi(ax, own, opp)

    # Dibujar equipo propio en azul
    for p in own:
        ax.scatter(p.x, p.y, c='dodgerblue', s=250, zorder=3, edgecolors='white')
        ax.text(p.x, p.y, p.label, color='white', ha='center', va='center',
                fontsize=8, zorder=4)

    # Dibujar equipo rival en rojo
    for p in opp:
        ax.scatter(p.x, p.y, c='crimson', s=250, zorder=3, edgecolors='white')
        ax.text(p.x, p.y, p.label, color='white', ha='center', va='center',
                fontsize=8, zorder=4)

    # Dibujar el balón (encima de todo, zorder más alto que los jugadores)
    ax.scatter(balon.x, balon.y, c='white', s=80, zorder=5,
               edgecolors='black', linewidths=1.5)

    plt.title("Terreno de juego — balón, jugadores y Voronoi")
    plt.savefig("terreno_4v4.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()

"""
EXPLICACIÓN DE __main__

si ejecutas un archivo directamente, por ejemplo players.py, entonces python crea una variable llamada __name__
y establece __name__ = "__main__"
si importas un archivo por ejemplo import players, entonces __name__ = "players" 

entonces la condición de __name__ == "__main__" se lee como:
si este archivo de está ejecutando directamente (sin ser importado) entonces haz lo que pone aquí.


"""