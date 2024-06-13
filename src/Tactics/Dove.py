from src.Enums.Choice import Choice
from src.Tactics.Tactic import Tactic


class Dove(Tactic):
    def __init__(self):
        super().__init__()
        self.name = Dove.__name__

    def play(self):
        self.choice_history.append(Choice.share)
        return Choice.share

