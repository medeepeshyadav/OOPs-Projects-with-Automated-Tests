# Soroban Japanese Abacus
from __future__ import annotations
import typing

class Rod:
    def __init__(self, name: str):
        self.name = name
        self.earth = 0
        self.heaven = 0
        self.mapping = {
                    'p': 10**0,
                    'o': 10**1,
                    'i': 10**2,
                    'u': 10**3,
                    'y': 10**4,
                    't': 10**5,
                    'r': 10**6,
                    'e': 10**7,
                    'w': 10**8,
                    'q': 10**9,
                }

    def move_beads_up(self) -> int:
        """
        Moves up the beads in abacus
        """
        if self.earth != 4:
            self.earth += 1

        elif self.earth != 4 or self.heaven != 1:
            self.earth = 0
            self.heaven += 1

        else:
            self.earth = 0
            self.heaven = 0
            return 0
        res = (self.earth*self.mapping[self.name]
                + self.heaven*self.mapping[self.name]*5)

        return res

    def move_beads_down(self) -> int:
        """
        Moves down the beads in abacus
        """
        if self.earth != 0:
            self.earth -= 1

        elif self.earth != 0 or self.heaven != 0:
            self.earth = 4
            self.heaven -= 1

        else:
            self.earth = 0
            self.heaven = 0
            return 0

        res = (self.earth*self.mapping[self.name] 
                + self.heaven*self.mapping[self.name]*5)

        return res

class Abacus:
    def __init__(self) -> None:
        self.rodP = Rod(name='p')
        self.rodO = Rod(name='o')
        self.rodI = Rod(name='i')
        self.rodU = Rod(name='u')
        self.rodY = Rod(name='y')
        self.rodT = Rod(name='t')
        self.rodR = Rod(name='r')
        self.rodE = Rod(name='e')
        self.rodW = Rod(name='w')
        self.rodQ = Rod(name='q')

        self.rods = {
            'p': self.rodP,
            'o': self.rodO,
            'i': self.rodI,
            'u': self.rodU,
            'y': self.rodY,
            't': self.rodT,
            'r': self.rodR,
            'e': self.rodE,
            'w': self.rodW,
            'q': self.rodQ,
        }

        self.vals = {
            'p': 0,
            'o': 0,
            'i': 0,
            'u': 0,
            'y': 0,
            't': 0,
            'r': 0,
            'e': 0,
            'w': 0,
            'q': 0,
        }

    def input(self, command: str) -> int:
        """ takes a string input of rod names
            returns total
        """
        decrement_commands = {
            ';':'p',
            'l':'o',
            'k':'i',
            'j':'u',
            'h':'y',
            'g':'t',
            'f':'r',
            'd':'e',
            's':'w',
            'a':'q',
        }

        for c in command:
            # If a character in command is in 
            # 'qwertyuiop' then move a bead up
            if c in 'qwertyuiop':
                self.vals[c] = self.rods[c].move_beads_up()
            
            # If a character in command is in 
            # 'asdfghjkl' then move a bead down
            elif c in 'asdfghjkl;':
                c = decrement_commands[c]
                self.vals[c] = self.rods[c].move_beads_down()

        # return the sun of all the values
        return sum(self.vals.values())

    def get_char_list(self, rod: Rod) -> list:
        """
        This method designs each column for abacus
        :param rod: object of Rod class
        :rtype: list
        """
        # initial character list
        char_list = [['0','0','0','0','|','|'],['|','0']]

        # get earth value and heaven value
        earth, heaven = rod.earth, rod.heaven
        
        # if earth is not zero
        if earth:
            # update the character list
            for _ in range(earth):
                char_list[0].insert(5, char_list[0].pop(4-earth))

        # if heaven is not zero
        if heaven:
            # update the character list
            char_list[1].insert(1,char_list[1].pop(1-heaven))

        # return the character list
        return char_list

    def display_abacus(self):
        """Displays the whole abacus on the screen"""
        print("+=====================+")

        # 1st heaven row
        print("I"+" {} {} {} {} {} {} {} {} {} {}".format(
        self.get_char_list(self.rodQ)[1][1], 
        self.get_char_list(self.rodW)[1][1],
        self.get_char_list(self.rodE)[1][1],
        self.get_char_list(self.rodR)[1][1],
        self.get_char_list(self.rodT)[1][1],
        self.get_char_list(self.rodY)[1][1],
        self.get_char_list(self.rodU)[1][1],
        self.get_char_list(self.rodI)[1][1],
        self.get_char_list(self.rodO)[1][1],
        self.get_char_list(self.rodP)[1][1])+" I")

        # 2nd heaven row
        print("I"+" {} {} {} {} {} {} {} {} {} {}".format(
        self.get_char_list(self.rodQ)[1][0], 
        self.get_char_list(self.rodW)[1][0],
        self.get_char_list(self.rodE)[1][0],
        self.get_char_list(self.rodR)[1][0],
        self.get_char_list(self.rodT)[1][0],
        self.get_char_list(self.rodY)[1][0],
        self.get_char_list(self.rodU)[1][0],
        self.get_char_list(self.rodI)[1][0],
        self.get_char_list(self.rodO)[1][0],
        self.get_char_list(self.rodP)[1][0])+" I")

        print("+=====================+")

        # 1st earth row
        print("I"+" {} {} {} {} {} {} {} {} {} {}".format(
        self.get_char_list(self.rodQ)[0][5], 
        self.get_char_list(self.rodW)[0][5],
        self.get_char_list(self.rodE)[0][5],
        self.get_char_list(self.rodR)[0][5],
        self.get_char_list(self.rodT)[0][5],
        self.get_char_list(self.rodY)[0][5],
        self.get_char_list(self.rodU)[0][5],
        self.get_char_list(self.rodI)[0][5],
        self.get_char_list(self.rodO)[0][5],
        self.get_char_list(self.rodP)[0][5])+" I")

        # 2nd earth row
        print("I"+" {} {} {} {} {} {} {} {} {} {}".format(
        self.get_char_list(self.rodQ)[0][4], 
        self.get_char_list(self.rodW)[0][4],
        self.get_char_list(self.rodE)[0][4],
        self.get_char_list(self.rodR)[0][4],
        self.get_char_list(self.rodT)[0][4],
        self.get_char_list(self.rodY)[0][4],
        self.get_char_list(self.rodU)[0][4],
        self.get_char_list(self.rodI)[0][4],
        self.get_char_list(self.rodO)[0][4],
        self.get_char_list(self.rodP)[0][4])+" I")

        # 3rd earth row
        print("I"+" {} {} {} {} {} {} {} {} {} {}".format(
        self.get_char_list(self.rodQ)[0][3], 
        self.get_char_list(self.rodW)[0][3],
        self.get_char_list(self.rodE)[0][3],
        self.get_char_list(self.rodR)[0][3],
        self.get_char_list(self.rodT)[0][3],
        self.get_char_list(self.rodY)[0][3],
        self.get_char_list(self.rodU)[0][3],
        self.get_char_list(self.rodI)[0][3],
        self.get_char_list(self.rodO)[0][3],
        self.get_char_list(self.rodP)[0][3])+" I")

        # 4th earth row
        print("I"+" {} {} {} {} {} {} {} {} {} {}".format(
        self.get_char_list(self.rodQ)[0][2], 
        self.get_char_list(self.rodW)[0][2],
        self.get_char_list(self.rodE)[0][2],
        self.get_char_list(self.rodR)[0][2],
        self.get_char_list(self.rodT)[0][2],
        self.get_char_list(self.rodY)[0][2],
        self.get_char_list(self.rodU)[0][2],
        self.get_char_list(self.rodI)[0][2],
        self.get_char_list(self.rodO)[0][2],
        self.get_char_list(self.rodP)[0][2])+" I")

        # 5th earth row
        print("I"+" {} {} {} {} {} {} {} {} {} {}".format(
        self.get_char_list(self.rodQ)[0][1], 
        self.get_char_list(self.rodW)[0][1],
        self.get_char_list(self.rodE)[0][1],
        self.get_char_list(self.rodR)[0][1],
        self.get_char_list(self.rodT)[0][1],
        self.get_char_list(self.rodY)[0][1],
        self.get_char_list(self.rodU)[0][1],
        self.get_char_list(self.rodI)[0][1],
        self.get_char_list(self.rodO)[0][1],
        self.get_char_list(self.rodP)[0][1])+" I")

        # 6th earth row
        print("I"+" {} {} {} {} {} {} {} {} {} {}".format(
        self.get_char_list(self.rodQ)[0][0], 
        self.get_char_list(self.rodW)[0][0],
        self.get_char_list(self.rodE)[0][0],
        self.get_char_list(self.rodR)[0][0],
        self.get_char_list(self.rodT)[0][0],
        self.get_char_list(self.rodY)[0][0],
        self.get_char_list(self.rodU)[0][0],
        self.get_char_list(self.rodI)[0][0],
        self.get_char_list(self.rodO)[0][0],
        self.get_char_list(self.rodP)[0][0])+" I")

        # last row to display numbers
        # in respective columns
        print("+={}={}={}={}={}={}={}={}={}={}=+".format(
            self.vals['q']//(10**9),
            self.vals['w']//(10**8),
            self.vals['e']//(10**7),
            self.vals['r']//(10**6),
            self.vals['t']//(10**5),
            self.vals['y']//(10**4),
            self.vals['u']//(10**3),
            self.vals['i']//(10**2),
            self.vals['o']//(10**1),
            self.vals['p']//(10**0),
            ))

        # Controls/Instructions
        print(' +q w e r t y u i o p')
        print(' -a s d f g h j k l ;')
        print('(Enter a stream of up/down letters or "quit" to stop.)')

    def run(self):
        """
        a method to run the abacus
        """
        print("SOROBAN JAPANESE ABACUS")
        while True:
            self.display_abacus()
            command = input('>')
            if command == 'quit':
                break
            print("TOTAL: ", self.input(command))
        


if __name__ == "__main__":
    a = Abacus()
    a.run()
