from unittest import TestCase
from Mood import *
from Angry import Angry
from Calm import Calm


class TestMood(TestCase):
    def setUp(self):
        self.mood1= Angry()
        self.mood2 = Calm()
        self.mood3 = Angry()

    def test_rise(self):
        try: self.mood4=Angry(-2)
        except ValueError as e:
            print(e)
            print("got it!")
        try: self.mood5=Angry(2)
        except ValueError as e:
            print(e)
            print("got it!")
        else:
            print("it fine")




    def test_eq(self):
        self.assertFalse(self.mood1==self.mood2)
        self.assertTrue(self.mood1 == self.mood3)
