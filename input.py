# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:33:58 2018

@author: chuck
"""

#name = input("Please enter your name: ")
#print("Hello, " + name + "!")

#height = input("How tall are you,in inches? ")
#height = int(height)
#
#if height >= 36:
#    print("\nYou're tall enough to ride!")
#else:
#    print("\nYou'll be able to ride when you're a little older.")

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user =  unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())