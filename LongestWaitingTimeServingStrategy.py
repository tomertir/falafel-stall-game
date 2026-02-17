
from ServingStrategy import *
from exceptions import OrderOutOfBoundsException
from Customer import *

class LongestWaitingTimeServingStrategy(ServingStrategy):

    def select_next_order(self,orders):
        if orders== {}:
            raise OrderOutOfBoundsException
        for key, value in orders.items():
            longest_wait_key=key
            longest_wait_value = value[0].get_waiting_time()
            break

        for key, value in orders.items():
            if value[0].get_waiting_time()>longest_wait_value:
                longest_wait_key=key
                longest_wait_value=value[0].get_waiting_time()
        order=orders.pop(longest_wait_key)
        return order









