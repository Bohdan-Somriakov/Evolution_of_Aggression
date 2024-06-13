from Enums.Choice import Choice
from Enums.Color import Color
from Enums.Creature import Creature
from Tactics.Hawk import Hawk
from Tactics.Dove import Dove
from Tactics.NoOne import NoOne


class Test:
    def __init__(self, game, encounters):
        self.game = game
        self.encounters = encounters
        self.hawk1 = Hawk()
        self.hawk2 = Hawk()
        self.dove1 = Dove()
        self.dove2 = Dove()
        self.no_one1 = NoOne()
        self.no_one2 = NoOne()

    def make_single_encounter(self, player1, player2):
        self.clear_all_history()
        self.make_encounters(player1, player2)
        self.print_results(player1, player2)
        self.visualise_history_points_2_players(player1, player2, self.player_color(player1), self.player_color(player2))

    def hawk_vs_dove(self):
        self.make_single_encounter(self.hawk1, self.dove1)

    def hawk_vs_hawk(self):
        self.make_single_encounter(self.hawk1, self.hawk2)

    def dove_vs_dove(self):
        self.make_single_encounter(self.dove1, self.dove1)

    def dove_vs_no_one(self):
        self.make_single_encounter(self.dove1, self.no_one1)

    def hawk_vs_no_one(self):
        self.make_single_encounter(self.hawk1, self.no_one1)

    def no_one_vs_no_one(self):
        self.make_single_encounter(self.no_one1, self.no_one2)

    def clear_all_history(self):
        self.hawk1.clear_history()
        self.hawk2.clear_history()
        self.dove1.clear_history()
        self.dove2.clear_history()
        self.no_one1.clear_history()
        self.no_one2.clear_history()

    @staticmethod
    def player_color(player):
        if player.name.casefold() == Creature.hawk.value.casefold():
            return Color.red.value
        elif player.name.casefold() == Creature.dove.value.casefold():
            return Color.blue.value
        elif player.name.casefold() == Creature.no_one.value.casefold():
            return Color.black.value

    def make_encounters(self, player1, player2):
        for elem in range(self.encounters):
            player1.receive_points(self.game.process_input(player1.play(), player2.play()))
            player2.receive_points(self.game.process_input(player2.play(), player1.play()))

    @staticmethod
    def visualise_history_points(player, color):
        player.visualise_history_points(player.__class__.__name__, color)

    @staticmethod
    def visualise_history_points_2_players(player1, player2, color1, color2):
        player1.visualise_history_points(player1.__class__.__name__, color1)
        player2.visualise_history_points(player2.__class__.__name__, color2)

    @staticmethod
    def print_results(player1, player2):
        print(player1.name + ":")
        print(player1.choice_history)
        print(player1.points_history)
        print(player2.name + ":")
        print(player2.choice_history)
        print(player2.points_history)

    @staticmethod
    def check_rules(game):
        print(game.input_process(Choice.share, Choice.share))
        print(game.input_process(Choice.steal, Choice.steal))
        print(game.input_process(Choice.share, Choice.steal))
        print(game.input_process(Choice.steal, Choice.share))