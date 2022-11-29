# Tower of Hanoi
from __future__ import annotations
from typing import List

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
            print(f"Rod {self.rod_name}: {self}")
            return

        if disc.size >= self[-1].size:
            raise InvalidMove("\n!!!Cannot put bigger disc on smaller disc. Did you not read the rules?!!!\n")
        else:
            self.append(disc)
            print(f"Rod {self.rod_name}: {self}")
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
            raise IndexError(f"BRUHHH!! Rod {self.rod_name} is empty \(-_-)/")

if __name__=="__main__":
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


