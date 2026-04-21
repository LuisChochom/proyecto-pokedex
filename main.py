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
            print(f"\n--- TURNO DE {p1.nombre} ---")
            procesar_turno(p1, p2)
            if p2.hp_actual <= 0: break

            print(f"\n--- TURNO DE {p2.nombre} ---")
            if modo == "2":
                accion_ia = random.choice(["1", "2", "3"])
                ejecutar_accion(p2, p1, accion_ia)
            else:
                procesar_turno(p2, p1)
            
        ganador = p1.nombre if p1.hp_actual > 0 else p2.nombre
        print(f"\n¡{ganador} ha ganado la batalla!")
    except (ValueError, KeyError):
        print("\n[ERROR] Entrada no válida. Use solo números del catálogo.")
        ejecutar_simulacion()
    
def procesar_turno(atacante, defensor):
    print(f"[{atacante.nombre}] HP: {atacante.hp_actual} | EP: {atacante.energia_actual}")
    print("1. Atacar\n2. Defender\n3. Descansar")
    accion = input("> Elija accion: ")
    ejecutar_accion(atacante, defensor, accion)

def ejecutar_accion(p_activo, p_objetivo, accion):
    if accion == "1":
        resultado = p_activo.atacar(p_objetivo)
        if isinstance(resultado, tuple):
            danio, paraliza = resultado
            print(f"{p_activo.nombre} ataca! Daño: {danio}. {'¡Paralizado!' if paraliza else ''}")
        else:
            print(f"{p_activo.nombre} ataca e inflige {resultado} de daño.")
    elif accion == "2":
        if p_activo.defender():
            print(f"{p_activo.nombre} se defiende y reduce el daño del próximo ataque.")
        else:
            print(f"{p_activo.nombre} no tiene energía suficiente para defender.")
    elif accion == "3":
        p_activo.descansar()
        print(f"{p_activo.nombre} descansa y recupera energía.")

if __name__ == "__main__":
    ejecutar_simulacion()