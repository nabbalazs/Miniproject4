import random

class PrizeCalculator:

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

    def calculate_expected_prize(self):
        self.expected_prize = 0
        self.last_expected_prize = 0
        self.hits = int(input("Hány telitalálatos szelvény volt?"))
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
    calculator = PrizeCalculator()
    num_trials = calculator.number_of_players()
    expected_prize = calculator.calculate_expected_prize()
    print("Játékosszám:", num_trials)
    print("Várható főnyeremény:", expected_prize)