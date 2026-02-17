from OrdersStrategy import *

class FixedOrdersStrategy(OrdersStrategy):
    def __init__(self,lst_orders):
        self.lst_orders=lst_orders
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index>=len(self.lst_orders):
            raise StopIteration
        temp= self.index
        self.index+=1
        return self.lst_orders[temp]






