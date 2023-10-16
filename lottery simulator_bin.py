import random
import struct

def simulate(num_trials, winning_numbers = [1,13,42,56,84]):
    doubles = 0
    triples = 0
    quads = 0
    hits = 0
    singles = 0

    # bin
    encoded_numbers = b''

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
        
        # bin
        for _ in selected_numbers:
            encoded_numbers += struct.pack('B', _)

    with open("results.bin", 'wb') as file:
        file.write(encoded_numbers)

    print(f"{singles} 1-hits, {doubles} 2-hits, {triples} 3-hits, {quads} 4-hits and {hits} 5-hits")
    return(hits)



#unused
def decode_bin():
    with open("results.bin", 'rb') as file:
        decoded_numbers = []
        file_content = file.read()
        while file_content:
            num, = struct.unpack('B', file_content[:1])
            decoded_numbers.append(num)
            file_content = file_content[1:]
    print(decoded_numbers)


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