import random
import statistics

class WinningNumberGenerator:
    
    def __init__(self):
        self.mean = 45.5
        self.stdev = 44.5

    def generate_winning_numbers(self):
        num_list = []
        while len(num_list) < 5:
            num = int(random.normalvariate(self.mean, self.stdev))
            if 1 <= num <= 90 and num not in num_list:
                num_list.append(num)
        num_list.sort()
        return num_list
    
if __name__=="__main__":
    winning_number_generator = WinningNumberGenerator()
    winning_numbers = winning_number_generator.generate_winning_numbers()
    print("Nyerőszámok:", winning_numbers)
