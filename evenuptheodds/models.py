import enum
from typing import List
from dataclasses import dataclass


class Division(enum.Enum):
    I4 = "Iron IV"
    I3 = "Iron III"
    I2 = "Iron II"
    I1 = "Iron I"
    B4 = "Bronze IV"
    B3 = "Bronze III"
    B2 = "Bronze II"
    B1 = "Bronze I"
    S4 = "Silver IV"
    S3 = "Silver III"
    S2 = "Silver II"
    S1 = "Silver I"
    G4 = "Gold IV"
    G3 = "Gold III"
    G2 = "Gold II"
    G1 = "Gold I"
    P4 = "Plat IV"
    P3 = "Plat III"
    P2 = "Plat II"
    P1 = "Plat I"
    D4 = "Diamond IV"
    D3 = "Diamond III"
    D2 = "Diamond II"
    D1 = "Diamond I"
    M = "Master"
    GM = "Grandmaster"
    C = "Challenger"

    @classmethod
    def fromstr(cls, string: str) -> "Division":
        return cls(string)

    @classmethod
    def allowed_division_names(cls) -> List[str]:
        return [div.value for div in cls]


@dataclass(frozen=True)
class Player:
    nick: str
    division: Division
