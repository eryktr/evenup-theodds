from evenuptheodds.models import Player, Division
from evenuptheodds.teammaker import TeamMaker
from evenuptheodds.valuator import DivValuator


def test_teammaker_returns_optimal_solution():
    players = [
        Player("P1", Division.G2),
        Player("P2", Division.S4),
        Player("P3", Division.S3),
        Player("P4", Division.P4),
        Player("P5", Division.B1),
        Player("P6", Division.B1),
        Player("P7", Division.D2),
    ]
    valuator = DivValuator()
    teammaker = TeamMaker(players, valuator)

    teammaker.make_fair_teams()
