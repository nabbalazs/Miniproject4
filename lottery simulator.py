import random
import struct
from getpass import getpass
from mysql.connector import connect, Error

def simulate(num_trials = 10, winning_numbers = [1,13,42,56,84]):
    doubles = 0
    triples = 0
    quads = 0
    hits = 0
    singles = 0

    savemethod = check_save_method()
    if savemethod == ": txt":
        with open("results.txt", 'w') as file:
            file.write("")
    elif savemethod == ": bin":
        with open("results.bin", 'w') as file:
            file.write("")
    elif savemethod == ": seed":
        with open("seed_results.txt", 'w') as file:
            file.write("")
        seed = random.randint(1,999999999)
        random.seed(seed)
    elif savemethod == ": sql":
            username=input("Enter username: ")
            password=getpass("Enter password: ")
            create_db_query = "CREATE DATABASE  IF NOT EXISTS lottery_tickets"
            drop_table_query = "DROP TABLE  IF EXISTS tickets"
            create_table_query = """
CREATE TABLE  IF NOT EXISTS tickets(
        id INT AUTO_INCREMENT PRIMARY KEY,
        first INT,
        second INT,
        third INT,
        fourth INT,
        fifth INT
    )
"""
            with connect(
                    host="localhost",
                    user=username,
                    password=password,
                ) as connection:
                    with connection.cursor() as cursor:
                        try:
                            cursor.execute(create_db_query)
                            cursor.execute("USE lottery_tickets")
                            cursor.execute(drop_table_query)
                            cursor.execute(create_table_query)
                            print("WARNING! The current version of the SQL database has been successfully deleted.")
                        except Error as err:
                            print(f"Something went wrong: {err}")



    for _ in range(num_trials):
        numbers = list(range(1,90))
        selected_numbers=[]
        TimesFound=0
        for _ in range(5):
            length = len(numbers)-1
            new_number = numbers[random.randint(0, length)]
            for a in winning_numbers:
                if new_number == a:
                    TimesFound += 1
            selected_numbers.append(new_number)
            numbers.remove(new_number)
        if TimesFound == 1:
            singles +=1
        elif TimesFound == 2:
            doubles +=1
        elif TimesFound == 3:
            triples +=1
        elif TimesFound == 4:
            quads +=1
        elif TimesFound == 5:
            hits +=1


        if savemethod == ": txt":
            with open("results.txt", 'r') as file:
                file_content = file.read()
                new_content = str(file_content)+"\n"+str(selected_numbers)
            with open("results.txt", 'w') as file:
                file.write(str(new_content))
        

        elif savemethod == ": bin":
            encoded_numbers = b''
            for _ in selected_numbers:
                encoded_numbers += struct.pack('B', _)
            with open("results.bin", 'wb') as file:
                file.write(encoded_numbers)
            with open("results.bin", 'rb') as file:
                decoded_numbers = []
                file_content = file.read()
                while file_content:
                    num, = struct.unpack('B', file_content[:1])
                    decoded_numbers.append(num)
                    file_content = file_content[1:]
            print(decoded_numbers)


        elif savemethod == ": seed":
            with open("seed_results.txt", 'w') as file:
                file.write("Seed: " + str(seed) + "\nTickets sold: " + str(num_trials))






        elif savemethod == ": sql":
            insert_ticket_query = """
INSERT INTO tickets (first, second, third, fourth, fifth)
VALUES
    ("%s", "%s", "%s", "%s", "%s")
""" % (
    selected_numbers[0],
    selected_numbers[1],
    selected_numbers[2],
    selected_numbers[3],
    selected_numbers[4]
)

            with connect(
                host="localhost",
                user=username,
                password=password,
                database="lottery_tickets",
            ) as connection:
                with connection.cursor() as cursor:
                    try:
                        cursor.execute(insert_ticket_query)
                    except Error as err:
                        print(f"Something went wrong: {err}")
            print("The SQL table was successfully filled with new data.")

    #doubles /= num_trials
    #triples /= num_trials
    #quads /= num_trials
    #singles /= num_trials
    print(f"{singles} 1-hits, {doubles} 2-hits, {triples} 3-hits, {quads} 4-hits and {hits} 5-hits")
    return(hits)



def check_save_method():
    with open("settings.txt", 'r', encoding='utf-8-sig') as file:
        file_content = file.readlines()
        settings=file_content[0].strip("Database type").strip()

    return settings



if __name__ == "__main__":
    num_trials = int(input("Number of players: "))
    winning_numbers =  input("Please enter the 5 winning numbers separated by spaces: ")
    numbers = winning_numbers.split(" ")  # Splits the input into a list of strings
    number_list = [int(num) for num in numbers]

    if len(number_list) == 5:
        expected_duplicates = simulate(num_trials, number_list)
        print("Hits:", expected_duplicates)
    else:
        print("Error")