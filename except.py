# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 09:20:53 2018

@author: chuck
"""

#try:
#    print(5/1)
#except ZeroDivisionError:
#    print("You can't divide by zero!")

#print("Give me two numbers, and I'll divide them.")
#print("Enter 'q' to quit")
#
#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Second number: ")
#    try:
#        answer = int(first_number) / int(second_number)
#    except ZeroDivisionError:
#        print("You can't divide by 0!")
#    else:
#        print(answer)

filename = 'alice.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
    