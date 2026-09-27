"""
pitch.py
Constantes y dibujo del terreno de juego (medidas reglamentarias FIFA).

Todo el resto de módulos del proyecto debe importar las medidas desde
aquí (FIELD_L, FIELD_W, etc.) en lugar de repetirlas, para que si algún
día cambias el sistema de coordenadas solo tengas que tocar un sitio.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, Rectangle

# =====================================
#   DIMENSIONES DEL TERRENO DE JUEGO
# =====================================

FIELD_L = 105.0   # largo
FIELD_W = 68.0    # ancho

# Área grande
PENALTY_AREA_L = 16.5   # profundidad
PENALTY_AREA_W = 40.32  # ancho

# Área pequeña
GOAL_AREA_L = 5.5
GOAL_AREA_W = 18.32

# Portería (longitud de la portería)
GOAL_W = 7.32

# Círculo central (radio del círculo central)
CENTER_CIRCLE_R = 9.15

# Punto de penalti (distancia desde la línea de fondo)
PENALTY_SPOT = 11.0

# Córners
CORNER_R = 1.0


def dibujar_campo(ax=None, figsize=(12, 8)):
    """
    Dibuja un campo de fútbol reglamentario sobre un Axes de matplotlib
    y lo devuelve, para que puedas seguir añadiendo jugadores, flechas,
    zonas de Voronoi, etc. encima.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=figsize)

    ax.set_xlim(-3, FIELD_L + 3)
    ax.set_ylim(-3, FIELD_W + 3)
    ax.set_aspect('equal')
    ax.set_facecolor('#2e8b57')  # verde césped

    # Líneas exteriores
    ax.add_patch(Rectangle((0, 0), FIELD_L, FIELD_W,
                            fill=False, edgecolor='white', linewidth=2))

    # Línea de medio campo
    ax.plot([FIELD_L / 2, FIELD_L / 2], [0, FIELD_W],
            color='white', linewidth=2)

    # Círculo central
    ax.add_patch(Circle((FIELD_L / 2, FIELD_W / 2), CENTER_CIRCLE_R,
                         fill=False, edgecolor='white', linewidth=2))
    ax.plot(FIELD_L / 2, FIELD_W / 2, 'wo', markersize=3)

    # Áreas grandes (izquierda y derecha)
    ax.add_patch(Rectangle((0, (FIELD_W - PENALTY_AREA_W) / 2),
                            PENALTY_AREA_L, PENALTY_AREA_W,
                            fill=False, edgecolor='white', linewidth=2))
    ax.add_patch(Rectangle((FIELD_L - PENALTY_AREA_L, (FIELD_W - PENALTY_AREA_W) / 2),
                            PENALTY_AREA_L, PENALTY_AREA_W,
                            fill=False, edgecolor='white', linewidth=2))

    # Áreas pequeñas
    ax.add_patch(Rectangle((0, (FIELD_W - GOAL_AREA_W) / 2),
                            GOAL_AREA_L, GOAL_AREA_W,
                            fill=False, edgecolor='white', linewidth=2))
    ax.add_patch(Rectangle((FIELD_L - GOAL_AREA_L, (FIELD_W - GOAL_AREA_W) / 2),
                            GOAL_AREA_L, GOAL_AREA_W,
                            fill=False, edgecolor='white', linewidth=2))

    # Puntos de penalti
    ax.plot(PENALTY_SPOT, FIELD_W / 2, 'wo', markersize=3)
    ax.plot(FIELD_L - PENALTY_SPOT, FIELD_W / 2, 'wo', markersize=3)

    # Semicírculos del área
    ax.add_patch(Arc((PENALTY_SPOT, FIELD_W / 2), 18.3, 18.3,
                      theta1=-53, theta2=53, edgecolor='white', linewidth=2))
    ax.add_patch(Arc((FIELD_L - PENALTY_SPOT, FIELD_W / 2), 18.3, 18.3,
                      theta1=127, theta2=233, edgecolor='white', linewidth=2))

    # Córners
    for cx, cy, t1, t2 in [(0, 0, 0, 90), (0, FIELD_W, 270, 360),
                            (FIELD_L, 0, 90, 180), (FIELD_L, FIELD_W, 180, 270)]:
        ax.add_patch(Arc((cx, cy), 2 * CORNER_R, 2 * CORNER_R,
                          theta1=t1, theta2=t2, edgecolor='white', linewidth=2))

    ax.set_xticks([])
    ax.set_yticks([])
    return ax


if __name__ == "__main__":
    dibujar_campo()
    plt.title("Campo de fútbol — 105 x 68 m")
    plt.show()
