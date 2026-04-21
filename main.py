import random
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import PokemonFuego, PokemonAgua, PokemonPlanta, PokemonElectrico


# CRITERIO 2 - Instanciación Dinámica:
# Esta función crea instancias de Pokémon según el tipo especificado en el catálogo
# Demuestra creación dinámica de objetos en tiempo de ejecución
def crear_objeto_pokemon(id_catalogo):
    # Instanciación Dinámica: Extrae datos del catálogo y llama al constructor apropiado (Criterio 2)
    datos = CATALOGO_POKEMON[id_catalogo]
    tipo = datos["tipo"]
    n, h, e = datos["nombre"], datos["hp_maximo"], datos["energia_maxima"]

    # Selección dinámica de la clase según el tipo de Pokémon
    if tipo == "Fuego":
        return PokemonFuego(n, h, e)
    elif tipo == "Agua":
        return PokemonAgua(n, h, e)
    elif tipo == "Planta":
        return PokemonPlanta(n, h, e)
    elif tipo == "Electrico":
        return PokemonElectrico(n, h, e)


# Función principal que ejecuta la simulación de batalla
# DEMOSTRA CRITERIOS:
# - Criterio 3: Uso de try/except para manejo de errores
# - Criterio 8: Modo Jugador vs Computadora (PvE) con IA aleatoria
def ejecutar_simulacion():
    print("===== SIMULADOR DE BATALLAS POKÉMON (POO) =====")
    try:
        # CRITERIO 3 - Manejo de Errores (Try/Except):
        # El bloque try captura errores como ValueError o KeyError para manejar entradas inválidas
        print("1. Jugador vs Jugador\n2. Jugador vs Computadora")
        modo = input("> Opción: ")

        mostrar_catalogo_disponible()

        p1_idx = input("Jugador 1, elija el número de su Pokémon: ")
        p1 = crear_objeto_pokemon(p1_idx)
        print(f"¡Has seleccionado a {p1.nombre}!")

        # CRITERIO 8 - Modo PvE (Jugador vs IA):
        # Si el modo es "2", la computadora elige un Pokémon aleatoriamente del catálogo
        if modo == "2":
            p2_idx = random.choice(list(CATALOGO_POKEMON.keys()))
            p2 = crear_objeto_pokemon(p2_idx)
            print(f"¡La computadora ha seleccionado a {p2.nombre}!")
        else:
            p2_idx = input("Jugador 2, elija el número de su Pokémon: ")
            p2 = crear_objeto_pokemon(p2_idx)

        # Ciclo principal de combate: continúa mientras ambos Pokémon tengan HP > 0
        while p1.hp_actual > 0 and p2.hp_actual > 0:
            # Turno Jugador 1
            print(f"\n--- TURNO DE {p1.nombre} ---")
            procesar_turno(p1, p2)
            if p2.hp_actual <= 0:
                break

            # Turno Jugador 2 o Computadora (Criterio 8 - IA simple aleatoria)
            print(f"\n--- TURNO DE {p2.nombre} ---")
            if modo == "2":
                # En modo PvE, la IA elige una acción aleatoria (atacar, defender o descansar)
                accion_ia = random.choice(["1", "2", "3"])
                ejecutar_accion(p2, p1, accion_ia)
            else:
                procesar_turno(p2, p1)

        # Determina el ganador basado en el HP restante
        ganador = p1.nombre if p1.hp_actual > 0 else p2.nombre
        print(f"\n¡{ganador.upper()} ES EL VENCEDOR!")

    # CRITERIO 3 - Validación de entradas:
    # Captura errores de tipo ValueError (entradas numéricas inválidas) y KeyError (índices fuera de rango)
    except (ValueError, KeyError):
        print("\n[ERROR] Entrada no válida. Use solo números del catálogo.")
        # Reinicia la simulación en caso de error
        ejecutar_simulacion()


# Procesa un turno completo de un Pokémon: muestra estado, pide acción y la ejecuta
# FLUJO DEL TURNO: Muestra HP/EP -> Solicita acción -> Ejecuta acción -> Actualiza estado
def procesar_turno(atacante, defensor):
    # Muestra el estado actual del Pokémon (HP y EP)
    print(f"[{atacante.nombre}] HP: {atacante.hp_actual} | EP: {atacante.energia_actual}")
    print("1. Atacar | 2. Defender | 3. Descansar")
    accion = input("> Elija acción: ")
    # Delega la ejecución de la acción a la función ejecutar_accion
    ejecutar_accion(atacante, defensor, accion)


# Ejecuta una acción específica (atacar, defender o descansar) sobre un objetivo
# VALIDACIÓN DE ACCIONES:
# - Atacar: Verifica si el oponente ya fue derrotado
# - Defender: Verifica si hay suficiente energía (mínimo 5 EP)
# - Descansar: Siempre disponible (sin validación)
def ejecutar_accion(p_activo, p_objetivo, accion):
    if accion == "1":
        resultado = p_activo.atacar(p_objetivo)
        # Manejo especial para Pokémon Eléctrico: retorna tupla (daño, paralizó)
        if isinstance(resultado, tuple):
            danio, paraliza = resultado
            print(f"¡{p_activo.nombre} ataca! Daño: {danio}. {'¡PARALIZADO!' if paraliza else ''}")
        else:
            print(f"¡{p_activo.nombre} ataca e inflige {resultado} de daño!")
    elif accion == "2":
        # VALIDACIÓN: Verifica si el Pokémon tiene suficiente energía para defender (5 EP)
        if p_activo.defender():
            print(f"{p_activo.nombre} se pone en guardia.")
        else:
            print(f"¡{p_activo.nombre} no tiene energía para defender!")
    elif accion == "3":
        # Descansar: recupera 20 EP (mecánica sin validación, siempre disponible)
        p_activo.descansar()
        print(f"{p_activo.nombre} está descansando para recuperar EP.")


# Punto de entrada principal del programa
# Este bloque se ejecuta solo cuando el archivo se ejecuta directamente (no al importar)
if __name__ == "__main__":
    ejecutar_simulacion()
