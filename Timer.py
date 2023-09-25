import tkinter as tk
import time
import random

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        self.is_running = False
        self.is_over = False
        self.start_time = 0
        self.elapsed_time = 0

        self.timer_label = tk.Label(root, text="0.000 seconds", font=("Arial", 24))
        self.timer_label.pack(pady=20)

        self.toggle_button = tk.Button(root, text="Start", command=self.toggle_timer, bg="red")
        self.toggle_button.pack()

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_timer)
        self.restart_button.pack()

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
            self.toggle_button.config(text="Stop", bg="green")
            self.update_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.is_over = True
            self.toggle_button.config(text="Start", bg="grey")

    def update_timer(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            formatted_time = "{:.3f} seconds".format(self.elapsed_time)
            self.timer_label.config(text=formatted_time)
        self.root.after(100, self.update_timer)

    def restart_timer(self):
        if not self.is_running:
            self.start_time = 0
            self.elapsed_time = 0
            self.toggle_button.config(text="Start", bg="red")
            self.timer_label.config(text="0.000 seconds")
            self.is_over = False



if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()