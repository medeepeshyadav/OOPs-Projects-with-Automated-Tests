# Hungry Robots
![](./images/towerofhanoi.gif)

In this small OOPs project, I have implemented a fun old school pen and paper game **BOLLYWOOD** which is basically a movie guessing game. using Object Oriented Programming and tested the functionality of the game using `pytest`.

## Project Procedure
- [Problem Description](#description)
- [Identifying the Attributes and Methods](#identify)
- [UML Diagram](#uml)
- [Documentation](#docu)
- [Testing](#testing)
    - [Testing objects and methods](#objects)

<a name = "description">
<h1> Problem Description</h1>
</a>

**BOLLYWOOD** is an old school pen & paper game we used to play as kids. It is basically a movie guessing game, where the player is given blanks to fill the letters of movie name and complete it. Each wrong guess costs one letter from the string "BOLLYWOOD". Player wins the game if he/she fills all the blanks with correct guesses and completes the name of movie. And the player looses if he/she couldn't guess the name of movie and all the letters in the string "BOLLYWOOD" are crossed out. The player is also provided with 3 different hints. The first hint fills one of letters in the name of movie in the blanks, the second hint tells the player in which year the movie was released, and the last and the most valuable hint is the name of the actor who played lead role in the movie.

<a name = "identify">
<h1>Identifying the Attributes and Methods</h1>
</a>

### 1. `SetUp` class
#### Methods:
**`get_movie()`**: Chooses a random movie from the IMDB Bollywood movie dataset. And returns a tuple of movie name and the query (a movie quiz or blanks for letters to be guessed)

### 2. `Game` class
#### Methods:
**`run()`**: Uses the SetUp class to prepare the quiz for player and runs the game.

<a name = "docu">
<h1> Documentation</h1>
</a>

### *class* `SetUp` 
A class to create an object of `SetUp` class

**Methods**:\
**get_movie()**:\
Chooses a random movie from the IMDB Bollywood movie dataset. And returns a tuple of movie name and the query (a movie quiz or blanks for letters to be guessed)

### *class* `Game` 
A class to create an object of `Game` class

**Methods**:\
**run()**:\
Uses the SetUp class to prepare the quiz for player and runs the game.

<a name = "testing">
<h1> Testing </h1>
</a>
<a name = "objects">
<h2> Testing objects and methods</h2>
</a>

Importing `pytest` and `Board` class and creating a fixture `board_obj` of `Board` class
```py
from __future__ import annotations
import pytest
from hungryrobots import Board
```

### Testing the get_movie() method of SetUp class
```py
# Testing get_movie() method of SetUp class
def test_get_movie():
    """tests the return type of get_movie() mehtod"""
    setup = SetUp()
    return_value = setup.get_movie() 
    assert isinstance(return_value, tuple)
    assert isinstance(return_value[0], str)
    assert isinstance(return_value[1], str)
```
This test function tests the return type of `get_movie()` method of `SetUp` class. The test passes if the return value of the method is `tuple` of strings.