#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:48:09 2019
@author: bhoeft
"""

import random

# User can pick 6 numbers #####################################################

def get_player_numbers():
    """captures the 6 comma separated value numbers
    entered by the user, stores them in a list."""
    
    number_csv = input("enter your 6 numbers separated by a comma: ")
    # create a set of numbers from number_csv
    integer_set = {int(number) for number in number_csv.split(",")}
    return integer_set


# Lottery calculates 6 random numbers (b/w 1 and 20) ##########################

def create_lottery_numbers():
    """Generate 6 random lottery numbers"""
    values = set() # cannot initialize like so: {}
    while len(values) < 6:
        values.add(random.randint(1, 21))
    return values
    

# Then we match the user numbers to the lottery numbers #######################

def menu():
    """Ask player for numbers, Calculate lottery numbers,
    and Print out the winnings. Winnings defined as 100 to 
    the power of number of matched numbers."""
    player_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    match_count = len(player_numbers.intersection(lottery_numbers))
    
    print("You matched {m} of the 6 lottery numbers,\ntherefore winning ${d}."
          .format(m=match_count, d=100 ** match_count))


if __name__ == '__main__':
    menu()