
from ServingStrategy import *
from exceptions import OrderOutOfBoundsException
from Customer import *

class LeastPatienceCustomerServingStrategy(ServingStrategy):

    def select_next_order(self,orders):
        if orders=={}:
            raise OrderOutOfBoundsException
        lowest_patience_key=0
        lowest_patience_value = 101

        for key, value in orders.items():
            if value[0].get_patience()<lowest_patience_value:
                lowest_patience_key=key
                lowest_patience_value=value[0].get_patience()
        order=orders.get(lowest_patience_key)
        return lowest_patience_key









