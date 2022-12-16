import random
import sys
class Door:
    def __init__(self, n: int, has_car: bool = False) -> None:
        self.door_number = n
        self.has_car = has_car

class SetUp:
    def get_setup(self) -> dict:
        # getting random number to choose a
        # door with car
        n = random.randint(1, 3)
        
        doors = {}
        # creating 3 door objects
        for i in range(1, 4):
            if i == n:
                doors[i] = Door(n=i, has_car=True)

            else:
                doors[i] = Door(n=i)

        return doors

class Game:
    def get_graphics(self) -> dict:
        FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |      |  |      |
| /_/|_|  |  2   |  |  3   |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+ """

        SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|      |  |  oo  |  |      |
|  1   |  | /_/|_|  |  3   |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+
"""

        THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|      |  |      |  |  oo  |
|  1   |  |  2   |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+
"""

        FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/__|  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

        SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  | 
| /_/|_|  |  _/__|  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

        THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|  
| /_/|_|  | /_/|_|  |  _/__|
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""

        graphics_dict = {
            1: FIRST_CAR_OTHERS_GOAT,
            2: SECOND_CAR_OTHERS_GOAT,
            3: THIRD_CAR_OTHERS_GOAT,
            '1': FIRST_GOAT,
            '2': SECOND_GOAT,
            '3': THIRD_GOAT,
            }
        return graphics_dict

    def run(self):
        # getting game graphics
        graphics = self.get_graphics()

        # getting game setup
        s = SetUp()
        setup = s.get_setup()
        print("#"*5+ " MONTY HALL PROBLEM "+ "#"*5)
        print("""
+------+  +------+  +------+
|      |  |      |  |      |
|      |  |      |  |      |
|  1   |  |  2   |  |  3   |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+
""")

        while True:
            print("Choose a door (1, 2 or 3) or type 'quit' to exit.")
            response = input(">")

            if response == 'quit':
                sys.exit()

            if response in ('1', '2', '3'):
                #change input type
                chosen_door = int(response)
                break

        # decide which door to open (decision made 
        # by computer randomly)
        while True:
            # choose a random number from 1, 2, or 3
            door_to_open = random.choice((1,2,3))

            # if door to open is not chosen door
            # and if door to open doesn't have a car
            if door_to_open != chosen_door and\
                not setup[door_to_open].has_car:
                break

        # open that door
        print(graphics[str(door_to_open)])

        # the remaining door is other door
        # other_door = [x for x in range(1,4) if x not in (chosen_door, door_to_open)][0]
        other_door = [1,2,3]
        other_door.remove(chosen_door)
        other_door.remove(door_to_open)
        other_door = other_door.pop()

        while True:
            # ask to switch or stay
            print(f"Your current choice is door {chosen_door}.")
            print("Do you want to swap your choice? Press 'Y' if Yes else press 'N'.")
            response = input(">").upper()
            if response in ("Y", "N"):
                break

        if response == "Y":
            print(f"You swapped your choice to door {other_door}.")

            if setup[other_door].has_car:
                print(graphics[other_door])
                print("Congratulations You won a car")
                sys.exit()

            print(graphics[chosen_door])
            print("Sorry, You got a GOAT!")
            sys.exit()

        print(f"Your choice is still door {chosen_door}.")
        if setup[chosen_door].has_car:
            print(graphics[chosen_door])
            print("Congratulations You won a car")
            sys.exit()

        print(graphics[other_door])
        print("Sorry, You got a GOAT!")
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
