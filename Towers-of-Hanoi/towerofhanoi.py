# Tower of Hanoi
from __future__ import annotations
import sys
from typing import List, Type

## error classes
class InvalidMove(ValueError):
    pass

class Disc:
    """
    Class for disc object 
    :attr size: disc size
    :method __repr__: returns string representation of object
    """
    def __init__(self, size: int) -> None:
        if not isinstance(size, int):
            raise TypeError("Size must be 'int' type.")
        self.size = size

    def __repr__(self) -> str:
        return (f"{self.size}")

class Rod(List[int]):
    """
    Class for rod object
    :attr name: name of rod (str)
    :attr disc: object of type Disc
    :method push: pushes a disc on rod
    :method pop_and_put: put disc from one rod to another
    """
    def __init__(
        self,
        name: str, 
        disc: Disc = None
        ) -> None:
        self.disc = disc
        self.rod_name = name

    def __repr__(self) -> str:
        """ returns a string representation of Rod object """
        return (f"{list(self)}")

    def push(self, disc: Disc) -> str:
        """
        a method to push disc on rod
        :param disc: object of type Disc
        """
        if not isinstance(disc, Disc):
            raise TypeError(f"Disc type object expected, got {type(disc).__name__} type.")
            
        elif not self:
            self.append(disc)
            # this code displays the rod as list
            # print(f"Rod {self.rod_name}: {self}")
            return

        if disc.size >= self[-1].size:
            raise InvalidMove("\n!!!Cannot put bigger disc on smaller disc. Did you not read the rules?!!!\n")
        else:
            self.append(disc)
            # this code displays the rod as list
            # print(f"Rod {self.rod_name}: {self}")
            return

    def pop_and_put(self, rod: Rod) -> str:
        """
        This method pops a disc from one rod
        and puts it on the another rod
        :param rod: rod to which the popped disc is put
        :return: str representation of Rod object
        """
        if self:
            popped = self.pop()
            try:
                rod.push(popped)
                print(f"Disc {popped.size} "
                    f"popped from rod {self.rod_name} "
                    f"and pushed on rod {rod.rod_name}.")

            except InvalidMove as e:
                self.append(popped)
                raise e
            
            return self
        else:
            raise IndexError(f"BRUHHH!! Rod {self.rod_name} is empty \\(-_-)/")

class SetUp:
    def __init__(
        self,
        n:int,
        disc_class: Type[Disc],
        rod_class: Type[Rod],
        ) -> None:

        self.rod1 = rod_class('A')
        self.rod2 = rod_class('B')
        self.rod3 = rod_class('C')

        # fill the rod 'A' with all the discs
        for i in range(n, 0, -1):
            self.rod1.push(disc_class(i))

    def prepare_setup(self) -> dict[str: Rod[Disc]]:
        return {'A': self.rod1, 'B': self.rod2, 'C': self.rod3}

class Game:
    def __init__(self) -> None:
        self.moves = 0

    def display_menu(self) -> tuple[int, Player]:
        print("#"*55 + " TOWER OF HANOI "+ "#"*55)
        print(" "*45 + "#"*15 + " RULES "+ "#"*15)
        print("""You are required to move all the discs from rod A to rod C. But there are certain rules you must follow.\n
    1. You can only move one disc from one rod at a time.\n
    2. You cannot put big disc on top of a small disc.\n
    3. Ofcourse, you cannot remove disc from an empty rod!\n
    4. You only win if you successfully move all the discs on rod C.\n
    5. Type 'QUIT' and press Return, if its hard for you.\n""")

        player_name = input('Please enter your name:')
        print("\n")
        player = Player(name=player_name)

        print("###### MENU ######")
        print("""Enter the no. of discs (3 to 5).
        Difficulty level:
        3 discs = Easy
        4 discs = Medium
        5 discs = Hard
        """)
        level = int(input('> '))

        # if the player did not input the
        # valid disc numbers, Ask again.
        while level not in range(3, 5+1):
            print('Please enter the no. of discs\
                 from the given range only.')
            level = int(input('> '))

        return level, player

    def display_initial_moves(
        self, 
        level: int, 
        player_name: str
        ) -> None:
        """ 
        Displays the number of max moves
        to solve the puzzle.        
        """
        if level == 3:
            print(f"\n{player_name}, you have 7 moves to finish this puzzle.\n")
            print("Moves Left: 7/7")

        elif level == 4:
            print(f"\n{player_name}, you have 15 moves to finish this puzzle.\n")
            print("Moves Left: 15/15")

        elif level == 5:
            print(f"\n{player_name}, you have 31 moves to finish this puzzle.\n")
            print("Moves Left: 31/31")
        
        else:
            # we can add more here
            pass

    def display_moves(
        self, 
        level: int, 
        towers: dict[str,Rod[Disc]]
        ) -> None:
        """Displays moves"""
        # if level is 3
        if level == 3:
            # max moves are 7
            max_moves = 7

        # if level is 4
        elif level == 4:
            # max moves are 15
            max_moves = 15

        # if level is 5
        elif level == 5:
            # maxmoves are 31
            max_moves = 31
        
        else:
            # we can add more here
            pass
        
        # if move counter between 0 and max moves
        if 0 < self.moves < max_moves:
            # display moves left
            print(f"Moves Left: {max_moves - self.moves}/{max_moves}")

        # if moves left is 0 and rod C has
        # all the discs
        elif len(towers['C']) == level:
            # display moves left for one last time
            print(f"Moves Left: {max_moves - self.moves}/{max_moves}")

        # if moves left is 0 and rod C still
        # doesn't have all the discs
        else:
            # display moves left
            print(f"Moves Left: {max_moves - self.moves}/{max_moves}")

            # display rods for one last time
            self.display_rods(level, towers)

            # show game over message
            print("Game Over, You ran out of moves!\n")
            sys.exit()

    def display_rods(
        self, 
        level: int, 
        rods: dict[str,Rod[Disc]]
        ) -> None:
        """Display the current state"""

        # Display the three towers
        for l in range(level, -1, -1):
            for rod in (rods['A'], rods['B'], rods['C']):
                if l >= len(rod):
                    # Bare rod with no discs.
                    self.display_discs(0, level) 

                else:
                    # display the discs.
                    self.display_discs(rod[l].size, level) 

            print()

        # display tower labels A, B, C.
        emptiness = ' '*(level)
        print("{0} A{0}{0} B{0}{0} C\n".format(emptiness))

    def display_discs(self, width: int, level: int) -> None:
        """ 
        Display discs of the given width. A width 0 means no disc
        """
        emptiness = ' '*(level - width)

        if width == 0:
            # display a bare rod
            print(
                emptiness + 
                '||' + 
                emptiness, 
                end='')

        else:
            # display the discs
            disc = '#'*width
            numLabel = str(width).rjust(2, '_')
            print(
                emptiness + 
                disc + 
                numLabel + 
                disc + 
                emptiness, 
                end='')

    def run(self):
        """ Runs the game """
        # get the user inputs
        level, player = self.display_menu()

        # get the setup for game
        setup = SetUp(level, Disc, Rod)
        towers = setup.prepare_setup()

        # display initial moves to solve the puzzle
        self.display_initial_moves(
            level, 
            player.name
            )

        # show UI
        while True:
            # display rods
            self.display_rods(level, towers)
            
            # get user input
            from_rod, to_rod = player.make_a_move(towers)

            try:
                from_rod.pop_and_put(to_rod)
                self.moves += 1
                self.display_moves(
                    level=level,
                    towers=towers
                )

            except Exception as e:
                print(e)

            # check if player solved the puzzle
            if len(towers['C']) == level:
                # Display towers for one last time.
                self.display_rods(level, towers)
                print(f"Congratulations, {player.name}! You solved the puzzle .'.\\(^_^)'/.!")
                sys.exit()

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def make_a_move(
        self,
        towers: dict[str,Rod[Disc]]
        ) -> tuple[Rod]:
        """ Ask the Player for move"""
        while True: # Keep Asking player until a Valid move.

            # ask the user for move
            print("Enter the letters of 'from' and 'to' rod or 'QUIT'.")
            print('(e.g. AB to moves a disk from rod A to rod B.)')
            response = input('> ').upper().strip()

            if response == 'QUIT':
                print(f"Thanks for playing!, {self.name}.")
                sys.exit()

            # make sure the user entered valid tower letters
            if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
                print('Enter one of AB, AC, BA, BC, CA, or CB.')
                continue

            # store the responses in variables.
            from_rod, to_rod = response[0], response[1]

            # return the "from_rod" and "to_rod".
            return (towers[from_rod], towers[to_rod])

if __name__=="__main__":
    game = Game()
    game.run()


