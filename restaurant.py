# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:27:01 2018

@author: chuck
"""

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def des_restaurant(self):
        print(self.restaurant_name.title() + "'s cuisine type is "
              + self.cuisine_type)
        
    def open_restaurant(self):
        print("The restaurant is opening.")
        
rest1=Restaurant('KFC','America')
rest2=Restaurant('BBQ','korea')

rest1.des_restaurant()
rest2.des_restaurant()
rest1.open_restaurant()
rest2.open_restaurant()