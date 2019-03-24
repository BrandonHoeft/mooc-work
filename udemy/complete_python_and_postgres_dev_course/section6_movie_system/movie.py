class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        
    def __repr__(self):
        '''Description of the Movie class object when it is printed 
        after instantiation'''
        return '<Movie: {}, of the {} genre>'.format(self.name, self.genre)
        
        