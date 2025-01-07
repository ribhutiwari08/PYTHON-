import tkinter as tk
from tkinter import messagebox

class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Adventure Game")

        self.text = tk.StringVar()
        self.text.set("Welcome to the Adventure Game!\nYou are in a dark forest. There is a path leading north and another to the east.\nWhat will you do?")
        
        self.label = tk.Label(root, textvariable=self.text, height=10, width=50, anchor="w", justify="left", padx=10, pady=10)
        self.label.pack()

        self.button1 = tk.Button(root, text="Go north", command=self.north_path)
        self.button1.pack(side="left", padx=10)

        self.button2 = tk.Button(root, text="Go east", command=self.east_path)
        self.button2.pack(side="left", padx=10)

    def update_text(self, new_text):
        self.text.set(new_text)
        
    def north_path(self):
        self.update_text("You head north and arrive at a river.\nThere is a boat nearby, but it looks old and unstable.\nWhat will you do?\n1. Cross the river\n2. Turn back")
        self.button1.config(text="Cross the river", command=self.cross_river)
        self.button2.config(text="Turn back", command=self.turn_back)

    def east_path(self):
        self.update_text("You head east and encounter a wild bear!\nWhat will you do?\n1. Fight the bear\n2. Run away")
        self.button1.config(text="Fight the bear", command=self.fight_bear)
        self.button2.config(text="Run away", command=self.run_away)

    def cross_river(self):
        self.update_text("The boat sinks halfway across, and you fall into the river. You drown.\nGame Over!")
        self.button1.config(state="disabled")
        self.button2.config(state="disabled")
        self.play_again()

    def turn_back(self):
        self.update_text("You turn back and return to the starting point.")
        self.reset_game()

    def fight_bear(self):
        self.update_text("You bravely fight the bear, but it's too strong. You lose the fight.\nGame Over!")
        self.button1.config(state="disabled")
        self.button2.config(state="disabled")
        self.play_again()

    def run_away(self):
        self.update_text("You run away safely back to the starting point.")
        self.reset_game()

    def reset_game(self):
        self.button1.config(state="normal")
        self.button2.config(state="normal")
        self.button1.config(text="Go north", command=self.north_path)
        self.button2.config(text="Go east", command=self.east_path)
        self.update_text("Welcome to the Adventure Game!\nYou are in a dark forest. There is a path leading north and another to the east.\nWhat will you do?")

    def play_again(self):
        result = messagebox.askyesno("Game Over", "Do you want to play again?")
        if result:
            self.reset_game()
        else:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()
