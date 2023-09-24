import tkinter as tk
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.timer_label = tk.Label(root, text="0.000 seconds", font=("Arial", 24))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        self.update_timer()

    def start_timer(self):
        self.start_time = 0
        self.elapsed_time = 0
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.update_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            formatted_time = "{:.3f} seconds".format(self.elapsed_time)
            self.timer_label.config(text=formatted_time)
        self.root.after(100, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()