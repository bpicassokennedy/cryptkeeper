# -----------------------------------------------------------------------------------
# Author: Bella Picasso-Kennedy 
# Date: May 03, 2026
# Purpose: Defines the DataCleaning class, which processes raw CSV data and inserts
#          validated records into the PostgreSQL database.
# -----------------------------------------------------------------------------------

import pandas as pd # for data manipulation
from database import Database 

class DataCleaning:
    def __init__(self, csv_file, db):
        self.csv_file = csv_file
        self.db = db
        self.movies = pd.read_csv(csv_file)
        
        # rename raw csv column headers to the names expected by the database schema (id -> movieID)
        self.movies = self.movies.rename(columns={
            'id': 'movieID',
            'title': 'title',
            'original_title': 'originalTitle',
            'overview': 'overview',
            'runtime': 'runtime',
            'release_date': 'releaseDate',
            'vote_average': 'voteAverage',
            'vote_count': 'voteCount'
        })
        
        # drops all columns that won't be used in the database
        self.movies = self.movies[['movieID', 'title', 'originalTitle', 'overview', 'runtime', 'releaseDate', 'voteAverage', 'voteCount']]
        
        # no description put n/a
        self.movies['overview'] = self.movies['overview'].fillna("N/A")
        
        # no negative runtimes 
        self.movies = self.movies[self.movies['runtime'] > 0]
        
        # no duplicate movie ids 
        self.movies = self.movies.drop_duplicates(subset=['movieID'])
        
        # valid release dates only 
        self.movies['releaseDate'] = pd.to_datetime(self.movies['releaseDate'], errors='coerce')
        self.movies = self.movies.dropna(subset=['releaseDate'])
        
        # no trailing spaces
        self.movies['title'] = self.movies['title'].str.strip()
        self.movies['overview'] = self.movies['overview'].str.strip()
        
        self.insertMovie()
    
    # insert valid movies into the db      
    def insertMovie(self):
        for _, row in self.movies.iterrows():
            # referenced: https://www.postgresql.org/docs/current/sql-insert.html for on conlfict do nothing
            # on conflict do nothing does not allow a row with the same primary key to be added to the database
            self.db.executeUpdate(
                """
                INSERT INTO movie(movieID, title, originalTitle, overview, runtime, releaseDate, voteAverage, voteCount)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING; 
                """,
                (
                    row['movieID'],
                    row['title'],
                    row['originalTitle'],
                    row['overview'],
                    row['runtime'],
                    row['releaseDate'],
                    row['voteAverage'],
                    row['voteCount']
                )
            )
        print(f"exported! {len(self.movies)} rows imported")
        
def load():
    db  = Database()
    db.connect()
    DataCleaning("horror_movies.csv", db)
    db.close()

load()