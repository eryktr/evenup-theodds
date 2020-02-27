import pytest

from evenuptheodds.models import Division

_NUM_OF_DIVISIONS = 36

@pytest.mark.parametrize("string, div", [
    ("Iron IV", Division.I4),
    ("Iron III", Division.I3),
    ("Iron II", Division.I2),
    ("Iron I", Division.I1),
    ("Bronze IV", Division.B4),
    ("Bronze III", Division.B3),
    ("Bronze II", Division.B2),
    ("Bronze I", Division.B1),
    ("Silver IV", Division.S4),
    ("Silver III", Division.S3),
    ("Silver II", Division.S2),
    ("Silver I", Division.S1),
    ("Gold IV", Division.G4),
    ("Gold III", Division.G3),
    ("Gold II", Division.G2),
    ("Gold I", Division.G1),
    ("Plat IV", Division.P4),
    ("Plat III", Division.P3),
    ("Plat II", Division.P2),
    ("Plat I", Division.P1),
    ("Diamond IV", Division.D4),
    ("Diamond III", Division.D3),
    ("Diamond II", Division.D2),
    ("Diamond I", Division.D1),
    ("Master", Division.M),
    ("Master Split 1", Division.MS1),
    ("Master Split 2", Division.MS2),
    ("Master Split 3", Division.MS3),
    ("Grandmaster", Division.G),
    ("Grandmaster Split 1", Division.GS1),
    ("Grandmaster Split 2", Division.GS2),
    ("Grandmaster Split 3", Division.GS3),
    ("Challenger", Division.C),
    ("Challenger Split 1", Division.CS1),
    ("Challenger Split 2", Division.CS2),
    ("Challenger Split 3", Division.CS3)
])
def test_division_fromstr(string, div):
    assert div == Division.fromstr(string)


def test_allowed_division_names():
    names = Division.allowed_division_names()
    assert all(div.value in names for div in Division)
