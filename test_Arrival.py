from unittest import TestCase
from ArrivalTimeServingStrategy import *
from Angry import Angry
from Calm import Calm
from TypeB import TypeB
from TypeA import TypeA
from Customer import Customer
from Dish import Dish
from Explosive import Explosive
from Furious import Furious
from Chill import Chill

class TestLongestWaitingTimeServingStrategy(TestCase):
    def test_select_next_order(self):
        self.t=ArrivalTimeServingStrategy()
        a=Customer(4, Angry(), TypeB())
        a.arrive_time = 100
        dict_t = {
            1: (Customer(0, Angry(), TypeB()), Dish(['french fries', 'humus', 'humus', 'humus'])),
            2: (Customer(1, Angry(), TypeB()), Dish(['french fries', 'humus', 'humus', 'humus'])),
            3: (a, Dish(['french fries', 'humus', 'humus', 'humus']))
        }
        a=self.t.select_next_order(dict_t)
        print(a[0])
        print(a[1])
        a = self.t.select_next_order(dict_t)
        print(a[0])
        print(a[1])
        a = self.t.select_next_order(dict_t)
        print(a[0])
        print(a[1])



