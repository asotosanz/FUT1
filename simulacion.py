"""
simulacion.py
simula cada dt=0.1 segundos

la función simular te ejecuta una simulación desde tiempo 0 hasta 'duracion'

Cómo se usa: le pasas una función `paso_fn(tiempo, dt)` que sabe cómo
actualizar tu mundo (mover jugadores, mover el balón, comprobar
posesión...) asumiendo que ha transcurrido `dt` segundos y que estamos en el tiempo el que sea

simular() se encarga solo de llamarla las veces que hagan falta y de llevar la
cuenta del tiempo — no sabe nada de fútbol, jugadores ni balón
"""


def simular(paso_fn, dt=0.1, duracion=10.0, on_frame=None):
    """
    Ejecuta la simulación desde tiempo=0 hasta tiempo=duracion, a
    saltos de `dt` segundos. no tiene ni idea de nada, ni contiene datos futbolisticos

    paso_fn(tiempo, dt):
        función que actualiza el estado del mundo para este paso.
        Aquí es donde, más adelante, moverás jugadores, actualizarás
        la posición del balón, comprobarás si alguien ha robado la
        posesión, etc.

    on_frame(tiempo):
        opcional. Si la pasas, se llama después de cada paso — pensada
        para "renderizar" (dibujar/guardar una imagen) ese instante sin
        mezclar la lógica de dibujo con la lógica de simulación.
        Esto se puede hacer para en una especie de animación dibujar el escenario en cada frame.

    Devuelve el número total de pasos ejecutados. No sé si eso nos interesa tanto.
    """
    tiempo = 0.0
    pasos = int(round(duracion / dt))

    for _ in range(pasos):
        paso_fn(tiempo, dt)
        if on_frame is not None:
            on_frame(tiempo)
        tiempo += dt

    return pasos


if __name__ == "__main__":
    # Ejemplo mínimo: no mueve nada todavía, solo demuestra que el
    # bucle avanza el tiempo correctamente.
    def paso_de_prueba(tiempo, dt):
        print(f"t = {tiempo:.1f}s (dt = {dt}s)")

    total = simular(paso_de_prueba, dt=0.5, duracion=2.0)
    print(f"Simulación terminada: {total} pasos")
