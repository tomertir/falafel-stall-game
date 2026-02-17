from Angry import Angry
from Explosive import Explosive
from Furious import Furious
from Personality import Personality


class TypeA(Personality):

    def adjust_mood(self,mood,waiting_time):
        if waiting_time>40:
            return Explosive()
        elif waiting_time>30 and mood!= Explosive:
            return Furious()
        elif waiting_time>20 and mood!= Explosive and mood!= Furious:
            return Angry()
        else:
            return mood





