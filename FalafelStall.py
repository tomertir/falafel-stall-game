from exceptions import *
from Dish import *
import copy


class FalafelStall:
    def __init__(self,strategy, ingredient_prices):
        self.strategy = strategy
        self.ingredient_prices = ingredient_prices
        self.orders= {}
        self.money=0.0
        self.order_counter=0

    def order(self, customer, dish):
        flag=True
        ingredient=""
        for i in dish.ingredients:
            if i not in self.ingredient_prices:
                flag=False
                ingredient=i
                break
        if flag:
            self.orders[self.order_counter+1]=(customer,dish)
            self.order_counter+=1
        else:
            raise NoSuchIngredientException(ingredient)

    def get_next_order_id(self):
        order=self.strategy.select_next_order(self.orders)
        return copy.copy(order)

    def serve_dish(self, order_id, dish):
        if type(order_id) != int:
            raise ValueError
        elif type(dish) !=Dish:
            raise ValueError
        elif order_id not in self.orders:
            raise NoSuchOrderException(order_id)
        elif dish != self.orders[order_id][1]:
            raise NotCustomerDishException(dish,self.orders[order_id][1])

        cost=self.calculate_cost(dish)
        self.money+=cost



    def remove_order(self, order_id):
        if type(order_id) != int:
            raise ValueError
        elif order_id not in self.orders:
            raise NoSuchOrderException(order_id)
        del self.orders[order_id]

    def get_order(self, order_id):
        if type(order_id) != int:
            raise ValueError
        elif order_id not in self.orders:
            raise NoSuchOrderException(order_id)
        return copy.copy(self.orders[order_id])

    def calculate_cost(self, dish):
        cost=0.0
        for i in dish.get_ingredients():
            if i not in self.ingredient_prices:
                raise NoSuchIngredientException(i)
            else:
                cost += self.ingredient_prices[i]
        return cost

    def get_orders(self):
        return self.orders
    def get_earning(self):
        return  copy.copy(self.money)
















