from getpass import getpass
from mysql.connector import connect, Error

def create():
    create_movies_table_query = """
    CREATE TABLE movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        genre VARCHAR(100),
        collection_in_mil INT
    )
    """

    create_reviewers_table_query = """
    CREATE TABLE reviewers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
    )
    """

    #review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    create_ratings_table_query = """
    CREATE TABLE ratings (
        movie_id INT,
        reviewer_id INT,
        rating DECIMAL(2,1),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
        PRIMARY KEY(movie_id, reviewer_id)
    )
    """


    try:
        with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(create_movies_table_query)
                cursor.execute(create_reviewers_table_query)
                cursor.execute(create_ratings_table_query)
                connection.commit()
    except Error as e:
        print(e)











def describe():
    # column; datatype; is_required?; is_key? (PRI); default_value; autoincrement etc.;
    show_table_query = "DESCRIBE movies"

    try:
        with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(show_table_query)
                # Fetch rows from last executed query
                result = cursor.fetchall()
                for row in result:
                    print(row)
    except Error as e:
        print(e)








def alter():
    # column; datatype; is_required?; is_key? (PRI); default_value; autoincrement etc.;
    alter_table_query = """
ALTER TABLE movies
MODIFY COLUMN collection_in_mil DECIMAL(4,1)
"""
    show_table_query = "DESCRIBE movies"


    try:
        with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(alter_table_query)
                cursor.execute(show_table_query)
                # Fetch rows from last executed query
                result = cursor.fetchall()
                print("Movie Table Schema after alteration:")
                for row in result:
                    print(row)

    except Error as e:
        print(e)






def delete():
    drop_table_query = "DROP TABLE ratings"
    
    with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(drop_table_query)





def execute():
    insert_movies_query = """
INSERT INTO movies (title, release_year, genre, collection_in_mil)
VALUES
    ("Forrest Gump", 1994, "Drama", 330.2),
    ("3 Idiots", 2009, "Drama", 2.4),
    ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
    ("Good Will Hunting", 1997, "Drama", 138.1),
    ("Skyfall", 2012, "Action", 304.6),
    ("Gladiator", 2000, "Action", 188.7),
    ("Black", 2005, "Drama", 3.0),
    ("Titanic", 1997, "Romance", 659.2),
    ("The Shawshank Redemption", 1994, "Drama",28.4),
    ("Home Alone", 1990, "Comedy", 286.9)
"""
    with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(insert_movies_query)
                connection.commit()







def executemany():
    insert_reviewers_query = """
INSERT INTO reviewers
(first_name, last_name)
VALUES ( %s, %s )
"""
    reviewers_records = [
    ("Chaitanya", "Baweja"),
    ("Mary", "Cooper"),
    ("John", "Wayne"),
    ("Thomas", "Stoneman"),
    ("Penny", "Hofstadter"),
    ("Mitchell", "Marsh"),
    ("Wyatt", "Skaggs"),
    ("Sheldon", "Cooper"),
    ("Kimbra", "Masters"),
    ("Amy", "Farah Fowler")
]
    with connect(
            host="localhost",
            user="root",#input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(insert_reviewers_query, reviewers_records)
                connection.commit()




def executemany_b():
    insert_ratings_query = """
    INSERT INTO ratings
    (rating, movie_id, reviewer_id)
    VALUES ( %s, %s, %s)
    """
    ratings_records = [
        (6.4, 7, 5), (5.6, 9, 1), (6.3, 2, 4), (5.1, 1, 7),
        (5.0, 5, 5), (6.5, 1, 5), (8.5, 3, 3), (9.7, 6, 10),
        (8.5, 4, 2), (9.9, 4, 9), (8.7, 6, 4), (9.9, 6, 1),
        (5.1, 3, 6), (5.4, 8, 6), (6.2, 6, 2), (7.3, 1, 9),
        (8.1, 7, 8), (5.0, 7, 2), (9.8, 3, 10), (8.0, 2, 9),
        (8.5, 1, 3), (5.0, 5, 1), (5.7, 8, 2), (7.6, 2, 10),
        (5.2, 8, 5), (9.7, 10, 3), (5.8, 8, 8), (5.8, 10, 5),
        (8.4, 2, 8), (6.2, 10, 6), (7.0, 10, 8), (9.5, 10, 2),
        (8.9, 3, 9), (6.4, 2, 2), (7.8, 9, 2), (9.9, 5, 3),
        (7.5, 2, 7), (9.0, 5, 6), (8.5, 3, 2), (5.3, 10, 7),
        (8.1, 5, 2), (5.7, 2, 1), (6.3, 8, 4),
    ]
    with connect(
                host="localhost",
                user="root",#input("Enter username: "),
                password=getpass("Enter password: "),
                database="online_movie_rating",
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.executemany(insert_ratings_query, ratings_records)
                    connection.commit()








def select():
    select_movies_query = "SELECT * FROM movies LIMIT 5"
    #"SELECT * FROM movies LIMIT 2,5" #3-tól 7-ig adja vissza
    #"SELECT title, release_year FROM movies LIMIT 5"
    with connect(
                host="localhost",
                user="root",#input("Enter username: "),
                password=getpass("Enter password: "),
                database="online_movie_rating",
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(select_movies_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)






def orderby():
    select_movies_query = """
SELECT title, collection_in_mil
FROM movies
WHERE collection_in_mil > 300
ORDER BY collection_in_mil DESC
"""
    with connect(
                host="localhost",
                user="root",#input("Enter username: "),
                password=getpass("Enter password: "),
                database="online_movie_rating",
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(select_movies_query)
                    for movie in cursor.fetchall():
                        print(movie)






def concat():
    select_movies_query = """
SELECT CONCAT(title, " (", release_year, ")"),
      collection_in_mil
FROM movies
ORDER BY collection_in_mil DESC
LIMIT 5
"""
    with connect(
            host="localhost",
            user="root",#input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                for movie in cursor.fetchall():
                    print(movie)





def fetchmany():
    select_movies_query = """
SELECT CONCAT(title, " (", release_year, ")"),
      collection_in_mil
FROM movies
ORDER BY collection_in_mil DESC
"""
    with connect(
            host="localhost",
            user="root",#input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                for movie in cursor.fetchmany(size=5):
                    print(movie)
                cursor.fetchall()

# A .fetchmany()-vel kapott kimenet hasonló az előző LIMIT clause-zal kapott eredményhez. Észrevehettél egy további cursor.fetchall() hívást a végén. Ez azért van ott, hogy töröld az összes olvasatlan eredményt, amelyet a .fetchmany() nem olvasott be.
# Fontos, hogy töröld az összes olvasatlan eredményt, mielőtt más utasításokat hajtasz végre ugyanazon a kapcsolaton. Ellenkező esetben egy InternalError: Unread result found kivétel fog dobódni.






def innerjoin():
    select_movies_query = """
SELECT title, AVG(rating) as average_rating
FROM ratings
INNER JOIN movies
    ON movies.id = ratings.movie_id
GROUP BY movie_id
ORDER BY average_rating DESC
LIMIT 5
"""
    with connect(
            host="localhost",
            user="root",#input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                for movie in cursor.fetchall():
                    print(movie)






def update():
    update_query = """
UPDATE
    reviewers
SET
    last_name = "Cooper"
WHERE
    first_name = "Amy"
"""
    with connect(
            host="localhost",
            user="root",#input("Enter username: "),
            password=getpass("Enter password: "),
            database="online_movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(update_query)
                connection.commit()





select()