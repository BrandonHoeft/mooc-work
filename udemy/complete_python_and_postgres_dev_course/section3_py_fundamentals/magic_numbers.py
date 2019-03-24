#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 16:04:48 2018
@author: bhoeft
"""

import random

# Create a list with two random numbers—each random number is created by random.randint(0, 9)
magic_numbers = [random.randint(0, 9), random.randint(0, 9)]

def ask_user_and_check_number():
    """Ask the user for a random number, and convert it 
    to an actual number using int()"""

    user_number = int(input('Enter a number between 0 and 9: '))
    if user_number in magic_numbers: # If the user's number is one of the random numbers generated above...
        return  'You got the number right!'
    if user_number not in magic_numbers:
        return 'You did not quite get it.'

def run_program_x_times(chances=1):    
    for attempt in range(chances):  # range(chances) is [0, 1, 2], so we're repeating this 3 times
        print('This is attempt number {}'.format(attempt))
        print(ask_user_and_check_number()) # Run the function above, and print the output

user_attempts = int(input('Enter the number of attempts: '))
run_program_x_times(user_attempts)












# Video: Generating Random Integers in Python
# Generate 10 random numbers.
# keep track of the minimum number generated.
# at the end, print out the minimum number that was generated.

# approach 1
#random_100 = random.choices(list(range(100)), k = 10)
#print("The minimum number generated was {m}".format(m = min(random_100)))

# approach using for loops
#minimum = 100
#for i in range(10):
#    random_number = random.randint(0, 100)
#    print("The number chosen at random is {}".format(random_number))
    
#    if random_number < minimum:
#        minimum = random_number

#print("The minimum number generated was {m}".format(m = minimum))
        