

from user_movie_activity import UserMovieActivity 

class Rating(UserMovieActivity):
    def __init__(self, db, username, movieID, rating):
        super().__init__(db, username, movieID)
        self.rating = rating 
        
    def add(self):
        self.db.executeUpdate(
            "INSERT INTO rating (username, movieID, rating) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
            (self.username, self.movieID, self.rating)
        )
        
    def remove(self):
        self.db.executeUpdate(
            "DELETE FROM rating WHERE username = %s AND movieID = %s",
            (self.username, self.movieID)
        )
    
    def update(self):
        self.db.executeUpdate(
            "UPDATE rating SET rating = %s WHERE username = %s AND movieID = %s",
            (self.rating, self.username, self.movieID)
        )
