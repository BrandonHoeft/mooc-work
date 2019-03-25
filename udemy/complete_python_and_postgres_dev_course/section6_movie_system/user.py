
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
        
    
    def watched_movies(self):
        '''
        return a list of movies that the user has watched
        '''
        watched_list = []
        for i, movie in enumerate(self.movies):
            if movie.watched: # movie iterable is a movie object. 
                watched_list.append(movie.name)
        return watched_list
    
    