import tkinter as tk
import time
import random

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")

        self.root.geometry("400x600")

        self.is_running = False
        self.is_over = False
        self.start_time = 0
        self.elapsed_time = 0

        self.toggle_button = tk.Button(root, command=self.toggle_timer, bg="red")
        self.toggle_button.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky="nsew")

        self.ranking_label = tk.Label(root, text="1. 0.000\n2. 0.234\n3. 0.999", font=("Arial", 12))
        self.ranking_label.grid(row=0, column=1, columnspan=1)

        self.timer_label = tk.Label(root, text="0.000 seconds", font=("Arial", 12))
        self.timer_label.grid(row=1, column=1, columnspan=1, pady=20)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_timer)
        self.restart_button.grid(row=2, column=1, columnspan=1, sticky="s")

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(2, weight=5)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

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
            self.toggle_button.config(bg="green")
            self.update_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.is_over = True
            formatted_time = "{:.3f} seconds".format(self.elapsed_time)
            self.timer_label.config(text=formatted_time)
            self.toggle_button.config(bg="grey")

    def update_timer(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
        self.root.after(100, self.update_timer)

    def restart_timer(self):
        if not self.is_running:
            self.start_time = 0
            self.elapsed_time = 0
            self.toggle_button.config(bg="red")
            #self.timer_label.config(text="0.000 seconds")
            self.is_over = False



if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()