import logging

from Enums.Choice import Choice
import random

from Enums.Creature import Creature
from Enums.EncounterResult import EncounterResult
from Tactics.Dove import Dove
from Tactics.Hawk import Hawk


class Game:
    def __init__(self, food_pairs_count, both_shared=1, both_stole=0, one_stole=3/2, one_shared=1/2):
        self.both_shared = both_shared
        self.both_stole = both_stole
        self.one_stole = one_stole
        self.one_shared = one_shared
        # No_one
        self.did_nothing = 0
        self.encountered_no_one = 2

        self.food_pairs_count = food_pairs_count

    def process_input(self, first_player_input, second_player_input) -> tuple:
        if self.doves_hawks_rules(first_player_input, second_player_input) is not None:
            return self.doves_hawks_rules(first_player_input, second_player_input)
        elif self.no_one_rules(first_player_input, second_player_input) is not None:
            return self.no_one_rules(first_player_input, second_player_input)

    def doves_hawks_rules(self, first_player_input, second_player_input) -> tuple:
        if first_player_input == Choice.share and second_player_input == Choice.share:
            return self.both_shared, self.both_shared
        elif first_player_input == Choice.steal and second_player_input == Choice.steal:
            return self.both_stole, self.both_stole
        elif first_player_input == Choice.share and second_player_input == Choice.steal:
            return self.one_shared, self.one_stole
        elif first_player_input == Choice.steal and second_player_input == Choice.share:
            return self.one_stole, self.one_shared

    def no_one_rules(self, first_player_input, second_player_input) -> tuple:
        if first_player_input == Choice.do_nothing:
            return self.did_nothing, self.encountered_no_one
        elif second_player_input == Choice.do_nothing:
            return self.encountered_no_one, self.did_nothing

    @staticmethod
    def encounter_result(food) -> EncounterResult:
        if food > 1:
            if random.random() < food - 1:
                return EncounterResult.reproduced
            else:
                return EncounterResult.survived
        elif 0 <= food < 1:
            if random.random() < food:
                return EncounterResult.survived
            else:
                return EncounterResult.starved
        elif food == 1:
            return EncounterResult.reproduced
        else:
            raise Exception("Probability cannot be less than 0")

    @staticmethod
    def creatures_to_make(encounter_result) -> int:
        if encounter_result == EncounterResult.survived:
            return 0
        elif encounter_result == EncounterResult.reproduced:
            return 1
        elif encounter_result == EncounterResult.starved:
            return -1

    def make_creature(self, num_to_make, creature_to_make):
        creatures = list()
        if num_to_make == 0:
            creatures.append(creature_to_make)
        elif num_to_make == 1:
            creatures.append(creature_to_make)
            creatures.append(self.make_similar_creature(creature_to_make))
        elif num_to_make == -1:
            pass
        return tuple(creatures)

    def new_generation(self, all_creatures_couples_points, food_pairs_count: int):
        creatures_and_points = []
        for pair in all_creatures_couples_points:
            for creature in pair:
                creatures_and_points.append(creature)

        old_creatures = []
        for creature_and_points in creatures_and_points:
            creature = creature_and_points[0]
            old_creatures.append(creature)

        new_generation_possibly = []
        for creature_and_points in creatures_and_points:
            new_generation_possibly.append(self.creature_destiny(creature_and_points))
        new_generation_possibly = self.flatten_nested_list(tuple(new_generation_possibly))

        # Now we got our old generation (old_creatures)
        # and the new one (new_generation_possibly)
        # the issue is that we only have food_pairs_count slots in our habitat
        # which means that we cannot return all creatures in new_generation_possibly
        # To solve this issue, first lets not forget to include all creatures that
        # were alife even during the previous loop
        # For that reason, lets make a list of creatures which occur in both
        # old_creatures and new_generation_possibly

        common_creatures = list(set(old_creatures) & set(new_generation_possibly))

        # now if len(common_creatures) is less than len(old_creatures) it means
        # that someone died, and we can append a new creature
        new_generation = list()
        new_generation.extend(common_creatures)
        if len(common_creatures) < len(old_creatures):
            # Since that someone surely died to a hawk
            # it makes sense to assume that the Hawk stole someone's food
            # That being said, if the hawk reproduced it means that
            # we should include him first to new_generation
            # because he was the one who made a free slot by
            # killing a dove

            # We cannot append someone who already exists in new_generation
            # And we should prioritise a hawk over doves
            new_generation_possibly_only =\
                [creature for creature in new_generation_possibly if creature not in old_creatures]
            new_generation_possibly_only.sort(key=self.sort_creatures)
            for elem in new_generation_possibly_only:
                if len(new_generation) < food_pairs_count * 2:
                    new_generation.append(elem)
            #logging.error(old_creatures)
            #logging.error(common_creatures)
            #logging.error(new_generation)
            #logging.error("-----")
            return new_generation
        return new_generation


    @staticmethod
    def sort_creatures(creature):
        if isinstance(creature, Hawk):
            return 1
        elif isinstance(creature, Dove):
            return 2
        else:
            return 3

    def creature_destiny(self, creature_and_food: tuple) -> tuple:
        creature = creature_and_food[0]
        food = creature_and_food[1]
        encounter_result = self.encounter_result(food)
        num_creatures_to_make: int = self.creatures_to_make(encounter_result)
        creatures = self.make_creature(num_creatures_to_make, creature)
        #print(f'{creature} || {num_creatures_to_make} || {creatures}')
        return creatures

    @staticmethod
    def flatten_nested_list(nested_list: tuple) -> list:
        creatures = []
        for elem in nested_list:
            if len(elem) == 1:
                creatures.append(elem[0])
            elif len(elem) == 2:
                creatures.append(elem[0])
                creatures.append(elem[1])
        return creatures

    @staticmethod
    def make_similar_creature(creature_to_compare):
        if creature_to_compare.name == Creature.hawk.value:
            return Hawk()
        elif creature_to_compare.name == Creature.dove.value:
            return Dove()
        else:
            raise Exception("????")



