from abc import ABC, abstractmethod

class Mood(ABC):
    def __init__(self,strength=2): #?האם צריך להגביל את זה למספר חיובי
        if strength<0:
            raise ValueError("Strength value need to be higher than Zero")
        self.strength=strength

    @abstractmethod
    def get_patience_factor(self,waiting_time):
        pass

    def __repr__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        if not isinstance(other, Mood):
            return NotImplemented
        return type(self)==type(other)