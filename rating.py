# -----------------------------------------------------------------------------------
# Author: Bella Picasso-Kennedy 
# Date: May 03, 2026
# Purpose: Defines the Rating class, a child class of UserMovieActivity that manages 
#          a user's ratings in the PostgreSQL database.
# -----------------------------------------------------------------------------------

from user_movie_activity import UserMovieActivity 

class Rating(UserMovieActivity):
    def __init__(self, db, username, movieID, rating):
        super().__init__(db, username, movieID)
        self.rating = rating 
        
    def add(self):
        self.db.executeUpdate(
            """
            INSERT INTO rating (username, movieID, rating) 
            VALUES (%s, %s, %s) 
            ON CONFLICT (username, movieID) DO UPDATE SET rating = EXCLUDED.rating
            """,
            (self.username, self.movieID, self.rating)
        )
        
    def remove(self):
        self.db.executeUpdate(
            """
            DELETE FROM rating 
            WHERE username = %s AND movieID = %s
            """,
            (self.username, self.movieID)
        )