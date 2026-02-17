from unittest import TestCase
from Calm import *
from Angry import *


class TestCalm(TestCase):
    def setUp(self):
        self.calm=Calm()
        self.calm2 = Calm(5)
        self.angry = Angry()

    def test_get_patience_factor(self):
        self.assertEqual(self.calm.get_patience_factor(20),2.43)

    def test_get_patience_factor_no_def_value(self):
        self.assertEqual(self.calm2.get_patience_factor(40), 7.39)

    def test_repr(self):
        self.assertEqual(repr(self.calm), "Calm")
        self.assertEqual(repr(self.calm2), "Calm")

    def test_eq(self):
        self.assertTrue(self.calm==self.calm2)
        self.assertFalse(self.calm == self.angry)
