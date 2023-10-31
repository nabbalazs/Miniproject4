import random
import statistics

class LotterySimulator:
    def __init__(self):
        self.mean = 45.5
        self.stdev = 44.5
        self.winning_numbers = []
        self.price = 300
        self.num_trials = 0
        self.income = 0
        self.expected_prize = 0
        self.hits = 0

    def draw_number(self):
        self.number_of_draw = 1
        with open("draw_number.txt", 'r') as file:
            line = file.readline()
            if line:
                self.number_of_draw = int(line)
                self.number_of_draw += 1
        with open("draw_number.txt", 'w') as file:
            file.write(str(self.number_of_draw))
        return self.number_of_draw

    def generate_winning_numbers(self):
        self.winning_numbers = []
        while len(self.winning_numbers) < 5:
            num = int(random.normalvariate(self.mean, self.stdev))
            if 1 <= num <= 90 and num not in self.winning_numbers:
                self.winning_numbers.append(num)
        self.winning_numbers.sort()
        return self.winning_numbers
    
    def number_of_players(self):
        with open("number_of_players.txt", 'r') as file:
            data = file.read()
            if data:
                with open("prize_change_rate.txt", 'r') as file:
                    line = file.readline()
                    if line:
                        self.rate = float(line)
                if self.rate >= 1:
                    self.num_trials = int(float(data) * random.uniform(1.1, 1.2))
                else:
                    self.num_trials = random.randint(2000000, 3000000)
            else:
                self.num_trials = random.randint(2000000, 3000000)
        with open("number_of_players.txt", 'w') as file:
            file.write(str(self.num_trials))
        return self.num_trials
    
    def simulate(self):
        
        doubles = 0
        triples = 0
        quads = 0
        self.hits = 0
        singles = 0

        for _ in range(self.num_trials):
            numbers = list(range(1, 90))
            selected_numbers = []
            TimesFound = 0

            for _ in range(5):
                length = len(numbers) - 1
                new_number = numbers[random.randint(0, length)]
                for a in self.winning_numbers:
                    if new_number == a:
                        TimesFound += 1
                selected_numbers.append(new_number)
                numbers.remove(new_number)

            if TimesFound == 1:
                singles += 1
            elif TimesFound == 2:
                doubles += 1
            elif TimesFound == 3:
                triples += 1
            elif TimesFound == 4:
                quads += 1
            elif TimesFound == 5:
                self.hits += 1

        new_content = ""
        for _ in range(self.num_trials):
            new_content += "\n" + str(selected_numbers)

        with open("results.txt", 'w') as file:
            file.write(str(new_content))

        #print(f"{singles} 1-hits, {doubles} 2-hits, {triples} 3-hits, {quads} 4-hits and {self.hits} 5-hits")
        return self.hits
    
    def calculate_expected_prize(self):
        self.expected_prize = 0
        self.last_expected_prize = 0
        self.hits
        self.price = 300
        self.income = self.num_trials * self.price
        self.rate = 0.00
        with open("expected_prize.txt", 'r') as file:
            line = file.readline()
            if line:
                self.last_expected_prize = float(line)
        if self.hits == 0:
            self.expected_prize += self.income / 2 + self.last_expected_prize
        else:
            self.expected_prize += self.income / 2
        with open("expected_prize.txt", 'r') as file:
            data = file.read()
            if data:
                self.rate = self.expected_prize / self.last_expected_prize
            else:
                self.rate = self.expected_prize / 300000000
        with open("prize_change_rate.txt", 'w') as file:
                    file.write(str(self.rate))
        with open("expected_prize.txt", 'w') as file:
            file.write(str(self.expected_prize))
        return self.expected_prize

if __name__=="__main__":
    simulator = LotterySimulator()
    draw_number = simulator.draw_number()
    num_of_players = simulator.number_of_players()
    winning_numbers = simulator.generate_winning_numbers()
    num_of_hits = simulator.simulate()
    expected_prize = simulator.calculate_expected_prize()
    print("Játékhét:", draw_number)
    print("Játékosszám:", num_of_players)
    print("Nyerőszámok:", winning_numbers)
    print("Telitalálatos szelvények száma:", num_of_hits)
    print("Várható főnyeremény:", expected_prize, "HUF")
