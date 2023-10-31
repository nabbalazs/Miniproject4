class DrawNumber:
    
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
    
if __name__=="__main__":
    drawnumber = DrawNumber()
    draw_number = drawnumber.draw_number()
    print("Játékhét:", draw_number)