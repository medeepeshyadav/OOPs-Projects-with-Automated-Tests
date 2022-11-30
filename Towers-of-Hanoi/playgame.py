import sys
from towerofhanoi import Disc, Rod

def main():
    print("#"*55 + " TOWER OF HANOI "+ "#"*55)
    print(" "*45 + "#"*15 + " RULES "+ "#"*15)
    print("""You are required to move all the discs from rod A to rod C. But there are certain rules you must follow.\n
1. You can only move one disc from one rod at a time.\n
2. You cannot put big disc on top of a small disc.\n
3. Ofcourse, you cannot remove disc from an empty rod!\n
4. You only win if you successfully move all the discs on rod C.\n
5. Type 'QUIT' and press Return, if its hard for you.\n""")

    print("###### MENU ######")
    print("Enter the level from (3 to 5).")
    level = int(input('> '))

    # display initial moves
    displayInitialMoves(level)

    while level not in range(3, 5+1):        
        print('Please enter level in the given range only.')
        level = int(input('> '))

        # display initial moves
        displayInitialMoves(level)
        
    # prepare initial setup based on the level
    towers = initial_setup(level)

    moves = 0

    while True: # run a single turn
        # Display towers and discs
        displayRods(towers, level)

        # Ask player to make a move
        from_rod, to_rod = askForMove(towers)

        # move the disk from rod X to rod Y
        try:
            from_rod.pop_and_put(to_rod)
            moves += 1
            displayMoves(towers, level, moves)

        except Exception as e:
            print(e)
        

        # check if player solved the puzzle
        if len(towers['C']) == level:
            displayRods(towers, level) # Display towers for one last time.
            print(r"Congratulations! You solved the puzzle .'.\(^_^)'/.!")
            sys.exit()

def initial_setup(level):
    """ Forms initial setup of game"""
    rod1 = Rod('A')
    rod2 = Rod('B')
    rod3 = Rod('C')
    for i in range(level, 0, -1):
        rod1.append(Disc(i))
        
    return {'A': rod1, 'B': rod2, 'C': rod3}

def askForMove(towers):
    """ Ask the Player for move"""

    while True: # Keep Asking player until a Valid move.

        # ask the user for move
        print("Enter the letters of 'from' and 'to' rod or 'QUIT'.")
        print('(e.g. AB to moves a disk from rod A to rod B.)')
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print("Thanks for playing!")
            sys.exit()

        # make sure the user entered valid tower letters
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue

        # store the responses in variables.
        from_rod, to_rod = response[0], response[1]

        # return the "from_rod" and "to_rod".
        return (towers[from_rod], towers[to_rod])

# USER INTERFACE
def displayRods(rods, total_discs):
    """Display the current state"""
    
    # Display the three towers
    for l in range(total_discs, -1, -1):
        for rod in (rods['A'], rods['B'], rods['C'] ):
            if l >= len(rod):
                displayDiscs(0, total_discs) # Bare rod with no discs.

            else:
                displayDiscs(rod[l].size, total_discs) # display the discs.

        print()

    # display tower labels A, B, C.
    emptiness = ' '*(total_discs)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptiness))

def displayDiscs(width, total_discs):
    """ Display discs of the given width. A width 0 means no disc"""
    emptiness = ' '*(total_discs - width)

    if width == 0:
        # display a bare rod
        print(emptiness + '||' + emptiness, end='')

    else:
        # display the discs
        disc = '#'*width
        numLabel = str(width).rjust(2, '_')
        print(emptiness + disc + numLabel + disc + emptiness, end='')

def displayInitialMoves(level):
    if level == 3:
        print("\nYou have 7 moves to finish this puzzle.\n")
        print("Moves Left: 7/7")

    elif level == 4:
        print("\nYou have 15 moves to finish this puzzle.\n")
        print("Moves Left: 15/15")

    elif level == 5:
        print("\nYou have 31 moves to finish this puzzle.\n")
        print("Moves Left: 31/31")
    
    else:
        # we can add more here
        pass

def displayMoves(towers, level, move_counter):
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
    if 0 < move_counter < max_moves:
        # display moves left
        print(f"Moves Left: {max_moves - move_counter}/{max_moves}")

    # if moves left is 0 and rod C has
    # all the discs
    elif len(towers['C']) == level:
        # display moves left for one last time
        print(f"Moves Left: {max_moves - move_counter}/{max_moves}")

    # if moves left is 0 and rod C still
    # doesn't have all the discs
    else:
        # display moves left
        print(f"Moves Left: {max_moves - move_counter}/{max_moves}")

        # display rods for one last time
        displayRods(towers, level)

        # show game over message
        print("Game Over, You ran out of moves!\n")
        sys.exit()

if __name__ == "__main__":
    main()