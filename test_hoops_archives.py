# IN PROCESS

from hoops_archives import get_leading_scorer, check_team
import pytest

def test_check_team():
    assert check_team("Golden State Warriors") == 1610612744
    assert check_team("Harvard University Team") == None


def test_get_leading_scorer():
    assert get_leading_scorer(1610612744) == ("Stephen Curry", 23668)
    assert get_leading_scorer("Real Madrid") == None
