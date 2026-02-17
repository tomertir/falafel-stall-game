import time
import copy
class Customer:
    def __init__(self,name,mood,personality, initial_patience=100,arrive_time=None):
        if arrive_time is None:
            self.arrive_time=int(time.time())
        self.name=name
        self.mood=mood
        self.personality=personality
        self.initial_patience=initial_patience

    def get_mood(self):
        return copy.copy(self.mood)

    def get_waiting_time(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        return copy.deepcopy(current_time-self.arrive_time)

    def get_patience(self):
        return round(self.initial_patience,2)

    def update(self,waiting_time=None):
        if waiting_time is None:
            waiting_time=self.get_waiting_time()
            factor= self.mood.get_patience_factor(waiting_time)
            self.initial_patience=self.initial_patience-factor
            self.mood=self.personality.adjust_mood(self.mood,waiting_time)



    def __repr__(self):
        l_name=f"name: {self.name}"
        l_mood=f"mood: {self.mood}"
        l_personality=f"personality: {self.personality}"
        l_patience = f"patience: {round(self.initial_patience,2)}"
        max_l=len(max(l_name,l_patience,l_personality,l_mood,key=len))
        op="*"*(max_l+4)+"\n"
        op+="* "+l_name+" "*(max_l-len(l_name)+1)+"*\n"
        op += "* "+l_mood+" " * (max_l - len(l_mood) + 1)+ "*\n"
        op += "* "+ l_personality+ " " * (max_l - len(l_personality) + 1)+"*\n"
        op += "* "+ l_patience+ " " * (max_l - len(l_patience) + 1)+"*\n"
        op += "*" * (max_l + 4)
        return op



