

from user_movie_activity import UserMovieActivity 

class WatchList(UserMovieActivity):
    def __init__(self, db, username, movieID):
        super().__init__(db, username, movieID)
       
    def add(self):
        self.db.executeUpdate(
            "INSERT INTO watchlist (username, movieID) VALUES (%s, %s) ON CONFLICT DO NOTHING",
            (self.username, self.movieID)
        )
        
    def remove(self):
        self.db.executeUpdate(
            "DELETE FROM watchlist WHERE username = %s AND movieID = %s",
            (self.username, self.movieID)
        )
    
    