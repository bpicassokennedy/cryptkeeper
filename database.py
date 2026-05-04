# Author: Bella Picasso-Kennedy 
# Date: May 03, 2026
# Purpose: Defines the Database class, that establishes and manages the connection 
#          to the horror_movies_db PostgreSQL database. 

import psycopg

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None 
    
    # open connection to horror_movie_db using psycopg    
    def connect(self):
        self.conn = psycopg.connect("dbname=horror_movies_db user=postgres password=Dahlia0807")
        self.cursor = self.conn.cursor()
    
    # execute a select style query with the cursor and return all matches
    def executeQuery(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    # execute a write operation, that allow changes to persist to the database
    def executeUpdate(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()
    
    # checks the cursor and conn exist before attempting to close them
    # releases connection cleanly    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()