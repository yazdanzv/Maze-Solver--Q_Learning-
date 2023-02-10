from tkinter import *

N = 10
M = 10

# COLORS

RED = "#FF4433"
AQUAMARINE = "#7FFFD4"
BLACK = "#000000"
NAVY = "#251D3A"

# Fonts

MONTSERRAT = ("Montserrat", 22, "")


class GUI:
    def __init__(self, policy_table):
        self.policy_table = policy_table
        self.window = Tk()
        self.window.title("Policy Table")
        self.window.geometry("370x500")
        self.window.config(padx=20, pady=20, bg=NAVY)
        self.labels = []
        self.label_builder()
        self.give_positions()
        self.window.mainloop()

    def label_builder(self):
        for i in range(M * N):
            if i <= 9:
                state = f'0{i}'
            else:
                state = str(i)
            if self.policy_table[state] == 'B':
                self.labels.append(Label(text="B", bg=RED, fg=BLACK, font=MONTSERRAT))
            else:
                self.labels.append(Label(text=self.policy_table[state], bg=AQUAMARINE, fg=BLACK, font=MONTSERRAT))

    def give_positions(self):
        for row in range(N):
            for column in range(M):
                index = row * 10 + column
                self.labels[index].grid(column=column, row=row, padx=2, pady=2)

