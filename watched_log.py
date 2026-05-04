

from user_movie_activity import UserMovieActivity 

class WatchedLog(UserMovieActivity):
    def __init__(self, db, username, movieID, dateWatched):
        super().__init__(db, username, movieID)
        self.dateWatched = dateWatched
        
    def add(self):
        self.db.executeUpdate(
            "INSERT INTO watchedlog (username, movieID, dateWatched) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
            (self.username, self.movieID, self.dateWatched)
        )
        
    def remove(self):
        self.db.executeUpdate(
            "DELETE FROM watchedlog WHERE username = %s AND movieID = %s",
            (self.username, self.movieID)
        )
