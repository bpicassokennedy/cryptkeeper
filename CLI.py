# Author: Bella Picasso-Kennedy
# Date: May 03, 2026 
# Purpose: Defines the CLI class, which provides a command-line interface for users to interact 
#          with the horror movie database, including searching, logging, and managing personal
#          movie activity.

from colorama import * # used for text color in terminal https://pypi.org/project/colorama/ 
from user import User 
from movie import Movie 
from watchlist import WatchList
from watched_log import WatchedLog
from rating import Rating 
from review import Review
from datetime import date # used for movie rating

class CLI:
    def __init__(self, db):
        self.db = db 
        # used to track who is logged in
        self.currentUser = None 
    
    # application entry point
    def startMenu(self):
        while True:
            print()
            print(Fore.RED + '=== CryptKeeper ===' + Style.RESET_ALL)
            print("1. Login")
            print("2. Register")
            print("3. Quit")
            print(Fore.RED + "===============" + Style.RESET_ALL)
            
            print()
            choice = input(Fore.YELLOW + 'Enter your choice: ')
            
            if choice == "1":
                self.login()
            elif choice == "2":
                self.register()
            elif choice == "3":
                print()
                print(Style.DIM + Fore.WHITE + 'Goodbye!' + Style.RESET_ALL)
                break
            else:
                print()
                print(Fore.WHITE + Style.DIM + "Invalid choice, try again!" + Style.RESET_ALL)
                    
    def login(self):
        print(Style.RESET_ALL)
        username = input(Fore.WHITE + Style.DIM + 'Username: ') 
        password = input("Password: ")
        user = User(self.db)
        
        # handles credential validation against the db
        if user.login(username, password):
            # store authenticated username
            self.currentUser = username
            # store user object itself
            self.user = user
            self.mainMenu()
    
    def register(self):
        print(Style.RESET_ALL)
        username = input(Fore.WHITE + Style.DIM + "Choose a username: ")
        password = input("Choose a password: ")
        user = User(self.db)
        if user.register(username, password):
            self.currentUser = username
            self.user = user
            self.mainMenu()
       
    # main menu after user logs in or completes registration       
    def mainMenu(self):
        while True: 
            print()
            print(Fore.RED + '=== Main Menu ===' + Style.RESET_ALL)
            print("1. Search Movie Catalog")
            print("2. View Profile")
            print("3. Logout")
            print(Fore.RED + "=================" + Style.RESET_ALL)
            
            print()
            choice = input(Fore.YELLOW + 'Enter your choice: ')
            
            if choice == "1":
                self.searchResults()
            elif choice == "2":
                self.showProfile()
            elif choice == "3":
                self.user.logout()
                self.currentUser = None
                self.user = None
                break
            else:
                print()
                print(Fore.WHITE + Style.DIM + "Invalid choice, try again!" + Style.RESET_ALL)
    
    # show signed in users profile            
    def showProfile(self):
        self.user.viewProfile()
        print(Style.RESET_ALL + '1. View Watchlist')
        print("2. View Watched Log")
        print("3. View Reviews")
        print("4. View Ratings")
        print("B. Back")
        print(Fore.RED + "===================" + Style.RESET_ALL)
        
        print()
        choice = input(Fore.YELLOW + 'Enter your choice: ')
        
        if choice == "1":
            self.showWatchList()
        elif choice == "2":
            self.showWatchedLog()
        elif choice == "3":
            self.showReviews()
        elif choice == "4":
            self.showRatings()
        elif choice.upper() == 'B':
            return
        else: 
            print()
            print(Fore.WHITE + Style.DIM + "Invalid choice, try again!" + Style.RESET_ALL)
    
    # show movie details and allow users to choose how they want to interact with the movie
    def movieDetails(self, row):
        # row indices: 0=movieID, 1=title, 2=originalTitle, 3=overview, 
        #              4=runtime, 5=releaseDate, 6=voteAverage, 7=voteCount
        print()
        print(Fore.RED + '=== Movie Details ===' + Style.RESET_ALL)
        print(f"Title: {row[1]}")
        print(Fore.WHITE + Style.DIM + f"Original Title: {row[2]}" + Style.RESET_ALL) 
        print()
        print(f"Overview: {row[3]}")
        print()
        print(f"Runtime: {row[4]} mins")
        print(f"Release Date: {row[5]}")
        print(f"Rating: {row[6]}/10 ({row[7]} votes)")
        print(Fore.RED + '======================' + Style.RESET_ALL)
        
        print()
        print("1. Add to Watchlist")
        print("2. Add to Watched Log")
        print("3. Leave a Review")
        print("4. Rate it")
        print("B. Back")
        
        print()
        choice = input(Fore.YELLOW + 'Enter your choice: ')
        
        if choice == "1":
            w = WatchList(self.db, self.currentUser, row[0])
            w.add()
        elif choice == "2":
            # add to watched log with date watched
            print()
            dateWatched = input(Style.RESET_ALL + 'Enter date watched (YYYY-MM-DD): ')
            wl = WatchedLog(self.db, self.currentUser, row[0], dateWatched)
            wl.add()
            
            # remove from watchlist if it's there 
            w = WatchList(self.db, self.currentUser, row[0])
            w.remove()
        elif choice == "3":
            # write review 
            print()
            review = input(Style.RESET_ALL + 'Write your review: ')
            r = Review(self.db, self.currentUser, row[0], review, date.today())
            r.add()
            
            # add to watched log, if already there it will skip it  
            dateWatched = input("When did you watch it? (YYYY-MMM-DD): ")
            wl = WatchedLog(self.db, self.currentUser, row[0], dateWatched)
            wl.add()
            
            # remove from watchlist 
            w = WatchList(self.db, self.currentUser, row[0])
            w.remove()
        elif choice == "4":
            print()
            rating = input(Style.RESET_ALL + 'Enter your rating (0-10): ')
            r = Rating(self.db, self.currentUser, row[0], float(rating))
            r.add()
            
            # add to watched log, if already there it will skip it 
            dateWatched = input("When did you watch it? (YYYY-MMM-DD): ")
            wl = WatchedLog(self.db, self.currentUser, row[0], dateWatched)
            wl.add()
            
            # remove from watchlist 
            w = WatchList(self.db, self.currentUser, row[0])
            w.remove()
        elif choice.upper() == 'B':
            return
        else: 
            print()
            print(Fore.WHITE + Style.DIM + 'Invalid choice, try again!' + Style.RESET_ALL)
    
    def searchResults(self):
        # keep this running until the user decides to navigate back
        while True:
            print()
            title = input("Enter a movie title: ")
            
            # instantiate a movie object 
            movie = Movie(self.db)
            # call search method to find movies with matching titles
            results = movie.search(self.db, title)
            
            # query returned nothing
            if not results:
                print()
                print(Fore.WHITE + Style.DIM + "No movies found, try again" + Style.RESET_ALL)
                continue 
            
            while True: 
                print()
                print(Fore.RED + '=== Search Results ===' + Style.RESET_ALL)
                for i, row in enumerate(results, 1):
                    print(f"{i}. {row[1]} ({row[5].year})")
            
                print()
                print("0. Search again")
                print("B. Back")
                print(Fore.RED + "=====================" + Style.RESET_ALL)
                
                print()
                choice = input(Fore.YELLOW + "Enter a number to see details or 'B' to go back: ")
            
                if choice.upper() == 'B':
                    return
                elif choice == '0':
                    break
                
                try: 
                    # convert user's input to int and subtract 1 to get correct index
                    index = int(choice) - 1
                    # index falls within valid range
                    if 0 <= index < len(results):
                        self.movieDetails(results[index])
                    # index is out of range
                    else:
                        print()
                        print(Fore.WHITE + Style.DIM + "Invalid choice, try again!" + Style.RESET_ALL)
                # handles input that cannot be converted to an int 
                except ValueError:
                    print("Invalid choice, try again!")
       
    def showWatchList(self):
        # find all movies on the current user's watchlist
        results = self.db.executeQuery(
            """
            SELECT m.movieID, m.title, m.releaseDate
            FROM movie m 
            JOIN watchlist w ON m.movieID = w.movieID
            WHERE w.username = %s
            """,
            (self.currentUser,)
        )
        
        if not results:
            print()
            print(Fore.WHITE + Style.DIM + "Watchlist is empty!" + Style.RESET_ALL)
            self.showProfile()
            return
        
        print()
        print(Fore.RED + '==== Watchlist ====' + Style.RESET_ALL)
        for i, row in enumerate(results, 1):
            # print movie along with release date (for movies w/ the same title)
            print(f"{i}. {row[1]} ({row[2].year})")

        self.selectMovie(results)
        self.showProfile()
            
    def showWatchedLog(self):
        results = self.db.executeQuery(
            """
            SELECT m.movieID, m.title, w.dateWatched
            FROM movie m 
            JOIN watchedlog w ON m.movieID = w.movieID
            WHERE w.username = %s
            """,
           (self.currentUser,) 
        )
        
        if not results:
            print()
            print(Fore.WHITE + Style.DIM + "Watched log is empty!" + Style.RESET_ALL)
            self.showProfile()
            return 
        
        print()
        print(Fore.RED + '=== Watched Log ===' + Style.RESET_ALL)
        for i, row in enumerate(results, 1):
            # movie title, with date watched (yyyy-mm-dd format)
            print(f"{i}. {row[1]} (Watched: {row[2]})")
        
        self.selectMovie(results)
        self.showProfile()

    def showReviews(self):
        results = self.db.executeQuery(
            """
            SELECT m.movieID, m.title, r.review, r.dateWritten
            FROM movie m 
            JOIN review r ON m.movieID = r.movieID
            WHERE r.username = %s
            """,
            (self.currentUser,)
        )
        
        if not results:
            print()
            print(Fore.WHITE + Style.DIM + "No reviews yet!" + Style.RESET_ALL)
            self.showProfile()
            return 
        
        print()
        print(Fore.RED + '===== Reviews =====' + Style.RESET_ALL)
        # display movie title, review written, and date written
        for i, row in enumerate(results, 1):
            print(f"{i}. {row[1]}")
            print(f"Review: {row[2]}")
            print(f"Written: {row[3]}")
        
        self.selectMovie(results)
        self.showProfile()
   
    def showRatings(self):
        results = self.db.executeQuery(
            """
            SELECT m.movieID, m.title, r.rating 
            FROM movie m 
            JOIN rating r ON m.movieID = r.movieID
            WHERE r.username = %s
            """,
            (self.currentUser,)
        )

        if not results:
            print()
            print(Fore.WHITE + Style.DIM + "No ratings yet!" + Style.RESET_ALL)
            self.showProfile()
            return 
        
        print(Fore.RED + '===== Ratings =====' + Style.RESET_ALL) 
        for i, row in enumerate(results, 1):
            # show movie title, and rating of movie out of ten
            print(f"{i}. {row[1]} - {row[2]}/10")
        
        self.selectMovie(results)
        self.showProfile()
    
    # function to select movie since this is repeated multiple times
    def selectMovie(self, results):
        print(Fore.RED + '===================' + Style.RESET_ALL)
        print()
        choice = input(Fore.YELLOW + "Enter a number to see details or 'B' to go back: ")
        
        # return control to whichever profile view method called it 
        if choice.upper() == 'B':
            return 
        
        try:  
            # convert index number to make sure we're accessing the right row
            index = int(choice) - 1
            # validates that index falls within the bounds of the result set before attempting to access it
            if 0 <= index < len(results):
                full = self.db.executeQuery(
                    """
                    SELECT * 
                    FROM movie 
                    WHERE movieID = %s
                    """,
                    (results[index][0],)
                )
                self.movieDetails(full[0])
            else:
                print()
                print(Fore.WHITE + Style.DIM + "Invalid choice, try again!" + Style.RESET_ALL)
        except ValueError:
            print("Invalid choice, try again!")