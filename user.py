from colorama import * 

class User:
    def __init__(self, db):
        self.db = db 
        self.username = None
        self.password = None
        
    def register(self, username, password):
        existing = self.db.executeQuery(
            "SELECT username FROM \"user\" WHERE username = %s",
            (username,)
        )
        
        if existing:
            print()
            print(f"Username already taken, try another" + Style.RESET_ALL)
            return False
        
        self.db.executeUpdate(
            "INSERT INTO \"user\" (username, password) VALUES (%s, %s)",
            (username, password)
        )
        
        self.username = username
        self.password = password 
        
        print()
        print(Style.RESET_ALL + Fore.GREEN + f"Welcome, {username}!" + Style.RESET_ALL)
        
        return True
    
    def login(self, username, password):
        result = self.db.executeQuery(
            "SELECT username FROM \"user\" WHERE username = %s AND password = %s",
            (username, password)
        )
        
        if result:
            self.username = username
            print()
            print(Style.RESET_ALL + Fore.GREEN + f"Welcome back, {username}!" + Style.RESET_ALL)
            return True 
        else:
            print() 
            print(f"Invalid username or password" + Style.RESET_ALL)
            return False
        
    def logout(self):
        self.username = None
        print()
        print(Fore.WHITE + Style.DIM + 'Logged out successfully' + Style.RESET_ALL)
        
    def viewProfile(self):
        print()
        print(Fore.RED + f"=== {self.username} Profile ===" + Style.RESET_ALL)
