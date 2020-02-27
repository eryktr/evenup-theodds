import re
from typing import List, Pattern, Set

from evenuptheodds.models import Division, Player
from evenuptheodds.errors import NoConfigFileError, InvalidPlayerDefinition, InvalidDivisionName, NameRepetition
from pathlib import Path


class ConfigParser:
    _CONFIGFILE: str = "./players.cfg"
    _PLAYER_DEFINITION_PATTERN: Pattern = re.compile(r"([\w|\d|_]*)\s+([\w|\d|\s]+)")

    def parse(self) -> List[Player]:
        seen_names = set()
        path = Path(self._CONFIGFILE)
        if not path.exists():
            raise NoConfigFileError
        lines = path.read_text().split("\n")

        return [self._parse_player(line, seen_names) for line in lines]

    def _parse_player(self, line: str, seen_names: Set[str]) -> Player:
        line = line.strip()
        match = re.match(self._PLAYER_DEFINITION_PATTERN, line)

        if not match:
            raise InvalidPlayerDefinition(line)

        name = match.group(1)
        if name in seen_names:
            raise NameRepetition(name)
        seen_names.add(name)

        division_str = match.group(2)

        if division_str not in Division.allowed_division_names():
            raise InvalidDivisionName(division_str)

        division = Division.fromstr(division_str)
        return Player(name, division)
