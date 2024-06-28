import tkinter as tk

from Enums.Color import Color
from Game import Game
from Habitat import Habitat


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulation of aggression")
        self.font = ("Helvetica", 16)
        self.btn_txt = "input"

        self.init_widgets()

    def init_widgets(self):
        self.init_food_widgets()
        self.init_creature_widgets()
        self.init_initial_counts_widgets()
        self.init_simulation_widgets()
        self.init_buttons()

    def init_food_widgets(self):
        self.food_pairs_count_lbl = tk.Label(self.root, text="Food pairs:", font=self.font)
        self.food_pairs_count_entry = tk.Entry(self.root, font=self.font, width=6)
        self.food_pairs_count_btn = tk.Button(self.root, text=self.btn_txt,
                                              font=self.font, command=self.food_pairs_count_get_entry)
        self.food_pairs_count = None

    def init_creature_widgets(self):
        self.dove_dove_entry = tk.Entry(font=self.font, width=3)
        self.dove_hawk_entry = tk.Entry(font=self.font, width=3)
        self.hawk_hawk_entry = tk.Entry(font=self.font, width=3)
        self.hawk_dove_entry = tk.Entry(font=self.font, width=3)
        self.dove_dove_entry.insert(0, '1')
        self.dove_hawk_entry.insert(0, '1/2')
        self.hawk_hawk_entry.insert(0, '0')
        self.hawk_dove_entry.insert(0, '3/2')

        self.dove1_lbl = tk.Label(text="Dove", font=self.font, fg=Color.blue.value)
        self.dove2_lbl = tk.Label(text="Dove", font=self.font, fg=Color.blue.value)
        self.hawk1_lbl = tk.Label(text="Hawk", font=self.font, fg=Color.red.value)
        self.hawk2_lbl = tk.Label(text="Hawk", font=self.font, fg=Color.red.value)

        self.rules_creatures_btn = tk.Button(self.root, text=self.btn_txt,
                                              font=self.font, command=self.rules_creatures_get_entries)

    def init_initial_counts_widgets(self):
        self.initial_dove_count_lbl = tk.Label(text="Initial dove count:", font=self.font, fg=Color.blue.value)
        self.initial_hawk_count_lbl = tk.Label(text="Initial hawk count:", font=self.font, fg=Color.red.value)
        self.initial_dove_count_entry = tk.Entry(font=self.font, width=5)
        self.initial_hawk_count_entry = tk.Entry(font=self.font, width=5)
        self.initial_counts_btn = tk.Button(self.root, text=self.btn_txt,
                                            font=self.font, command=self.initial_counts)
        self.initial_dove_count = None
        self.initial_hawk_count = None

    def init_simulation_widgets(self):
        self.simulate_num_lbl = tk.Label(self.root, text="Iterations to run:", font=self.font)
        self.simulate_num_entry = tk.Entry(self.root, font=self.font, width=8)
        self.simulate_num_btn = tk.Button(self.root, text=self.btn_txt,
                                          font=self.font, command=self.simulate_num_method)
        self.simulate_num = None

    def init_buttons(self):
        self.run_simulation_btn = tk.Button(self.root, font=self.font, text="Run simulation",
                                            command=self.run_simulation)

        self.input_all_btn = tk.Button(self.root, font=self.font, text="input all",
                                       command=self.input_all_method)

    def place_food_pairs_widgets(self):
        self.food_pairs_count_lbl.grid(row=0, column=0)
        self.food_pairs_count_entry.grid(row=0, column=1)
        self.food_pairs_count_btn.grid(row=1, column=1)

    def place_creatures_widgets(self):
        self.dove1_lbl.grid(row=2, column=1)
        self.dove2_lbl.grid(row=3, column=0)
        self.hawk1_lbl.grid(row=2, column=2)
        self.hawk2_lbl.grid(row=4, column=0)

        self.dove_dove_entry.grid(row=3, column=1)
        self.dove_hawk_entry.grid(row=3, column=2)
        self.hawk_dove_entry.grid(row=4, column=1)
        self.hawk_hawk_entry.grid(row=4, column=2)

        self.rules_creatures_btn.grid(row=5, column=1)

    def place_initial_counts_widgets(self):
        self.initial_dove_count_lbl.grid(row=6, column=0)
        self.initial_hawk_count_lbl.grid(row=7, column=0)
        self.initial_dove_count_entry.grid(row=6, column=1)
        self.initial_hawk_count_entry.grid(row=7, column=1)
        self.initial_counts_btn.grid(row=8, column=1)

    def place_simulation_widgets(self):
        self.simulate_num_lbl.grid(row=9, column=0)
        self.simulate_num_entry.grid(row=9, column=1)
        self.simulate_num_btn.grid(row=10, column=1)
        self.input_all_btn.grid(row=11, column=1)
        self.run_simulation_btn.grid(row=12, column=1)

    def unpack(self):
        self.place_food_pairs_widgets()
        self.place_creatures_widgets()
        self.place_initial_counts_widgets()
        self.place_simulation_widgets()

    def food_pairs_count_get_entry(self):
        self.food_pairs_count = self.food_pairs_count_entry.get()

    def rules_creatures_get_entries(self):
        self.dove_dove_result = self.dove_dove_entry.get()
        self.dove_hawk_result = self.dove_hawk_entry.get()
        self.hawk_hawk_result = self.hawk_hawk_entry.get()
        self.hawk_dove_result = self.hawk_dove_entry.get()

    def initial_counts(self):
        self.initial_dove_count = self.initial_dove_count_entry.get()
        self.initial_hawk_count = self.initial_hawk_count_entry.get()

    def simulate_num_method(self):
        self.simulate_num = self.simulate_num_entry.get()

    def input_all_method(self):
        self.simulate_num_method()
        self.initial_counts()
        self.rules_creatures_get_entries()
        self.food_pairs_count_get_entry()

    def run_simulation(self):
        game1 = Game(int(self.food_pairs_count), eval(self.dove_dove_result),
                     eval(self.hawk_hawk_result), eval(self.hawk_dove_result), eval(self.dove_hawk_result))
        habitat1 = Habitat(int(self.initial_hawk_count), int(self.initial_dove_count), game1)
        habitat1.simulate(int(self.simulate_num))
