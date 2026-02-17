import random
from Calm import Calm
from Angry import Angry
from Chill import Chill
from Explosive import Explosive
from Furious import Furious
from TypeA import TypeA
from TypeB import TypeB
from Customer import Customer
from Dish import Dish
from OrdersStrategy import *



class RandomOrdersStrategy(OrdersStrategy):
    global_counter = 0
    def __init__(self,max_dishes,max_ingredients,ingredients,n_orders=-1):
        self.max_dishes=max_dishes
        self.max_ingredients=max_ingredients
        self.ingredients=ingredients
        self.n_orders=n_orders
        self.current=0

    def __iter__(self):
        return self

    def __next__(self):

        if self.n_orders != -1 and self.current>=self.n_orders:
            raise StopIteration

        num_dishes = random.randint(1, self.max_dishes)
        orders = []
        for i in range(num_dishes):
            num_ingredients = random.randint(1, self.max_ingredients)
            ingredients_for_dish=[]
            for j in range(num_ingredients):
                ingredients_for_dish.append(random.choice(self.ingredients))
            dish= Dish(ingredients_for_dish)
            mood = random.choice([Angry(),Calm(),Chill(),Explosive(),Furious()])
            personality = random.choice([TypeA(),TypeB()])
            name = str(RandomOrdersStrategy.global_counter + 1)
            customer = Customer(name,mood,personality)
            order = (customer, dish)
            orders.append(order)
            RandomOrdersStrategy.global_counter += 1


        self.current += 1

        return orders






