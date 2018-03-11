# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:09:13 2018

@author: chuck
"""

#alien_0 = {'x_position':0, 'y_position':25,'speed':'fast'}
#print("Original x-position: " + str(alien_0['x_position']))
#
#if alien_0['speed'] == 'slow':
#	x_increment = 1
#elif alien_0['speed'] == 'medium':
#	x_increment = 2
#else:
#	x_increment = 3
#	
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#	
#print("New x-position: " + str(alien_0['x_position']))

#alien_0 = {'colr':'green','points':5}
#print(alien_0)
#
#del alien_0['points']
#print(alien_0)

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

for key,value in favorite_languages.items():
    print('\nKey:' + key)
    print('Value:' + value)