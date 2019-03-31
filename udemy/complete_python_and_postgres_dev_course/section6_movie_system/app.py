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
import json # for importing json-like objects from file. 


user = User('Brandon')

user.add_movie('The Matrix', 'Sci-Fi')
user.add_movie('Game Night', 'Comedy')

print(user.json())

with open(home + desktop_rel_path + '/my_file.txt', 'w') as f:
    json.dump(user.json(), f)
    