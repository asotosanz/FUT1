"""
RAZONABLEMENTE ENTENDIDA =========================
main.py
Punto de entrada del proyecto.

Primer paso: dibujar el terreno de juego y colocar 4 jugadores por
equipo. Todavía no hay balón, ni tiempo, ni posesión: eso vendrá
en los siguientes pasos, reutilizando esta misma base.
"""

import matplotlib.pyplot as plt

from pitch import dibujar_campo
from players import crear_equipo_prueba


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

    plt.title("Terreno de juego — 4 jugadores por equipo")
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