import math
from collections import OrderedDict
from typing import Dict
from evenuptheodds.models import Division

# Normalized
_PLAYERS_PER_DIV = OrderedDict({
    Division.I4: 430,
    Division.I3: 1300,
    Division.I2: 2400,
    Division.I1: 3900,
    Division.B4: 5600,
    Division.B3: 4700,
    Division.B2: 5900,
    Division.B1: 7900,
    Division.S4: 10000,
    Division.S3: 9800,
    Division.S2: 9500,
    Division.S1: 7500,
    Division.G4: 8300,
    Division.G3: 5400,
    Division.G2: 4200,
    Division.G1: 3000,
    Division.P4: 2800,
    Division.P3: 1200,
    Division.P2: 1200,
    Division.P1: 1000,
    Division.D4: 1100,
    Division.D3: 440,
    Division.D2: 300,
    Division.D1: 170,
    Division.M: 17,
    Division.GM: 50,
    Division.C: 28
})


class DivValuator:
    __slots__ = "_value_map"

    _value_map: Dict[Division, int]

    def __init__(self):
        self._value_map = self._build_value_map()

    def valueof(self, div: Division) -> int:
        return self._value_map[div]

    def _build_value_map(self) -> Dict[Division, int]:
        map = {}
        sum = 0
        multiplier = 1
        precision = 10
        for key, val in _PLAYERS_PER_DIV.items():
            lg = -math.log(1 / sum) if sum else 0
            map[key] = int((pow(lg, 3) + lg * multiplier) / precision) * precision
            sum += val
            multiplier *= 1.25
        map[Division.I4] = map[Division.I3] // 2
        return map
