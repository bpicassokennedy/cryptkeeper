# Author: Bella Picasso-Kennedy 
# Date: May 03, 2026
# Purpose: Defines the UserMovieActivity class, which provides a shared interface for managing
#          user interactions with movies in the PostgreSQL database. Intended to be extended by 
#          children that implement the add() and remove() methods.

class UserMovieActivity:
    def __init__(self, db, username, movieID):
        self.db = db
        self.username = username 
        self.movieID = movieID 
        
    def add(self):
        pass 
    
    def remove(self):
        pass 