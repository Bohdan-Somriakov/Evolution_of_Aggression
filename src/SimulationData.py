import matplotlib.pyplot as plt

from Enums.Color import Color
from Enums.Creature import Creature


class SimulationData:
    def __init__(self):
        self.hawk_count_history = []
        self.dove_count_history = []
        self.hawks_history = []
        self.doves_history = []
        self.creatures_count_history = []
        self.creatures_history = []

    def visualise_counts(self):
        self.make_plot()
        self.make_hist()
        self.make_pie_chart()
        self.make_plots()
        self.make_pies()

    def make_plot(self):
        plt.plot(self.hawk_count_history, color=Color.red.value, label="Hawks")
        plt.plot(self.dove_count_history, color=Color.blue.value, label="Doves")
        plt.xlabel("Iterations")
        plt.ylabel("Population")
        plt.legend()
        plt.title("Habitat")
        plt.savefig("results/population_simulation_graph.png")
        plt.show()

    def make_hist(self):
        figure, axis = plt.subplots(2)
        axis[0].hist(self.hawk_count_history, color=Color.red.value)
        axis[0].set_title("Hawks")
        axis[0].set_xlabel("Hawks population")
        axis[0].set_ylabel("Times population reached")

        axis[1].hist(self.dove_count_history, color=Color.blue.value)
        axis[1].set_title("Doves")
        axis[1].set_xlabel("Doves population")
        axis[1].set_ylabel("Times population reached")

        figure.suptitle("Simulation of Hawk and Dove Populations")

        plt.subplots_adjust(hspace=1)
        figure.savefig("results/population_simulation_hist.png")
        plt.show()

    def make_pie_chart(self):
        fig, ax = plt.subplots()
        sizes = list()
        sizes.append(self.dove_count_history[-1])
        sizes.append(self.hawk_count_history[-1])
        labels = list()
        labels.append(Creature.dove.value)
        labels.append(Creature.hawk.value)
        colors = list()
        colors.append(Color.blue.value)
        colors.append(Color.red.value)
        if ((self.dove_count_history[-1] != 0 and self.hawk_count_history[-1] != 0) or (self.dove_count_history[-1] != 0 and self.hawk_count_history[-1] == 0)):
            ax.pie(sizes, labels=labels, colors=colors)
            ax.set_title("On last iteration")
            fig.savefig("results/population_simulation_pie.png")
            plt.show()
        else:
            ax.pie([1], colors=[Color.black.value], radius=0.5)
            ax.text(0, 0, 'No One', ha='center', va='center', fontsize=14, color='white')
            ax.axis('equal')
            ax.set_title("On the last iteration")
            fig.savefig("results/population_simulation_pie.png")

    def make_plots(self):
        parts = 8
        divided_list_dove = self.divided_list(self.dove_count_history, parts)
        divided_list_hawk = self.divided_list(self.hawk_count_history, parts)
        plt.figure(figsize=(17, 9))
        for i in range(parts):
            plt.subplot(2, 4, i + 1)
            plt.plot(divided_list_dove[i], color=Color.blue.value, label="Doves")
            plt.plot(divided_list_hawk[i], color=Color.red.value, label="Hawks")
            plt.xlabel("Iterations")
            plt.ylabel("Population")
            plt.legend()
            plt.subplots_adjust(wspace=0.5)
        plt.savefig("results/population_simulation_plots.png")
        plt.show()

    def make_pies(self):
        parts = 8
        divided_list_dove = self.divided_list(self.dove_count_history, parts)
        divided_list_hawk = self.divided_list(self.hawk_count_history, parts)

        divided_num_dove = self.first_elements_of_lists(divided_list_dove)
        divided_num_hawk = self.first_elements_of_lists(divided_list_hawk)
        plt.figure(figsize=(17, 9))

        labels = list()
        labels.append(Creature.dove.value)
        labels.append(Creature.hawk.value)
        colors = list()
        colors.append(Color.blue.value)
        colors.append(Color.red.value)
        sizes = list()
        for i in range(parts):
            if (divided_num_dove[i] != 0 and divided_num_hawk[i] != 0) or (divided_num_dove[i] != 0 and divided_num_hawk[i] == 0):
                sizes.append(divided_num_dove[i])
                sizes.append(divided_num_hawk[i])
                plt.subplot(2, 4, i + 1)
                plt.pie(sizes, labels=labels, colors=colors)
            else:
                plt.subplot(2, 4, i + 1)
                plt.pie([1], colors=[Color.black.value], radius=0.5)
                plt.text(0, 0, 'No One', ha='center', va='center', fontsize=14, color='white')
                plt.axis('equal')
            plt.title(f"part {i}")
            sizes.clear()
        plt.savefig("results/population_simulation_pies.png")
        plt.show()

    @staticmethod
    def divided_list(list_, parts):
        part_size = len(list_) // parts
        return [list_[i * part_size: (i + 1) * part_size] for i in range(8)]

    @staticmethod
    def first_elements_of_lists(list_:list[list]):
        return [elem[0] for elem in list_]


