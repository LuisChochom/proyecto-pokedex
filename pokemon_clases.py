from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    def __init__(self, nombre, hp_max, ep_max):
        self.nombre = nombre
        self._hp_actual = hp_max
        self._hp_maximo = hp_max
        self._energia_actual = ep_max
        self._energia_maxima = ep_max
        self._bloqueo_activo = False

    @property
    def hp_actual(self):
        return self._hp_actual
    
    @hp_actual.setter
    def hp_actual(self, valor):
        if valor < 0:
            self._hp_actual = 0
        elif valor > self._hp_maximo:
            self._hp_actual = self._hp_maximo
        else:
            self._hp_actual = valor
    
    @property
    def energia_actual(self):
        self._energia_actual
    
    @energia_actual.setter
    def energia_actual(self, valor):
        if valor < 0:
            self._energia_actual = 0
        elif valor > self._energia_maxima:
            self._energia_actual = self._energia_maxima
        else:
            self._energia_actual = valor
    
    @abstractmethod
    def atacar(self, oponente):
        pass

    def defender(self):
        if self.energia_actual > 5:
            self.energia_actual -= 5
            self.bloqueo_activo = True
            return True
        return False
    
    def descansar(self):
        self.energia_actual += 20

class PokemonFuego(Pokemon):
    def atacar(self, oponente):
        costo = 15
        if self.energia_actual < costo:
            return 0
        self.energia_actual -= costo

        from pokemon_clases import PokemonPlanta
        multiplicador = 2 if isinstance(oponente, PokemonPlanta)else 1
        danio = 20 * multiplicador

        if oponente.bloque_activo:
            danio //= 2
            oponente.bloque_activo = False
        
        oponente.hp_actual -= danio
        return danio

class PokemonAgua(Pokemon):
    def atacar(self, oponente):
        costo = 15
        if self.energia_actual < costo:
            return 0
        self.energia_actual -= costo

        multiplicador = 2 if isinstance (oponente, PokemonFuego) else 1
        danio = 20 * multiplicador

        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False
        
        oponente.hp_actual -=  danio
        return danio

class PokemonPlanta(Pokemon):
    def atacar(self, oponente):
        costo = 15
        if self.energia_actual < costo:
            return 0
        self.energia_actual -= costo

        multiplicador = 2 if isinstance(oponente, PokemonAgua) else 1
        danio = 20 * multiplicador

        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False

        oponente.hp_actual -= danio
        return danio

class PokemonElectrico(Pokemon):
    def atacar(self, oponente):
        costo = 15
        if self.energia_actual < costo:
            return 0
        self.energia_actual -= costo

        danio = 20
        paralizado = False

        if random.random() <= 0.20:
            paralizado = True
        
        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False
        
        oponente.hp_actual -= danio
        return danio, paralizado