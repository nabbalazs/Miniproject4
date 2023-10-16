import random

def simulate(num_trials, winning_numbers = [1,13,42,56,84]):
    doubles = 0
    triples = 0
    quads = 0
    hits = 0
    singles = 0

    # seed
    seed = random.randint(1,999999999)
    random.seed(seed)

    for _ in range(num_trials):
        numbers = list(range(1,91))
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

    # seed
    with open("seed_results.txt", 'w') as file:
        file.write("Seed: " + str(seed) + "\nTickets sold: " + str(num_trials))

    print(f"{singles} 1-hits, {doubles} 2-hits, {triples} 3-hits, {quads} 4-hits and {hits} 5-hits")
    return(hits)


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