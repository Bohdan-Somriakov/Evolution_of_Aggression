from src.Enums.Choice import Choice
from src.Tactics.Tactic import Tactic


class Hawk(Tactic):
    def __init__(self):
        super().__init__()
        self.name = Hawk.__name__

    def play(self):
        self.choice_history.append(Choice.steal)
        return Choice.steal
