# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:53:23 2018

@author: chuck
"""

#aliens = []
#
#for alien_number in range(30):
#    new_alien = {'color':'green', 'points':5,'speed':'slow'}
#    aliens.append(new_alien)
#    
#for alien in aliens[0:3]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['points'] = 10
#    
#    
#for alien in aliens[:5]:
#    print(alien)
#print("...")


#pizza = {
#        'crust': 'thick',
#        'toppings': ['mushrooms', 'extra cheese'],
#        }
#
#print("You ordered a" + pizza['crust'] + "-crust pizza " +
#      "with the following toppings:")
#
#for topping in pizza['toppings']:
#    print("\t" + topping)


users = {
        'aeinstein':{
                'first': 'albert',
                'last': 'einstein',
                'location': 'princeton',
                },
                
         'mcurie': {
                 'first': 'marie',
                 'last': 'curie',
                 'location': 'paries',
                 },
        }
         
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
         
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         