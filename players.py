"""

ENTENDIDA ==========================

players.py
Contiene el formato de clase de un jugador e incluye una función que
genera un equipo utilizando un vector de posiciones.

Atributos actuales: id del jugador, team para indicar a que equipo pertenece
                    (x,y) indica la posición en el campo. label para cualquier otra cosa extra
                    tiene_balon me dice si un jugador tiene o no el balón
                    area me dice que area controla de voronoi
"""

from dataclasses import dataclass, field



@dataclass
class Player:
    id: int
    team: str       # 'own' (tu equipo) u 'opp' (rival)
    x: float           #posición del jugador en un momento dado
    y: float
    label: str = ""  # texto a mostrar junto al jugador (opcional)

    tiene_balon: bool = False

    # Región de control del terreno de juego, calculada por voronoi.py:
    # lista de vértices (x, y) del polígono. Vacía hasta que se calcule
    area: list = field(default_factory=list)

    def posicion(self):                 #función para saber en que posición está tu jugador, por ejemplo print(p1.posicion())
        return (self.x, self.y)


def crear_equipo_prueba(team: str, ids_inicio: int, posiciones):    #crea una estructura de equipo que no es más que el listado de sus jugadores cada jugador con sus atributos, en particular su código y posición en el campo.
    """
    Crea una lista de Player a partir de una lista de posiciones (x, y).

    team:        'own' u 'opp'
    ids_inicio:  id del primer jugador (los siguientes serán consecutivos)
    posiciones:  son del tipo [(x1, y1), (x2, y2), ...]
    """
    jugadores = []      #la lista de jugadores del equipo
    for i, (x, y) in enumerate(posiciones): #se añade un jugador por cada posición
        jugador_id = ids_inicio + i
        jugadores.append(
            Player(id=jugador_id, team=team, x=x, y=y, label=str(jugador_id))
        )
    return jugadores
