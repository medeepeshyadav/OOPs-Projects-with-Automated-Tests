import sys
import random
import settings

class Board:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def get_board(self):
        """
        Returns a dictionary that represents the board. The keys are
        (x, y) tuples of integer indexes for board positions, the values are
        WALL, EMPTY_SPACE, or DEAD_ROBOT. The dictionary also has the key
        'teleports' for the number of teleports the player has left.
        The living robots are stored separately from the board dictionary.
        """
        # defining board
        board = {'teleports': settings.NUM_TELEPORTS}
        # empty board
        for x in range(self.width):
            for y in range(self.height):
                board[(x, y)] = settings.EMPTY_SPACE

        # Creating walls around the board
        # the horizontal walls
        for x in range(self.width):
            # ceiling
            board[(x, 0)] = settings.WALL
            
            # floor
            board[(x, self.height -1)] = settings.WALL

        for y in range(self.height):
            # left wall
            board[(0, y)] = settings.WALL
            
            # right wall
            board[(self.width -1, y)] = settings.WALL

        # adding random walls
        for i in range(settings.NUM_WALLS):
            x, y = self.get_random_empty_space(board, robots=[])
            board[(x, y)] = settings.WALL

        # adding dead robots
        for i in range(settings.NUM_DEAD_ROBOTS):
            x, y = self.get_random_empty_space(board, robots=[])
            board[(x, y)] = settings.DEAD_ROBOT

        return board

    def get_random_empty_space(self, board , robots):
        """
        Return a (x, y) integer tuple of an empty 
        space on the board.
        """
        while True:
            randomX = random.randint(1, self.width - 2)
            randomY = random.randint(1, self.height - 2)

            if self.__isEmpty(randomX, randomY, robots, board):
                break
        return randomX, randomY

    
    def __isEmpty(self, x: int, y: int, robots: list, board) -> bool:
        """
        Return True if the (x, y) position is empty on the 
        board and there's also no robot there.
        """
        return (board[(x,y)] == settings.EMPTY_SPACE 
                    and (x, y) not in robots)

    def add_robots(self, board) -> list[tuple]:
        """
        Add NUM_ROBOTS number of robots to empty 
        spaces on the board and return a list of these (x, y) 
        spaces where robots are now located.
        """
        robots = []
        for _ in range(settings.NUM_ROBOTS):
            x, y = self.get_random_empty_space(board, robots)
            robots.append((x, y))

        return robots

    def display_board(self, board, robots, player_pos):
        """Display the board, robots, and player on the screen."""

        # loop over every space in the board
        for y in range(self.height):
            for x in range(self.width):
                # display the character at that pos
                if board[(x , y)] == settings.WALL:
                    print(settings.WALL, end='')

                elif board[(x , y)] == settings.DEAD_ROBOT:
                    print(settings.DEAD_ROBOT, end='')

                elif (x, y) == player_pos:
                    print(settings.PLAYER, end='')

                elif (x, y) in robots:
                    print(settings.ROBOT, end='')
                
                else:
                    print(settings.EMPTY_SPACE, end='')

            print()
    
    def make_move(self, board, robots, player_pos):
        """Takes user's input to move the player on the board"""
        playerX, playerY = player_pos
        
        moves_dict = {
            'Q': (playerX - 1, playerY - 1),
            'W': (playerX + 0, playerY - 1),
            'E': (playerX + 1, playerY - 1),
            'D': (playerX + 1, playerY + 0),
            'C': (playerX + 1, playerY + 1),
            'X': (playerX + 0, playerY + 1),
            'Z': (playerX - 1, playerY + 1),
            'A': (playerX - 1, playerY + 0),
            'S': (playerX, playerY)
        }

        # find which directions aren't blocked by robots
        q = 'Q' if self.__isEmpty(playerX-1, playerY-1, robots, board) else ' '
        w = 'W' if self.__isEmpty(playerX+0, playerY-1, robots, board) else ' '
        e = 'E' if self.__isEmpty(playerX+1, playerY-1, robots, board) else ' '
        d = 'D' if self.__isEmpty(playerX+1, playerY+0, robots, board) else ' '
        c = 'C' if self.__isEmpty(playerX+1, playerY+1, robots, board) else ' '
        x = 'X' if self.__isEmpty(playerX+0, playerY+1, robots, board) else ' '
        z = 'Z' if self.__isEmpty(playerX-1, playerY+1, robots, board) else ' '
        a = 'A' if self.__isEmpty(playerX-1, playerY+0, robots, board) else ' '

        all_moves = (q + w + e + d + c + x + z + a + 'S')

        while True:
            # get player moves
            print(f"(T)eleports remaining: {board['teleports']}")
            print(f"                   ({q})({w})({e})")
            print(f"                   ({a})(S)({d})")
            print(f"                   ({z})({x})({c})")
            print("Enter your move or (QUIT)")

            move = input('> ').upper()
            if move == 'QUIT':
                sys.exit()

            elif move == 'T':
                if board['teleports']:
                    # teleport the player to a random empty space
                    board['teleports'] -= 1
                    return self.get_random_empty_space(board, robots)
                else:
                    self.display_board(board, robots, player_pos)
                    print(settings.WARNING +'You have used up all your teleports.'+settings.ENDC)
            elif move != '' and move in  all_moves:
                # Return the new player position based on their move:
                return moves_dict[move]

    def move_robots(self, board, robot_pos, player_pos):
        """
        Return a list of (x, y) tuples of new robot positions after they
        have tried to move toward the player.
        """
        playerX, playerY = player_pos

        robot_next_pos = []

        while len(robot_pos):
            robotX, robotY = robot_pos[0]

            # where will robot move
            if robotX < playerX:
                # move right
                moveX = 1

            elif robotX > playerX:
                # move left
                moveX = -1

            elif robotX == playerX:
                # stay there
                moveX = 0

            if robotY < playerY:
                # move up
                moveY = 1

            elif robotY > playerY:
                # move down
                moveY = -1

            elif robotY == playerY:
                # stay there
                moveY = 0

            if board[robotX + moveX, robotY + moveY] == settings.WALL:
                if board[robotX + moveX, robotY] == settings.EMPTY_SPACE:
                    moveY = 0

                elif board[robotX, robotY + moveY] == settings.EMPTY_SPACE:
                    moveX = 0

                else:
                    moveX = 0
                    moveY = 0

            newRobotX = robotX + moveX
            newRobotY = robotY + moveY

            if board[robotX, robotY] == settings.DEAD_ROBOT\
                or board[newRobotX, newRobotY] == settings.DEAD_ROBOT:
                # robot is going to die here
                del robot_pos[0]

                continue
            
            # if the robot moves into another robot
            # destroy both robots
            if (newRobotX, newRobotY) in robot_next_pos:
                board[newRobotX, newRobotY] = settings.DEAD_ROBOT
                robot_next_pos.remove((newRobotX, newRobotY))

            else:
                robot_next_pos.append((newRobotX, newRobotY))

            # remove robots from the position as they move
            del robot_pos[0]

        return robot_next_pos

class Game:
    def __init__(self) -> None:
        pass

    def run(self):
        board_obj = Board(settings.WIDTH, settings.HEIGHT)
        board = board_obj.get_board()
        robots = board_obj.add_robots(board)
        player_pos = board_obj.get_random_empty_space(board, robots)
        
        while True:
            board_obj.display_board(board, robots, player_pos)

            if len(robots) == 0:
                print(settings.OKGREEN+"All the robots have crashed into each other. \n You have won!"+settings.ENDC)
                sys.exit()

            # move the player
            player_pos = board_obj.make_move(board, robots, player_pos)

            # move robots
            robots = board_obj.move_robots(board, robots, player_pos)

            for x, y in robots:
                if (x, y) == player_pos:
                    board_obj.display_board(board, robots, player_pos)
                    print(settings.FAIL+"You have been eaten by robots!"+settings.ENDC)
                    sys.exit()


if __name__ == "__main__":
    g = Game()
    g.run()

