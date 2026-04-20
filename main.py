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
        
        