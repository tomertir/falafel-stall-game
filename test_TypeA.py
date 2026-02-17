from unittest import TestCase

from Angry import Angry
from Chill import Chill
from Explosive import Explosive
from Furious import Furious
from TypeA import TypeA


class TestTypeA(TestCase):
    def setUp(self):
        self.typea=TypeA()

    def test_adjust_mood(self):
        self.assertTrue(self.typea.adjust_mood(Angry, 45)), Explosive

    def test_adjust_mood_over20(self):
        self.assertEqual(self.typea.adjust_mood(Angry, 21), Angry())
        self.assertEqual(self.typea.adjust_mood(Chill, 22), Angry())

    def test_adjust_mood_over30(self):
        self.assertEqual(self.typea.adjust_mood(Chill, 31), Furious())

    def test_repr(self):
        self.assertEqual(repr(self.typea), "TypeA")
        print(self.typea)



