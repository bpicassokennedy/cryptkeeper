from database import Database 
from CLI import CLI

def main():
    db = Database()
    db.connect()
    
    cli = CLI(db)
    cli.startMenu()
    
    db.close()

if __name__ == "__main__":
    main()