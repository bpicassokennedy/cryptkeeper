# -----------------------------------------------------------------------------------
# Author: Bella Picasso-Kennedy 
# Date: May 03, 2026 
# Purpose: Defines the User class, which handles user authentication, and 
#          profile display, including registration ,login, and logout functionality.
# -----------------------------------------------------------------------------------

from colorama import * 

class User:
    def __init__(self, db):
        self.db = db 
        self.username = None
        self.password = None
        
    def register(self, username, password):
        existing = self.db.executeQuery(
            """
            SELECT username FROM \"user\" 
            WHERE username = %s
            """,
            (username,)
        )
        
        # if username already exists don't allow it to be inserted into the db
        if existing:
            print()
            print(f"Username already taken, try another" + Style.RESET_ALL)
            return False
        
        # username is free and can be added to the db
        self.db.executeUpdate(
            """
            INSERT INTO \"user\" (username, password) 
            VALUES (%s, %s)
            """,
            (username, password)
        )
        
        self.username = username
        self.password = password 
        
        print()
        print(Style.RESET_ALL + Fore.GREEN + f"Welcome, {username}!" + Style.RESET_ALL)
        
        return True
    
    def login(self, username, password):
        # needs a matching name and password
        result = self.db.executeQuery(
            """SELECT username FROM \"user\" 
            WHERE username = %s AND password = %s
            """,
            (username, password)
        )
        
        # if result exists in the db allow them to login 
        if result:
            self.username = username
            print()
            print(Style.RESET_ALL + Fore.GREEN + f"Welcome back, {username}!" + Style.RESET_ALL)
            return True 
        # result does not exist in the db
        else:
            print() 
            print(f"Invalid username or password" + Style.RESET_ALL)
            return False
        
    def logout(self):
        # clear session state
        self.username = None
        print()
        print(Fore.WHITE + Style.DIM + 'Logged out successfully' + Style.RESET_ALL)
    
    # prints profile header using the currently authenticated usenrname    
    def viewProfile(self):
        print()
        print(Fore.RED + f"=== {self.username} Profile ===" + Style.RESET_ALL)