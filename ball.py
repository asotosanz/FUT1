"""
ball.py
El balón, como entidad con posición propia, más las funciones que
mantienen sincronizada su posesión con el flag `tiene_balon` de cada
Player. No cambies `balon.poseedor_id` ni `player.tiene_balon` a mano
por separado: usa siempre dar_posesion / soltar_posesion, para que
nunca queden desincronizados.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Ball:
    x: float
    y: float
    poseedor_id: Optional[int] = None  # id del Player que la tiene, o None si está suelta


def dar_posesion(balon, jugador, jugadores):
    """
    Da la posesión del balón a `jugador`.

    - Mueve el balón a la posición de ese jugador.
    - Marca `tiene_balon = True` solo en él, y False en el resto.

    `jugadores` debe ser la lista de TODOS los jugadores en juego
    (own + opp), para que el rival que tuviera el balón antes quede
    correctamente marcado sin posesión.
    """
    balon.poseedor_id = jugador.id
    balon.x, balon.y = jugador.x, jugador.y
    for p in jugadores:
        p.tiene_balon = (p.id == jugador.id)


def soltar_posesion(balon, jugadores):
    """
    Deja el balón suelto: nadie tiene la posesión (por ejemplo,
    mientras un pase está en el aire, o tras un balón dividido).
    El balón conserva su posición actual (x, y) — solo cambia quién
    la controla.
    """
    balon.poseedor_id = None
    for p in jugadores:
        p.tiene_balon = False
