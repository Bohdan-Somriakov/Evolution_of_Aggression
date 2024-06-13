from time import sleep

import matplotlib.pyplot as plt


class Tactic:
    def __init__(self):
        self.points_history_both = []
        self.points_history = []
        self.choice_history = []

    def play(self):
        print("Make choice")

    def receive_points(self, points: tuple):
        self.points_history_both.append(points)
        self.points_history.append(points[0])

    def clear_history(self):
        self.points_history_both = []
        self.points_history = []
        self.choice_history = []

    def visualise_history_points(self, name, color: str):
        plt.plot(self.points_history, color=color)
        plt.xlabel("Encounters")
        plt.ylabel("Points received")
        plt.title(name)
        plt.show()
