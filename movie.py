# movie class

class Movie:
    def __init__(self, db, movieID=None, title=None, originalTitle=None, overview=None, runtime=None, releaseDate=None, voteAverage=None, voteCount=None):
        self.db = db
        self.movieID = movieID
        self.title = title
        self.originalTitle = originalTitle 
        self.overview = overview 
        self.runtime = runtime 
        self.releaseDate = releaseDate
        self.voteAverage = voteAverage
        self.voteCount = voteCount
    
    def search(self, db, title):
        # referenced: https://www.postgresql.org/docs/7.3/functions-matching.html to make the search case insensitive
        results = db.executeQuery(
            "SELECT * FROM movie WHERE title ILIKE %s",
            (f'%{title}%',)
        ) 
        if results:
            return results
        else:
            return None