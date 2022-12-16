import pytest
from montyhall import Door, SetUp, Game

# testing Door class
def test_Door() -> None:
    # creating 3 door objects

    # door1: has_car not passed
    # default: False
    door1 = Door(n=1)

    # door2: has_car == False
    door2 = Door(n=2, has_car=False)
    
    # door3: has_car == True
    door3 = Door(n=3, has_car=True)

    # asserting doo1.has_car == False
    assert False == door1.has_car

    # asserting door2.has_car == False
    assert False == door2.has_car

    # asserting door3.has_car == True
    assert True == door3.has_car

# testing SetUp class
def test_SetUp() -> None:
    # instantiating a SetUp object
    s = SetUp()

    # getting setup
    setup = s.get_setup()

    # getting values in setup dict
    values = [x.has_car for x in setup.values()]

    # asserting setup is instance of dict
    assert isinstance(setup, dict)

    # asserting there are 2 doors with Goat
    assert 2 == values.count(False)

    # asserting there is only 1 door with car
    assert 1 == values.count(True)







    