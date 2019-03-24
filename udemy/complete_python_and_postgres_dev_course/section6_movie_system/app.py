import sys
from os.path import expanduser
from movie import Movie
from user import User

home = expanduser("~")
desktop_rel_path = '/Desktop/MOOC_work/udemy/complete_python_and_postgres_dev_course/section6_movie_system'
sys.path.insert(0, home+desktop_rel_path)

user = User('Brandon')
print(user) # This address is the memory address of where the user obj has been created and stored in memory.

my_movie = Movie('The Matrix', 'Sci-Fi')
print(my_movie)

user.movies.append(my_movie)
print(user.movies[0].name)
print(user.movies[0].genre)
