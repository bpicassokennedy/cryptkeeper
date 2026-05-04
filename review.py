

from user_movie_activity import UserMovieActivity

class Review(UserMovieActivity):
    def __init__(self, db, username, movieID, review, dateWritten):
        super().__init__(db, username, movieID)
        self.review = review
        self.dateWritten = dateWritten
        
    def add(self):
        self.db.executeUpdate(
            "INSERT INTO review (username, movieID, review, dateWritten) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
            (self.username, self.movieID, self.review, self.dateWritten)
        )
        
    def remove(self):
        self.db.executeUpdate(
            "DELETE FROM review WHERE username = %s AND movieID = %s",
            (self.username, self.movieID)
        )
    
    def update(self):
        self.db.executeUpdate(
            "UPDATE review SET review = %s, dateWritten = %s WHERE username = %s AND movieID = %s",
            (self.review, self.dateWritten, self.username, self.movieID)
        )
