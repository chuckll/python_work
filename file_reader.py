# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 18:57:54 2018

@author: chuck
"""

#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#    print(contents.rstrip())

#filename = 'pi_digits.txt'
#
#with open(filename) as file_object:
#    for line in file_object:
#        print(line.rstrip())

#filename = 'programming.txt'
#
#with open(filename,'w') as file_object:
#    file_object.write("I love programming.\n")
#    file_object.write("I love creating new games.\n")

filename = "programming.txt"

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    