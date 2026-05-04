


import psycopg

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None 
        
    def connect(self):
        self.conn = psycopg.connect("dbname=horror_movies_db user=postgres password=Dahlia0807")
        self.cursor = self.conn.cursor()
    
    def executeQuery(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def executeUpdate(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()
        
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()