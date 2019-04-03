# The Purpose of the app: track what movies the user has watched and the order
# in which the user has watched them.

import sys
from os.path import expanduser, isfile
home = expanduser("~")
desktop_rel_path = '/Desktop/MOOC_work/udemy/complete_python_and_postgres_dev_course/section6_movie_system'
if home + desktop_rel_path not in sys.path:
    sys.path.insert(0, home+desktop_rel_path)
from user import User
import json # for importing json-like objects from file. 


def menu():
    '''
    Ask for the user's name.
    Check if a file exists for that user.
    If it already exists, welcome them and load their data.
    If not, create a User object.
    
    Give them a list of actions:
        - Add a movie
        - See list of movies
            - Set a movie as watched
            - Delete a movie by name
        - See list of watched movies
        - Save and Quit
    '''
    name = input('please enter your name: ')
    filename = '{}.txt'.format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)
    
    user_input = input("Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set movie as watched,"
                       "'d' to delete a movie, 'l to see the list of watched movies, or 'q' to save and quite")   
    
    if user_input == 'a':
        movie_name = input('add movie name:')
        movie_genre = input('add movie genre: ')
        user.add_movie(movie_name, movie_genre)
    if user_input == 's':
        
    if user_input == 'w':
        pass
    if user_input == 'd':
        pass
    if user_input == 'l':
        pass
    if user_input == 'q':
        pass
    


def file_exists(filename):
    return isfile(filename)
menu()