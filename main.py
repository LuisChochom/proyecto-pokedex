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
    