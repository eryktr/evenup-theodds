from typing import List

from evenuptheodds.models import Division, Player
from evenuptheodds.errors import NoConfigFileError
from pathlib import Path

class ConfigParser:
    _CONFIGFILE: str = "./players.cfg"
    
    def parse(self) -> List[Player]:
        self._assert_configfile_exists()

    def _assert_configfile_exists(self):
        path = Path(self._CONFIGFILE)
        if not path.exists():
            raise NoConfigFileError
