
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
        
    
