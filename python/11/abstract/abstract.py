from abc import ABC, abstractmethod

class Unit(ABC):
    @abstractmethod
    def hp_power(self):
        pass

    @abstractmethod
    def mp_power(self):
        pass

class Player(Unit):
    def __init__(self, hp, mp):
        self.hp = hp
        self.mp = mp

    def hp_power(self):
        return self.hp ** self.hp

    def mp_power(self):
        return self.mp ** self.mp
