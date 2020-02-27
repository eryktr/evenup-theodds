from builtins import property
from dataclasses import dataclass
from typing import List, Tuple
from more_itertools import powerset

from evenuptheodds.models import Player, Division
from evenuptheodds.valuator import DivValuator


@dataclass
class Team:
    players: List[Player]
    value: int


@dataclass
class Solution:
    team1: Team
    team2: Team

    @property
    def skilldiff(self):
        return abs(self.team1.value - self.team2.value)


class TeamMaker:
    __slots__ = ("players", "valuator")

    players: List[Player]
    valuator: DivValuator

    def __init__(self, players: List[Player], valuator: DivValuator):
        self.players = players
        self.valuator = valuator

    def make_fair_teams(self) -> Solution:
        minimum = 20 * self.valuator.valueof(Division.C)
        optimum_solution = Solution(Team([], 0), Team([], 0))

        viable_solutions = list((set_, self._complem(set_)) for set_ in powerset(self.players) if 1 <= len(set_) <= 5)
        for players1, players2 in viable_solutions:
            val1, val2 = self._values_of_teams(players1, players2)
            diff = abs(val2 - val1)
            if diff < minimum:
                minimum = diff
                optimum_solution.team1.players = list(players1)
                optimum_solution.team2.players = list(players2)
                optimum_solution.team1.value = val1
                optimum_solution.team2.value = val2

        return optimum_solution

    def _complem(self, set_: Tuple[Player, ...]):
        return list(set(self.players) - set(set_))

    def _values_of_teams(self, players1, players2):
        return sum(self.valuator.valueof(p.division) for p in players1), sum(
            self.valuator.valueof(p.division) for p in players2)
