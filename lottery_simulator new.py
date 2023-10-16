import random
from getpass import getpass
from mysql.connector import connect, Error


def create_database(cursor, database_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print("The database has been created.")
    except Error as err:
        print(f"Error: {err}")

def drop_table(cursor, table_name):
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        print("The table has been dropped.")
    except Error as err:
        print(f"Error: {err}")

def create_table(cursor, table_name):
    try:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, first INT, second INT, third INT, fourth INT, fifth INT)")
        print("The table has been created.")
    except Error as err:
        print(f"Error: {err}")

def insert_ticket(cursor, table_name, selected_numbers):
    try:
        cursor.execute(f"INSERT INTO {table_name} (first, second, third, fourth, fifth) VALUES (%s, %s, %s, %s, %s)", selected_numbers)
    except Error as err:
        print(f"Error: {err}")

def simulate(num_trials, winning_numbers=[1, 13, 42, 56, 84]):
    singles, doubles, triples, quads, hits = 0, 0, 0, 0, 0

    # Set up MySQL connection
    try:
        connection = connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
        )
    except Error as err:
        print(f"Error: {err}")
        return

    database_name = "lottery_tickets"
    table_name = "tickets"

    # Create database and table
    cursor = connection.cursor()
    create_database(cursor, database_name)
    cursor.execute(f"USE {database_name}")
    drop_table(cursor, table_name)
    create_table(cursor, table_name)

    # Simulate lottery and insert data
    for _ in range(num_trials):
        # Simulate lottery
        selected_numbers = random.sample(range(1, 91), 5)
        TimesFound = sum(1 for num in selected_numbers if num in winning_numbers)

        # Update hits
        if TimesFound == 1:
            singles += 1
        elif TimesFound == 2:
            doubles += 1
        elif TimesFound == 3:
            triples += 1
        elif TimesFound == 4:
            quads += 1
        elif TimesFound == 5:
            hits += 1

        # Insert data into the table
        insert_ticket(cursor, table_name, selected_numbers)
        #print("The SQL table was successfully filled with new data.")

    print(
        f"{singles} 1-hits, {doubles} 2-hits, {triples} 3-hits, {quads} 4-hits and {hits} 5-hits"
    )
    return hits

# Example usage
simulate(1000000)