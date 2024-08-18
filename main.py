import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.minsize(300, 400)

        self.number_to_guess = random.randint(1, 100)

        self.title_font = ("Helvetica", 16, "bold")
        self.button_font = ("Helvetica", 14)
        self.result_font = ("Helvetica", 14, "italic")

        self.label = tk.Label(root, text="Guess a number between 1 and 100:", font=self.title_font)
        self.label.pack(pady=10)

        self.guess_entry = tk.Entry(root, font=self.button_font, width=5)
        self.guess_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Guess", font=self.button_font, command=self.check_guess, bg="#4CAF50", fg="white")
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=self.result_font, fg="blue")
        self.result_label.pack(pady=10)
      
        self.restart_button = tk.Button(root, text="Restart Game", font=self.button_font, command=self.restart_game, bg="#2196F3", fg="white")
        self.restart_button.pack(pady=10)

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
            if user_guess < 1 or user_guess > 100:
                raise ValueError("Guess must be between 1 and 100")

            if user_guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif user_guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text="Congratulations! You guessed it!")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def restart_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")

root = tk.Tk()
app = NumberGuessingGame(root)

root.mainloop()
