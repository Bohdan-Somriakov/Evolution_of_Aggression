import random

from Enums.Creature import Creature
from SimulationData import SimulationData
from Tactics.Dove import Dove
from Tactics.Hawk import Hawk
from Tactics.NoOne import NoOne
from Tactics.Tactic import Tactic


class Habitat:
    def __init__(self, initial_hawk_count, initial_dove_count, game):
        self.game = game
        self.food_pairs_count = self.game.food_pairs_count
        self.hawk_count = initial_hawk_count
        self.dove_count = initial_dove_count
        self.hawks = self.make_hawks()
        self.doves = self.make_doves()
        self.creatures_count = self.combine_counts()
        self.creatures = self.combine_creatures()
        self.creatures_couples = None
        self.all_creatures_couples_points = None
        self.simulation_data = SimulationData()

    def pick_random_creature(self) -> Tactic:
        rand_int = 0
        picked_creature = self.creatures[rand_int]
        while isinstance(picked_creature, NoOne):
            rand_int = random.randint(0, len(self.creatures)-1)
            picked_creature = self.creatures[rand_int]
            no_creatures = all(isinstance(creature, NoOne) for creature in self.creatures)
            if no_creatures:
                rand_int = 0
                picked_creature = self.creatures[rand_int]
                break
        self.creatures.pop(rand_int)
        return picked_creature

    def try_pick_no_one(self):
        for creature in self.creatures:
            if isinstance(creature, NoOne):
                return creature

    def sum_encounter_results(self) -> list:
        all_creatures_couples_points = []
        for i in range(len(self.creatures_couples)):
            plr1 = self.creatures_couples[i][0]
            plr2 = self.creatures_couples[i][1]
            plr1_input = plr1.play()
            plr2_input = plr2.play()
            creatures_couples_points = \
                (
                    (plr1, self.game.process_input(plr1_input, plr2_input)[0]),
                    (plr2, self.game.process_input(plr2_input, plr1_input)[0])
                )
            all_creatures_couples_points.append(creatures_couples_points)
        return all_creatures_couples_points

    def simulation_data_gather(self):
        self.simulation_data.doves_history.append(self.doves)
        self.simulation_data.hawks_history.append(self.hawks)
        self.simulation_data.dove_count_history.append(self.dove_count)
        self.simulation_data.hawk_count_history.append(self.hawk_count)
        self.simulation_data.creatures_history.extend(self.creatures)
        self.simulation_data.creatures_count_history.append(self.creatures_count)

    def simulate(self, iterations):
        self.simulation_data_gather()
        for elem in range(iterations):
            self.make_encounters()
            self.simulation_data_gather()
        self.simulation_data.visualise_counts()

    def make_encounters(self):
        self.fill_empty_space()
        random.shuffle(self.creatures)
        self.creatures_couples = self.make_couples()
        self.all_creatures_couples_points = self.sum_encounter_results()
        self.clear_habitat()
        self.creatures = self.process_all_encounters()
        self.refill_data()

    def refill_data(self):
        if self.creatures is None:
            self.hawks = []
            self.doves = []
            self.creatures = []
            self.hawk_count = 0
            self.dove_count = 0
            self.creatures_count = 0
        else:
            self.hawks = [creature for creature in self.creatures if creature.name == Creature.hawk.value]
            self.doves = [creature for creature in self.creatures if creature.name == Creature.dove.value]
            self.creatures = self.doves + self.hawks
            self.hawk_count = len(self.hawks)
            self.dove_count = len(self.doves)
            self.creatures_count = self.hawk_count + self.dove_count
            self.creatures_couples = None  # Still None

    def display(self):
        print(f"hawks: {self.hawks}")
        print(f"doves: {self.doves}")
        print(f"hawk_count: {self.hawk_count}")
        print(f"dove_count: {self.dove_count}")
        print(f"creatures_count: {self.creatures_count}")
        print(f"creatures_couples: {self.creatures_couples}")

    def process_all_encounters(self) -> list:
        return self.game.new_generation(self.all_creatures_couples_points, self.food_pairs_count)

    def make_couples(self) -> list:
        creatures_couples = []
        food_pairs_available = self.food_pairs_count
        while food_pairs_available >= 1 and self.creatures_count >= 1:
            player1 = self.pick_random_creature()  # Not no one if possible
            player2 = self.try_pick_no_one() or self.pick_random_creature()
            food_pairs_available -= 1
            creatures_couples.append((player1, player2))
        return creatures_couples

    def clear_habitat(self):
        self.hawk_count = 0
        self.dove_count = 0
        self.hawks = []
        self.doves = []
        self.creatures_count = 0
        self.creatures = []
        self.creatures_couples = None

    def make_doves(self) -> list:
        return self.make_creatures(Creature.dove.value)

    def make_hawks(self) -> list:
        return self.make_creatures(Creature.hawk.value)

    def make_creatures(self, creature_type: str):
        creatures = []
        count = self.count_creature(creature_type)
        for elem in range(count):
            new_creature = self.make_new_creature(creature_type)
            creatures.append(new_creature)
        return creatures

    def combine_counts(self):
        return self.hawk_count + self.dove_count

    def combine_creatures(self):
        return self.hawks + self.doves

    def fill_empty_space(self):
        filled_slots = self.creatures_count
        food_count = self.food_pairs_count * 2
        while filled_slots < food_count:
            filled_slots += 1
            self.creatures.append(NoOne())

    def count_creature(self, creature_type: str):
        if creature_type == Creature.hawk.value:
            return self.hawk_count
        elif creature_type == Creature.dove.value:
            return self.dove_count

    @staticmethod
    def make_new_creature(creature_type: str):
        if creature_type == Creature.hawk.value:
            return Hawk()
        elif creature_type == Creature.dove.value:
            return Dove()
