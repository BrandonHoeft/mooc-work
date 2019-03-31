# The Purpose of the app: track what movies the user has watched and the order
# in which the user has watched them.

import sys
from os.path import expanduser
home = expanduser("~")
desktop_rel_path = '/Desktop/MOOC_work/udemy/complete_python_and_postgres_dev_course/section6_movie_system'
if home + desktop_rel_path not in sys.path:
    sys.path.insert(0, home+desktop_rel_path)
#from movie import Movie # No longer need to import, because 
from user import User

#user = User('Brandon')
user = User.load_from_file(home + desktop_rel_path + '/Brandon.txt')
print(user.movies)
#user.add_movie('The Matrix', 'Sci-Fi')
#user.add_movie('Game Night', 'Comedy')
#user.save_to_file()

#print(user) # This address is the memory address of where the user obj has been created and stored in memory.
#my_movie = Movie('The Matrix', 'Sci-Fi', True)
#print(my_movie)
#user.movies.append(my_movie)
#print(user.movies[0].name)
#print(user.movies[0].genre)

