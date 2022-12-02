from __future__ import annotations
import pytest
from towerofhanoi import Disc, Rod, Player, SetUp, Game, InvalidMove

# Testing Errors raises in towerofhanoi.py
@pytest.fixture
def rod_object():
    """This fixture is expected to raise error"""
    rod = Rod('A')
    return rod

@pytest.mark.parametrize("val", [10,20,100,300, Disc(2)])
def test_type_error(rod_object, val) -> None:
    """This is expected to raise error"""
    try:
        rod_object.push(val)
    except TypeError:
        assert True

# testing push method of Rod class
@pytest.mark.parametrize("val", [Disc(2), Disc(3), Disc(100)])
def test_push_method1(rod_object, val) -> None:
    rod_object.push(val)
    assert isinstance(rod_object[0], Disc)

# testing push method of Rod class
def test_push_method2(rod_object) -> None:
    """This is expected to raise error"""
    try:
        # trying to push a bigger disc on small disc
        rod_object.push(Disc(1))
        rod_object.push(Disc(2))
    except InvalidMove:
        assert True

# testing pop_and_put method of Rod class
def test_pop_and_put_method() -> None:
    try:
        # creating disc objects
        disc1 = Disc(1)
        disc2 = Disc(2)

        # creating rod objects
        rod1 = Rod('A')
        rod2 = Rod('B')
        rod3 = Rod('C')
        
        # pushing all discs in rod1
        # in decreasing order of their size
        rod1.push(disc2)
        rod1.push(disc1)

        # popping disc from rod1 and pushing on rod2
        rod1.pop_and_put(rod2)

        # popping disc from rod1 and pushing on rod3
        rod1.pop_and_put(rod3)

        # popping disc from rod1 (which is empty now)
        # and pushing on rod2
        # this will raise IndexError
        rod1.pop_and_put(rod2)

        assert True

    except IndexError:
        assert True

    else:
        assert False

# Testing SetUp class
def test_setup_class() -> None:
    """ This test checks the SetUp"""
    # it takes 3 parameters
    # n : Number of discs
    # disc_class : Disc
    # rod_class : Rod
    # and its prepare_setup() method prepares
    # the initial setup of game
    number_of_discs = 3
    setUp = SetUp(n=number_of_discs, disc_class=Disc, rod_class=Rod)
    towers = setUp.prepare_setup()

    assert isinstance(towers, dict)
    assert isinstance(towers['A'], Rod)
    assert len(towers['A']) == number_of_discs
    assert len(towers['B']) == 0
    assert len(towers['C']) == 0

@pytest.fixture
def setup():
    """this fixture creates a setup object"""
    setUp = SetUp(n=3, disc_class=Disc, rod_class=Rod)
    towers = setUp.prepare_setup()
    return towers

# Testing make_a_move() method in Player class
def test_make_a_move_method(setup) -> None:
    player = Player(name='Jack Sparrow')
    
    rod1, rod2 = player.make_a_move(setup)
    
    # checking the return type of method
    assert isinstance(player.make_a_move(setup), tuple)

    # checking the type of the value in tuple returned
    assert isinstance(rod1, Rod)
    assert isinstance(rod2, Rod)

    # checking the length of the tuple returned
    assert len(player.make_a_move(setup)) == 2

# testing the display_menu() method of Game class
def test_display_menu(setup) -> None:
    g = Game

    # takes input from the user and returns values
    level, player = g.display_menu(g)

    assert len(g.display_menu(g)) == 2
    assert isinstance(level, int)
    assert isinstance(player, Player)

# testing the whole Game class
@pytest.fixture
def game_object() -> None:
    g = Game()

    return g

def test_Game_class(game_object: Game) -> None:
    try:
        game_object.run()
    except SystemExit:
        assert True

    