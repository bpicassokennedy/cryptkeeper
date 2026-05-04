# CyrptKeeper
#### Bella Picasso-Kennedy 
#### CS 457: Database Management Systems Final Project
#### May 06, 2026

---

## Features 
A command-line horror movie tracking application inspired by *Letterboxd*, built with Python and PostgreSQL!

- User registration and login 
- Search horror movies by title 
- Add movies to a personal watchlist 
- Log watched movies with a date 
- Write and update reviews 
- Rate movies

---

## Data 
Horror movie data was sourced from [Kaggle Horror Movie Dataset](https://www.kaggle.com/datasets/evangower/horror-movies?resource=download) created by Evan Gower

---
## Setup 

**1) Install postgreSQL**

Download and install [PostgreSQL](https://www.postgresql.org/download/) 

**2) Install all dependencies**
```bash 
pip install psycopg pandas colorama
```

- `psycopg` - connects Python to PostgreSQL database 
- `pandas` - cleans and processes the raw CSV data 
- `colorama` - handles terminal text styling  

**3) Create the database**
```bash 
psql -U postgres 
CREATE DATABASE horror_movies_db;
```

**4) Create the tables**
```bash 
CREATE TABLE "user"( 
    username VARCHAR(255) PRIMARY KEY, 
    password VARCHAR(255)
);

CREATE TABLE movie(
    movieID INTEGER PRIMARY KEY, 
    title VARCHAR(255),
    originalTitle VARCHAR(255),
    overview TEXT,
    runtime INT,
    releaseDate DATE,
    voteAverage NUMERIC(3,1),
    voteCount INT 
);

CREATE TABLE watchlist(
    username VARCHAR(255),
    movieID INT,
    PRIMARY KEY (username, movieID),
    FOREIGN KEY (username) REFERENCES "user"(username),
    FOREIGN KEY (movieID) REFERENCES movie(movieID)
);

CREATE TABLE watchedlog(
    username VARCHAR(255),
    movieID INT,
    dateWatched DATE,
    PRIMARY KEY (username, movieID),
    FOREIGN KEY (username) REFERENCES "user"(username),
    FOREIGN KEY (movieID) REFERENCES movie(movieID)
);

CREATE TABLE review(
    username VARCHAR(255),
    movieID INT,
    review TEXT, 
    dateWritten DATE,
    PRIMARY KEY (username, movieID),
    FOREIGN KEY (username) REFERENCES "user"(username),
    FOREIGN KEY (movieID) REFERENCES movie(movieID)
);

CREATE TABLE rating(
    username VARCHAR(255),
    movieID INT,
    rating NUMERIC(3,1),
    PRIMARY KEY (username, movieID),
    FOREIGN KEY (username) REFERENCES "user"(username),
    FOREIGN KEY (movieID) REFERENCES movie(movieID)
);
```

**5) Populate the database**

Run once before launching the application to clean and load the movie dataset into the database
```bash
python3 data_cleaning.py
```

**6) Ensure database was populated correctly** 
```bash 
# how many rows were populated into the db
SELECT COUNT(*)
FROM movie

# first 20 titles from the db 
SELECT title
FROM movie 
LIMIT 20;

# release date should match the first 20 titles
SELECT releaseDate
FROM movie
LIMIT 20;

# overview should match the first 20 titles as well ^ 
SELECT overview
FROM movie
LIMIT 20;
```

**7) Run the application**
```bash 
python3 main.py 
```