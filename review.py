# -----------------------------------------------------------------------------------
# Author: Bella Picasso-Kennedy 
# Date: May 03, 2026
# Purpose: Defines the Review class, a child class of UserMovieActivity that manages 
#          a user's reviews in the PostgreSQL database.
# -----------------------------------------------------------------------------------

from user_movie_activity import UserMovieActivity

class Review(UserMovieActivity):
    def __init__(self, db, username, movieID, review, dateWritten):
        super().__init__(db, username, movieID)
        self.review = review
        self.dateWritten = dateWritten
        
    def add(self):
        self.db.executeUpdate(
            """
            INSERT INTO review (username, movieID, review, dateWritten) 
            VALUES (%s, %s, %s, %s) 
            ON CONFLICT (username, movieID) DO UPDATE SET review = EXCLUDED.review, dateWritten = EXCLUDED.dateWritten
            """,
            (self.username, self.movieID, self.review, self.dateWritten)
        )
        
    def remove(self):
        self.db.executeUpdate(
            """
            DELETE FROM review 
            WHERE username = %s AND movieID = %s"
            """,
            (self.username, self.movieID)
        )