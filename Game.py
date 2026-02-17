from exceptions import *
from Dish import *
import time
import copy
from FalafelStall import *



class Game:
    def __init__(self, orders_strategy, serving_strategy, ingredient_prices):
        self.orders_strategy = orders_strategy
        self.serving_strategy = serving_strategy
        self.ingredient_prices= ingredient_prices
        self.game_start=int(time.time())
        self.lives=3
        self.ingredient_dictionary= {0:"green salad",1:"falafel",2: "french fries",3: "coleslaw",4: "fried eggplants",5: "tachina",6: "humus"}

    def get_lives(self):
        return copy.copy(self.lives)

    def get_game_duration(self, current_time=None):
        if current_time is None:
            current_time= int(time.time())
            return current_time - self.game_start

    def __helper_print_dic(self, i_dict):
        result = 'Insert ingredients:\n'
        for key, value in i_dict.items():
            result += f'{key}: {value}\n'
        return result.strip()

    def run(self):
        f=FalafelStall(self.serving_strategy,self.ingredient_prices)
        while self.lives>0:
            try:
                a= next(self.orders_strategy)
            except StopIteration:
                break
            for i in a:
                f.order(i[0],i[1])
            while len(f.get_orders())>0:
                order_id=f.get_next_order_id()
                customer= f.get_order(order_id)[0]
                ordered_dish = f.get_order(order_id)[1]
                while True:
                    print(f'Customer:\n{customer}\nDish: {ordered_dish}')
                    print(self.__helper_print_dic(self.ingredient_dictionary))
                    player_in = input()
                    ing = player_in.split()
                    dish=[]
                    flag = True
                    for ingredient in ing:
                        try:
                            num = int(ingredient)
                            if num in self.ingredient_dictionary:
                                dish.append(self.ingredient_dictionary[num])
                            else:
                                print(
                                f'Failed to create a Dish\nError:\n"{num}" is an invalid ingredient.\n please retry.')
                                flag=False
                                break
                        except ValueError:
                            print(f'Failed to create a Dish\nError:\n"{ingredient}" is an invalid ingredient.\n please retry.')
                            flag= False
                            break

                    if not flag:
                        continue

                    player_dish=Dish(dish)
                    if player_dish==ordered_dish:
                        f.serve_dish(order_id, player_dish)
                        f.remove_order(order_id)
                        orders = f.get_orders().copy()
                        for o_id, customer in orders.items():
                            customer[0].update()
                            if customer[0].get_patience()<=0:
                                self.lives-=1
                                f.remove_order(o_id)

                        break
                    else:
                        print(f'Failed to serve a Dish to customer\nError:\nThe suggested dish:\t{player_dish}\nis not as expected:\t{ordered_dish}.')
                        break

        print(f'Game Over\nscore: {f.get_earning()}')

                







































