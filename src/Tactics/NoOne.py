from src.Enums.Choice import Choice
from src.Tactics.Tactic import Tactic


class NoOne(Tactic):
    def __init__(self):
        super().__init__()
        self.name = NoOne.__name__

    def play(self):
        self.choice_history.append(Choice.steal)
        return Choice.do_nothing
