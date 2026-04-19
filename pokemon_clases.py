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
    
    