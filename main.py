import random
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import PokemonFuego, PokemonAgua, PokemonPlanta, PokemonElectrico

def crear_objeto_pokemon(id_catalogo):
    datos = CATALOGO_POKEMON[id_catalogo]
    tipo = datos["tipo"]
    n, h, e = datos["nombre"], datos["hp_maximo"], datos["energia_maxima"]

    if tipo == "Fuego":return PokemonFuego(n,h,e)
    elif tipo == "Agua":return PokemonAgua(n,h,e)
    elif tipo == "Planta":return PokemonPlanta(n,h,e)
    elif tipo == "Electrico":return PokemonElectrico(n,h,e)
    
def ejecutar_simulacion():
    print("¡Bienvenido a la simulación de batalla Pokémon!")
    try:
        print("1. Jugador vs Jugador\n2. Jugador vs Computadora")
        modo = input("> opcion: ")
        mostrar_catalogo_disponible()

        p1_idx = input("Jugador 1, elija el número del Pokémon: ")
        p1 = crear_objeto_pokemon(p1_idx)
        print(f"Jugador 1 ha elegido a {p1.nombre}.")

        if modo == "2":
            p2_idx = random.choice(list(CATALOGO_POKEMON.keys()))
            p2 = crear_objeto_pokemon(p2_idx)
            print(f"La computadora ha elegido a {p2.nombre}.")
        else:
            p2_idx = input("Jugador 2, elija el número del Pokémon: ")
            p2 = crear_objeto_pokemon(p2_idx)
            print(f"Jugador 2 ha elegido a {p2.nombre}.")
        
        while p1.hp_actual > 0 and p2.hp_actual > 0:
            print(f"\nTurno de {p1.nombre} (HP: {p1.hp_actual}/{p1.hp_maximo}, Energía: {p1.energia_actual}/{p1.energia_maxima})")
            procesar_turno(p1, p2)
            if p2.hp_actual <= 0: break

            print(f"\nTurno de {p2.nombre} (HP: {p2.hp_actual}/{p2.hp_maximo}, Energía: {p2.energia_actual}/{p2.energia_maxima})")
            if modo == "2":
                accion_ia = random.choice("1", "2", "3")
                ejecutar_accion(p2, p1, accion_ia)
            else:
                procesar_turno(p2, p1)
            
        ganador = p1.nombre if p1.hp_actual > 0 else p2.nombre
        print(f"\n¡{ganador} ha ganado la batalla!")
    except (ValueError, KeyError):
        print("\n[ERROR] Entrada no válida. Use solo números del catálogo.")
        ejecutar_simulacion()
    
    