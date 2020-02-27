from evenuptheodds.models import Division
from evenuptheodds.valuator import DivValuator


def test_valuator_sanity_check():
    v = DivValuator()
    assert all((v.valueof(d) > 0)for d in Division)


def test_valuator_increasing_values():
    v = DivValuator()
    prev = 0
    for div in Division:
        val = v.valueof(div)
        assert v.valueof(div) >= prev
        prev = val
