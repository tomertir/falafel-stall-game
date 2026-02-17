from unittest import TestCase
from RandomOrdersStrategy import *

class TestRandomOrderStrategy(TestCase):

    def setUp(self):
        self.r=RandomOrdersStrategy(3,4,["a","b","c","d","t"],2)

    def test_p(self):

        a=(list((self.r)))
        for i in a[0]:
            print(i[0])
            print(i[1])

        print(a[1])

        try:
            print(a[2])
        except IndexError as e:
            print("we did it, you got:",e)






