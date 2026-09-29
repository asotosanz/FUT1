"""
io_posiciones.py
Lee y escribe las posiciones de los jugadores en un archivo JSON,
manteniendo los datos separados del código.

Formato del JSON (ver data/posiciones.json):
{
  "own": [{"id": 1, "x": 15, "y": 34}, ...],
  "opp": [{"id": 101, "x": 40, "y": 20}, ...]
}
"""

import json

from players import Player


def cargar_posiciones(path="data/posiciones.json"):
    """
    Lee el JSON y devuelve dos listas de Player: (own, opp).
    """
    with open(path, "r", encoding="utf-8") as f:
        datos = json.load(f)

    own = [Player(id=j["id"], team="own", x=j["x"], y=j["y"], label=str(j["id"]))
           for j in datos.get("own", [])]
    opp = [Player(id=j["id"], team="opp", x=j["x"], y=j["y"], label=str(j["id"]))
           for j in datos.get("opp", [])]

    return own, opp


def guardar_posiciones(own, opp, path="data/posiciones.json"):
    """
    Vuelca las posiciones actuales de own/opp (listas de Player) al JSON,
    sobrescribiéndolo.
    """
    datos = {
        "own": [{"id": p.id, "x": p.x, "y": p.y} for p in own],
        "opp": [{"id": p.id, "x": p.x, "y": p.y} for p in opp],
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)


def mover_jugador(jugadores, jugador_id, nuevo_x, nuevo_y):
    """
    Busca un jugador por id dentro de una lista (own u opp) y actualiza
    su posición in-place. Lanza ValueError si no existe ese id.
    """
    for p in jugadores:
        if p.id == jugador_id:
            p.x, p.y = nuevo_x, nuevo_y
            return p
    raise ValueError(f"No existe ningún jugador con id={jugador_id}")


if __name__ == "__main__":
    # Ejemplo: cargar, mover al jugador 1 y guardar el cambio
    own, opp = cargar_posiciones()
    mover_jugador(own, jugador_id=1, nuevo_x=18, nuevo_y=30)
    guardar_posiciones(own, opp)
    print("Posiciones actualizadas y guardadas en data/posiciones.json")
