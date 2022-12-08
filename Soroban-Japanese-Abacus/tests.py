import pytest
from soroban import Rod, Abacus

@pytest.fixture
def rod() -> Rod:
    rod = Rod('u')
    return rod

# Testing Rod class
def test_Rod_class() -> None:
    # creating a Qth rod of abacus
    # moving up beads at Qth place
    # adds billion in each move
    rodQ = Rod('q')
    rodQ.move_beads_up()

    # creating a Pth rod of abacus
    # moving up beads at Pth place
    # adds 1 in each move
    rodP = Rod('p')
    rodP.move_beads_up()

    assert isinstance(rodQ, Rod)
    assert isinstance(rodP, Rod)
    assert 1_000_000_000 == rodQ.earth*rodQ.mapping[rodQ.name]
    assert 1 == rodP.earth*rodP.mapping[rodP.name]

def test_move_beads_up() -> None:
    # creating a Qth rod of abacus
    # moving up beads at Qth place
    # adds billion in each move
    rodQ = Rod('q')
    # moving 4 beads up
    rodQ.move_beads_up()
    rodQ.move_beads_up()
    rodQ.move_beads_up()
    result_for_Q = rodQ.move_beads_up()

    # creating a Pth rod of abacus
    # moving up beads at Pth place
    # adds 1 in each move
    rodP = Rod('p')
    # moving 5 beads up
    # this will activate the
    # the heaven bead
    # and reset the earth beads
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()
    result_for_P = rodP.move_beads_up()

    # asserting moving 4 beads up on Qth rod will result in 4 billion
    assert 4_000_000_000 == result_for_Q

    # asserting moving 5 beads up on rod will activate Heaven bead
    assert rodP.heaven == 1
    # asserting moving 5 beads up on rod will reset Earth beads
    assert rodP.earth == 0

    # asserting moving 5 beads up on rod will activate Heaven bead and
    # result in 5
    assert 5 == result_for_P

def test_move_beads_down() -> None:
    # creating a Pth rod of abacus
    # moving up beads at Pth place
    # adds 1 in each move
    rodP = Rod('p')
    # moving 5 beads up
    # will result in 5
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()

    # moving 1 bead down on rod P
    # will deativate the Heaven bead
    # and Earth beads will be 4

    # result will be 4
    result_for_P = rodP.move_beads_down()

    # asserting moving 1 bead down on rod will deactivate Heaven bead
    assert rodP.heaven == 0

    # asserting moving 1 bead down on rod will reset Earth beads to 4
    assert rodP.earth == 4

    # asserting moving 1 beads up on rod will deativate Heaven bead and
    # result in 4
    assert 4 == result_for_P

# testing Abacus class
def test_get_char_list(rod:Rod) -> None:
    a = Abacus()

    # moving 3 beads up on rod object
    rod.move_beads_up()
    rod.move_beads_up()
    rod.move_beads_up()
    char_list =  a.get_char_list(rod)

    # asserting the char_list is instance of list type
    assert isinstance(char_list, list)

    # asserting the char_list will look like this
    assert [['0','|','|','0','0','0'],['|','0']] == char_list


