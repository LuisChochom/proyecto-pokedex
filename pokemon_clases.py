# Módulos importados (Criterio 1 - Compilación):
# - ABC y abstractmethod: Para definir clases abstractas y métodos abstractos, habilitando polimorfismo
# - random: Para generar números aleatorios, usado en el tipo Electrico para probabilidad de parálisis
from abc import ABC, abstractmethod
import random


# Clase Base Abstracta (Criterio 3 del enunciado)
# Esta clase define la estructura base que todos los Pokémon deben seguir
# HERENCIA (Criterio 4): Las clases hijas (PokemonFuego, PokemonAgua, etc.) heredan atributos y métodos de Pokemon
# ENCAPSULAMIENTO (Criterio 6): Los atributos de estado (hp, energia) se encapsulan con variables privadas (_hp_actual, _energia_actual)
class Pokemon(ABC):
    def __init__(self, nombre, hp_max, ep_max):
        self.nombre = nombre
        # Atributos privados para encapsulamiento (Criterio 6)
        # _hp_actual y _hp_maximo gestionan la salud del Pokémon
        # _energia_actual y _energia_maxima gestionan los puntos de energía
        self._hp_actual = hp_max
        self._hp_maximo = hp_max
        self._energia_actual = ep_max
        self._energia_maxima = ep_max
        self.bloqueo_activo = False

    # Property hp_actual (Criterio 6 - Encapsulamiento):
    # Permite acceder al HP actual desde fuera de la clase sin exponer la variable privada directamente
    @property
    def hp_actual(self):
        return self._hp_actual

    # Setter hp_actual (Criterio 6 y 7):
    # ENCAPSULAMIENTO (Criterio 6): Controla la modificación del HP a través de una interfaz controlada
    # VALIDACIÓN MATEMÁTICA (Criterio 7): Asegura que el HP se mantenga siempre entre 0 y hp_maximo
    @hp_actual.setter
    def hp_actual(self, valor):
        if valor < 0:
            self._hp_actual = 0
        elif valor > self._hp_maximo:
            self._hp_actual = self._hp_maximo
        else:
            self._hp_actual = valor

    # Property energia_actual (Criterio 6 - Encapsulamiento):
    # Similar a hp_actual, controla el acceso a la energía del Pokémon
    @property
    def energia_actual(self):
        return self._energia_actual

    # Setter energia_actual (Criterio 6 - Encapsulamiento):
    # Enfocado en encapsulación, limita la energía entre 0 y energia_maxima
    @energia_actual.setter
    def energia_actual(self, valor):
        if valor < 0:
            self._energia_actual = 0
        elif valor > self._energia_maxima:
            self._energia_actual = self._energia_maxima
        else:
            self._energia_actual = valor

    # Método abstracto atacar (Criterio 5 - Polimorfismo):
    # Declarado como abstractmethod, obliga a todas las subclases a implementar su propia versión de atacar
    # Esto permite polimorfismo: cada tipo de Pokémon tiene un comportamiento distinto al atacar
    @abstractmethod
    def atacar(self, oponente):
        pass

    # Método defender: Implementa la mecánica de defensa del juego
    # Reduce el daño recibido a la mitad si el defensor tiene suficiente energía (mínimo 5 EP)
    # Si no hay suficiente energía, la defensa falla y retorna False
    # VALIDACIÓN DE EP: Verifica que energia_actual >= 5 antes de permitir la defensa
    def defender(self):
        # Consume 5 EP y reduce daño a la mitad (Criterio 2)
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.bloqueo_activo = True
            return True
        return False

    # Método descansar: Mecánica de recuperación de energía
    # Recupera 20 puntos de energía cada vez que se usa
    def descansar(self):
        self.energia_actual += 20


# Pokémon Fuego - HERENCIA (Criterio 4): Hereda de Pokemon
# POLIMORFISMO (Criterio 5): Implementa su propia versión del método abstracto atacar
# Ventaja elemental: Hace el doble de daño a Pokémon Planta
class PokemonFuego(Pokemon):
    def atacar(self, oponente):
        costo = 15
        # VALIDACIÓN DE EP: Verifica que el atacante tenga suficiente energía (15 EP mínimo)
        if self.energia_actual < costo:
            return 0
        self.energia_actual -= costo

        # POLIMORFISMO con isinstance(): Detecta el tipo del oponente en tiempo de ejecución
        # Se importa la clase aquí para evitar dependencias circulares
        from pokemon_clases import PokemonPlanta
        # MECÁNICA DE VENTAJA ELEMENTAL: El fuego es eficaz contra planta (x2 daño)
        multiplicador = 2 if isinstance(oponente, PokemonPlanta) else 1
        danio = 20 * multiplicador

        # Mecánica de defensa: Si el oponente está bloqueando, el daño se reduce a la mitad
        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False

        oponente.hp_actual -= danio
        return danio


# Pokémon Agua - HERENCIA (Criterio 4): Hereda de Pokemon
# POLIMORFISMO (Criterio 5): Implementación particular del método atacar
# Ventaja elemental: Hace el doble de daño a Pokémon Fuego
class PokemonAgua(Pokemon):
    def atacar(self, oponente):
        costo = 15
        # VALIDACIÓN DE EP: Sin suficiente energía, el ataque falla y retorna 0 de daño
        if self.energia_actual < costo:
            return 0
        self.energia_actual -= costo

        # POLIMORFISMO con isinstance(): El agua es eficaz contra fuego (x2 daño)
        multiplicador = 2 if isinstance(oponente, PokemonFuego) else 1
        danio = 20 * multiplicador

        # Mecánica de bloqueo: reduce daño a la mitad y desactiva el bloqueo del defensor
        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False

        oponente.hp_actual -= danio
        return danio


# Pokémon Planta - HERENCIA (Criterio 4): Hereda de Pokemon
# POLIMORFISMO (Criterio 5): Implementación específica del ataque
# Ventaja elemental: Hace el doble de daño a Pokémon Agua
class PokemonPlanta(Pokemon):
    def atacar(self, oponente):
        costo = 15
        # VALIDACIÓN DE EP: Revisa la disponibilidad de energía antes del ataque
        if self.energia_actual < costo:
            return 0
        self.energia_actual -= costo

        # POLIMORFISMO con isinstance(): La planta es eficaz contra agua (x2 daño)
        multiplicador = 2 if isinstance(oponente, PokemonAgua) else 1
        danio = 20 * multiplicador

        # Mecánica de bloqueo: aplica reducción de daño y consume el bloqueo del defensor
        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False

        oponente.hp_actual -= danio
        return danio


# Pokémon Eléctrico - HERENCIA (Criterio 4): Hereda de Pokemon
# POLIMORFISMO (Criterio 5): Tiene un comportamiento de ataque único
# EFECTO DE ESTADO: Posee un 20% de probabilidad de paralizar al oponente
class PokemonElectrico(Pokemon):
    def atacar(self, oponente):
        costo = 15
        # VALIDACIÓN DE EP: Verifica que el Pokémon tenga la energía necesaria para atacar
        if self.energia_actual < costo:
            return 0
        self.energia_actual -= costo

        danio = 20
        paralizado = False

        # PROBABILIDAD DEL 20% (Criterio 2 - Validación): random.random() genera [0.0, 1.0)
        # Si el valor es <= 0.20, el oponente queda paralizado (efecto de estado)
        if random.random() <= 0.20:
            paralizado = True

        # Mecánica de bloqueo: reduce daño y elimina el estado de bloqueo
        if oponente.bloqueo_activo:
            danio //= 2
            oponente.bloqueo_activo = False

        oponente.hp_actual -= danio
        # Retorna una tupla (daño, paralizado) para informar del efecto secundario
        return danio, paralizado
