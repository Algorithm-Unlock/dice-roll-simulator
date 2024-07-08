import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk

class DiceRollSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dice Roll Simulator")
        self.geometry("300x300")
        self.configure(bg="#f5f5f5")

        # Dice images
        self.dice_images = [
            ImageTk.PhotoImage(Image.open(f"images\\dice{i}.png")) for i in range(1, 7)
        ]

        # Dice Label
        self.dice_label = tk.Label(self, image=self.dice_images[0], bg="#f5f5f5")
        self.dice_label.pack(pady=20)

        # Roll Button
        self.roll_button = ttk.Button(self, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(self, text="Click the button to roll the dice!", bg="#f5f5f5", font=("Helvetica", 12))
        self.result_label.pack(pady=20)

    def roll_dice(self):
        result = random.randint(1, 6)
        self.dice_label.config(image=self.dice_images[result - 1])
        self.result_label.config(text=f"You rolled a {result}!")

if __name__ == "__main__":
    app = DiceRollSimulator()
    app.mainloop()