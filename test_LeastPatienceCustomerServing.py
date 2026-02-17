from unittest import TestCase
from LeastPatienceCustomerServingStrategy import *
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
        self.t=LeastPatienceCustomerServingStrategy()
        a = Customer(1, Angry(), TypeB())
        a.initial_patience = 30
        dict_t = {
            1: (Customer(0, Angry(), TypeB()), Dish(['french fries', 'humus', 'humus', 'humus'])),
            2: (a, Dish(['french fries', 'humus', 'humus', 'humus']))
        }
        a=self.t.select_next_order(dict_t)
        print(a)
        a = self.t.select_next_order(dict_t)
        print(a)





