from evenuptheodds.const import MAX_NUM_OF_PLAYERS
from evenuptheodds.models import Division


class NoConfigFileError(Exception):
    def __init__(self):
        super().__init__("No players.cfg file found. It should reside in the root of the project.")


class InvalidPlayerDefinition(Exception):
    line: str

    def __init__(self, line: str):
        self.line = line
        super().__init__(f"Invalid player definition: {line}. Player definition should look like this: \n "
                         "PlayerName    PlayerDivision \n")


class InvalidDivisionName(Exception):
    divname: str

    def __init__(self, divname: str):
        self.divname = divname
        super().__init__(f"Invalid division name: {divname}. Allowed are: {Division.allowed_division_names()}")


class NameRepetition(Exception):
    name: str

    def __init__(self, name):
        self.name = name
        super().__init__(f"Player {name} declared multiple times.")


class TooManyPlayers(Exception):
    def __init__(self):
        super().__init__(f"The maximum allowed number of players is {MAX_NUM_OF_PLAYERS}")
