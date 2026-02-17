
from ServingStrategy import *
import time
from exceptions import OrderOutOfBoundsException
from Customer import *


class ArrivalTimeServingStrategy(ServingStrategy):

    def select_next_order(self,orders):
        if orders== {}:
            raise OrderOutOfBoundsException
        for key, value in orders.items():
            first_in_key=key
            first_in_value = value[0].arrive_time
            break

        for key, value in orders.items():
            if value[0].arrive_time<first_in_value:
                first_in_key=key
                first_in_value=value[0].arrive_time
        order=orders.pop(first_in_key)
        return order









