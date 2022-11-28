import pytest
from towerofhanoi import Disc, Rod, InvalidMove

# Testing Errors raises
@pytest.fixture
def rod_object():
    """This fixture is expected to raise error"""
    rod = Rod('A')
    return rod

def test_type_error(rod_object) -> None:
    try:
        rod_object.push(200)
        assert False
    except TypeError as t:
        assert True

def test_push_method(rod_object) -> None:
    try:
        rod_object.push(Disc(1))
        rod_object.push(Disc(2))
        assert False
    except InvalidMove:
        assert True

def test_pop_and_put_method() -> None:
    try:
        disc1 = Disc(1)
        disc2 = Disc(2)
        rod1 = Rod('A')
        rod2 = Rod('B')
        rod3 = Rod('C')
        
        rod1.push(disc2)
        rod1.push(disc1)

        rod1.pop_and_put(rod2)
        rod1.pop_and_put(rod3)
        rod1.pop_and_put(rod2)

        assert True

    except IndexError:
        assert False

def test_program() -> None:
    try:
        d1 = Disc(1)
        d2 = Disc(2)
        d3 = Disc(3)
        d4 = Disc(4)

        rod1 = Rod(name='A')
        rod2 = Rod(name='B')
        rod3 = Rod(name='C')

        rod1.push(d4)
        rod1.push(d3)
        rod1.push(d2)
        rod1.push(d1)

        rod1.pop_and_put(rod2)
        rod1.pop_and_put(rod3)
        rod2.pop_and_put(rod3)
        rod1.pop_and_put(rod2)
        rod3.pop_and_put(rod2)
        rod3.pop_and_put(rod1)
        rod2.pop_and_put(rod1)
        rod2.pop_and_put(rod3)
        rod1.pop_and_put(rod2)
        rod1.pop_and_put(rod3)
        rod2.pop_and_put(rod3)
        rod1.pop_and_put(rod2)
        rod3.pop_and_put(rod1)
        rod3.pop_and_put(rod2)
        rod1.pop_and_put(rod2)
        rod3.pop_and_put(rod1)
        rod2.pop_and_put(rod1)
        rod2.pop_and_put(rod3)
        rod1.pop_and_put(rod3)
        rod3.pop_and_put(rod2)
        rod3.pop_and_put(rod1)
        rod2.pop_and_put(rod1)
        rod2.pop_and_put(rod3)
        rod1.pop_and_put(rod3)
        rod1.pop_and_put(rod2)
        rod3.pop_and_put(rod2)
        rod1.pop_and_put(rod3)
        rod2.pop_and_put(rod1)
        rod2.pop_and_put(rod3)
        rod1.pop_and_put(rod3)

        assert not(rod1)
        assert not(rod2)
        assert rod3

    except (TypeError, InvalidMove, IndexError) as e:
        print(e)
        assert False
