class Movie:
    '''
    A movie object that contains the name, genre, and a True/False
    boolean of whether or not the movie was watched. 
    '''
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched
        
    def __repr__(self):
        '''
        Description of the Movie class object when it is printed 
        after instantiation
        '''
        return '<Movie: {}>'.format(self.name)
            
    def create_json(self):
        '''
        return a dict that stores the name, genre, watched 
        indicator for the movie
        '''
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }