# because User module depends on Movie module and the modules aren't PythonPath by default.

import sys
from os.path import expanduser
home = expanduser("~")
desktop_rel_path = '/Desktop/MOOC_work/udemy/complete_python_and_postgres_dev_course/section6_movie_system'
if home + desktop_rel_path not in sys.path:
    sys.path.insert(0, home+desktop_rel_path)
    
from movie import Movie # see add_movie()




class User:
    '''
    Th User class, defines a user. The user can mark whether 
    or not movies were watched or not watched.
    '''
    def __init__(self, name):
        self.name = name # the user's name will be the name arg that gets passed in as a param when this class is instantiated.
        self.movies = []
        
    
    def __repr__(self): 
        '''
        Description of the User class object when it is printed after instantiation.
        '''
        return '<User {}>'.format(self.name)
            
    
    def add_movie(self, name, genre): # my_user_object.add_movie(name, genre)
        '''
        After importing the Movie class from movie module, 
        create a new Movie object, and by default it won't be watched.
        Append it to the User's movie list.
        '''
        movie = Movie(name, genre, False)
        self.movies.append(movie)
        
    def delete_movie(self, name): 
        '''
        Delete movie from the movies list, self.movies. inside the filter(), 
        movie is a lambda variable representing each element in self.movies. Each
        element in self.movies is Movie object with a name attribute that can
        be analyzed, and remove the one with the matching name from this func.
        '''
        self.movies =  list(filter(lambda movie: movie.name != name, self.movies))
        
    
    def watched_movies(self):
        '''
        return a list of movies that the user has watched
        '''
        return list(filter(lambda movie: movie.watched, self.movies))
    
    def save_to_file(self):
        with open('{}.txt'.format(home + desktop_rel_path + '/' + self.name), 'w') as f:
            f.write(self.name + '\n')
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))            
                
    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            username = content[0].rstrip()
            movies = []
            for line in content[1:]:
                movie_data = line.rstrip('\n').split(',')
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == 'True'))
        user = User(username) 
        user.movies = movies
        return user
        
            