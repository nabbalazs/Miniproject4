import tkinter as tk
import time
import random

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")

        self.root.geometry("600x450")

        self.is_running = False
        self.is_over = False
        self.start_time = 0
        self.elapsed_time = 0

        self.redbutton=tk.PhotoImage(file="Red_Button.png")
        self.greenbutton=tk.PhotoImage(file="Green_Button.png")
        self.graybutton=tk.PhotoImage(file="Gray_Button.png")
        self.restartbutton=tk.PhotoImage(file="Restart_Button.png")

        self.toggle_button = tk.Button(root, command=self.toggle_timer, image=self.redbutton)#, background="red")
        self.toggle_button.grid(row=0, column=0, rowspan=3, sticky="nsew")

        self.ranking_label = tk.Label(root, text=self.load_leaderboard(), font=("Arial", 12))
        self.ranking_label.grid(row=0, column=1, columnspan=1)

        self.timer_label = tk.Label(root, text="0.000 seconds", font=("Arial", 12))
        self.timer_label.grid(row=1, column=1, columnspan=1, pady=20)

        self.restart_button = tk.Button(root, command=self.restart_timer, image=self.restartbutton)

        root.grid_rowconfigure(0, weight=0)
        root.grid_rowconfigure(1, weight=0)
        root.grid_rowconfigure(2, weight=0)
        root.grid_columnconfigure(0, weight=0)
        root.grid_columnconfigure(1, weight=0)
        root.grid_columnconfigure(2, weight=0)

        self.update_timer()

    def toggle_timer(self):
        if not self.is_over:
            if self.is_running:
                self.stop_timer()
            else:
                self.start_timer()

    def start_timer(self):
        delay = float(random.uniform(1,5))
        print(delay)
        time.sleep(delay)
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True
            self.toggle_button.config(image=self.greenbutton)
            self.update_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.is_over = True
            formatted_time = "{:.3f} seconds".format(self.elapsed_time)
            self.timer_label.config(text=formatted_time)
            self.toggle_button.config(image=self.graybutton)
            self.restart_button.grid(row=2, column=1, sticky="s")
            self.update_leaderboard(formatted_time.strip(" seconds"))
            self.ranking_label.config(text=self.load_leaderboard())

    def update_timer(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
        self.root.after(100, self.update_timer)

    def restart_timer(self):
        if not self.is_running:
            self.start_time = 0
            self.elapsed_time = 0
            self.toggle_button.config(image=self.redbutton)
            #self.timer_label.config(text="0.000 seconds")
            self.is_over = False
            self.restart_button.grid_forget()

    def load_leaderboard(self, filename="Leaderboard"):
        try:
            with open(filename + ".txt", 'r', encoding='utf-8-sig') as file:
                file_content = file.readlines()

            first, second, third = file_content[:3]
        except:
            first="99.999"
            second="99.999"
            third="99.999"

        ranks = "1. "+first.strip()+"\n2. "+second.strip()+"\n3. "+third.strip()
        return ranks
    
    def update_leaderboard(self, new_score, filename="Leaderboard"):
        try:
            with open(filename + ".txt", 'r', encoding='utf-8-sig') as file:
                file_content = file.readlines()

            first, second, third = file_content[:3]
        except:
            first=99.999
            second=99.999
            third=99.999

        results=[float(first), float(second), float(third), float(new_score)]
        results = sorted(results)
        ranks = str(results[0]) + "\n" + str(results[1]) + "\n" + str(results[2]) + "\n"

        with open(filename + ".txt", 'w', encoding='utf-8-sig') as file:
            file.write(ranks)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()