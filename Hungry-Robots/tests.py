from __future__ import annotations
import pytest
from hungryrobots import Board

@pytest.fixture
def board_obj():
    board_obj = Board(40, 40)
    return board_obj

# testing get_board() method of Board class
def test_get_board(board_obj : Board):
    """tests the return type of get_board() mehtod"""
    return_value = board_obj.get_board()
    assert isinstance(return_value, dict)

def test_add_robots(board_obj: Board):
    """ tests the return type of add_robots() method"""
    board = board_obj.get_board()
    return_value = board_obj.add_robots(board)
    assert isinstance(return_value, list)
    assert isinstance(return_value[0], tuple)

def test_make_move(board_obj: Board):
    """ tests the return type of make_move() method"""
    board = board_obj.get_board()
    robots_pos = board_obj.add_robots(board)
    player_pos = board_obj.get_random_empty_space(board, robots_pos)
    try:
        return_value = board_obj.make_move(board, robots_pos, player_pos)
        assert isinstance(return_value, tuple)
    except SystemExit:
        assert True

def test_move_robots(board_obj: Board):
    """ tests the return type of move_robots() method"""
    board = board_obj.get_board()
    robots_pos = board_obj.add_robots(board)
    player_pos = board_obj.get_random_empty_space(board, robots_pos)
    return_value = board_obj.move_robots(board, robots_pos, player_pos)
    
    assert isinstance(return_value, list)
    assert isinstance(return_value[0], tuple)