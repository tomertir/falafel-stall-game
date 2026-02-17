from unittest import TestCase
from Chill import Chill
from Customer import *
from TypeA import TypeA


class TestCustomer(TestCase):
    def setUp(self):
        self.cus=Customer(1,Chill(),TypeA())
    def test_get_mood(self):
        self.assertEqual(self.cus.get_mood(),Chill())


    def test_get_patience(self):
        print(self.cus.get_waiting_time())

    def test_repr(self):

        print(repr(self.cus))
