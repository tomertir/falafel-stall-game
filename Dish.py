import copy
class Dish:
    def __init__(self,ingredients=None):
        if ingredients is None:
            ingredients=[]
        self.ingredients=ingredients

    def add_ingredient(self,other):
        self.ingredients.append(other)

    def get_ingredients(self):
        return copy.copy(self.ingredients)

    def __eq__(self,other):
        if not isinstance(other,Dish):
            return NotImplemented
        return len(self.ingredients)==len(other.ingredients) and sorted(self.ingredients)==sorted(other.ingredients)

    def __repr__(self):
        op="*"
        for i in self.ingredients:
            op += f" {i},"
        if len(self.ingredients)>0:
            op =op[:-1]
        op+=" *"
        return op

