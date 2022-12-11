# Prime Numbers Generator
In this OOP project, I have implemented various primality test algorithms like, Old School method, Fermat Method, Sieve of Eratosthenes, Sieve of Sundaram and Miller Rabin primality test, to generate prime numbers. And also tested the program with the help of `pytest` library.

## Project Procedure
- [Problem Description](#description)
    - Primality Test Algorithms
- [Object Oriented Design (OOD)](#ood)
    - UML Diagram
- [Object Oriented Programming (OOP)](#oop)
    - Documentation
    - Examples
- [Testing](#testing)
    - Testing Rod class
    - Testing Abacus Class

- [Demonstration](#demo)
- [Things that I learnt from this Project](#lessons)

<a name = "description">
<h1> Problem Description</h1>
</a>

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Examples of the first few prime numbers are {2, 3, 5, …}. There is no algorithm to predict a prime number, the numbers are tested one at a time if they are prime or not using some primality test algorithms, such as:
- School Method
- Fermat Method
- Sieve of Eratosthenes
- Sieve of Sundaram
- Millar Rabin Primality Test

### Primality Test Algorithms
1. **School Method**: It is the most simple solution, we iterate through all the numbers from 2 to n-1 and for every number we check if it divides n. If we find any number that divides, we return `False` meaning the number failed the primality test. Instead of checking till `n`, we can check till `√n` because a larger factor of `n` must be a multiple of a smaller factor that has been already checked.

Time Complexity: O(√n)

2. **Fermat Method**: It is a probabilistic method, it tests if a number is probably a prime or a composite number. For prime number it will always return `True` but for composite number it may return either `True` or `False`, hence, this method is not very accurate. However, if we increase the iterations for test `k` the algorithm gets more accurate. 

Algorithm:
1)  Repeat following k times:\
    a) Pick a randomly in the range [2, n - 2]\
    b) If gcd(a, n) ≠ 1, then return False\
    c) If an-1 &nequiv; 1 (mod n), then return False\
2) Return True [probably prime].\

Where, Higher value of k indicates, probability of correct results for composite inputs become higher and henve,  prime inputs result is more correct.

3. **Sieve of Eratosthenes**: The Sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than `n` when `n` is smaller than 10 million or so.

Algorithm:
1) We create a list of all numbers from 2 to n. Let `n = 10` for simplicity.
    [2, 3, 4, 5, 6, 7, 8, 9, 10]

Then, we repeat the following steps until the square of current element is smaller than the input `n`.

2) n = 10, current element = 2, Since, 2*2 < 10 we remove all the numbers that are multiples of 2, except itself.
    [2, 3, 5, 7, 9]

3) n = 10, current element = 3, Since, 3*3 < 10 we remove all the number that are multiples of 3, except itself.
    [2, 3, 5, 7]

4) n = 10, current element = 5, Since, 5*5 > 10 we stop here, and the elements in the list are the prime numbers less than 10.
    Answer: [2, 3, 5, 7]

4. **Sieve of Sundaram**: Sieve of Sundaram is more efficient method than Sieve of Eratosthenes method. It allows us to find the prime numbers smaller than 1 Billion.

Algorithms:
1) In general Sieve of Sundaram, produces primes smaller than 
   (2*x + 2) for a number given number x. Since we want primes 
   smaller than n, we reduce n to half. We call it nNew.
       nNew = n//2

   For example, if n = 102, then nNew = 50.
                if n = 103, then nNew = 51

2) Create an array `marked[n]` that is going\
   to be used to separate numbers of the form (i + j + 2ij) from\
   others where  (1 <= i <= j)\

3) Initialize all entries of `marked[]` as 0 (False).\

4) // Mark all numbers of the form (i + j + 2ij) as 1 (True)\
   // where (1 <= i <= j)\
   Loop for i=1 to nNew\
        a) j = i\
        b) Loop while (i + j + 2*i*j),  if 2 then append 2 as first prime.\

6) Remaining primes are of the form (2i + 1) where i is index of `NOT marked` numbers. So print (2i + 1) for all i such that marked[i] is 0 (False).\

5. **Miller Rabin Primality Test**: This algorithm, is more advanced form of Fermat Method of primality test. It is based on the same Fermat's Little Theorem. It return False for composite prime and True for prime numbers.

Algorithm:
k is an input parameter that determines accuracy level. Higher value of k indicates more accuracy.

A function to check if a number is prime or not:
isPrime(n : int, k: int) -> bool
1) Handle base cases for n < 3\
2) If n is even, return False.\
3) Find an odd number d such that `n-1` can be written as `d*2r`.\
   Note that since `n` is odd, `(n-1)` must be even and `r` must be\
   greater than 0.\
4) Do following k times\
     if (millerTest(n, d) == False)\
          return False\
5) Return True.\

This function is called for all k trials. It returns `False` if n is composite and returns `True` if n is probably prime. `d` is an odd number such that `d*2r = n-1` for some `r >= 1`.\
bool millerTest(int n, int d)
1) Pick a random number 'a' in range `[2, n-2]`
2) Compute: x = a^d % n
3) If x == 1 or x == n-1, return True.

4) Do following while d doesn't become `n-1`.
     a) x = (x*x) % n.
     b) If (x == 1) return False.
     c) If (x == n-1) return True. 

<a name = "ood">
<h1> Object Oriented Design (OOD)</h1>
</a>

In this project we are going to implement a class for each of the primality test algorithms mentioned above. Each class will consist of a `get_primes()` method and a `isPrime()` method. `get_primes()` method uses the algorithm defined in `isPrime()` method to check if a number is prime or not and return a list of prime numbers smaller than a given number.

## Identifying the Attributes and Methods
### 1. `SchoolMethod` class
#### Methods:
**`get_primes()`**: This method returns the list of all prime numbers smaller than the given number with the help of `isPrime()` method.

**`isPrime()`**: This method defines the algorithm we are using for testing if the number is prime or not. In case of `SchoolMethod` class we will define School Method of primality test in this method.

### 2. `FermatMethod` class
#### Attributes:
**`k`**: It is the number of iterations to run the Fermat Test on a number. Greater the `k` more will be the accuracy.

#### Methods:
**`get_primes()`**: This method returns the list of all prime numbers smaller than the given number with the help of `isPrime()` method.

**`isPrime()`**: This method defines the algorithm we are using for testing if the number is prime or not. In case of `FermatMethod` class we will define Fermat Method of primality test in this method.

### 3. `SieveOfEratosthenes` class
#### Methods:
**`get_primes()`**: This method returns the list of all prime numbers smaller than the given number using Sieve of Eratosthenes algorithm.

### 4. `SieveOfSundaram` class
#### Methods:
**`get_primes()`**: This method returns the list of all prime numbers smaller than the given number using Sieve of Sundaram algorithm.

### 5. `MillerRabin` class
#### Attributes:
**`k`**: It is the number of iterations to run the Fermat Test on a number. Greater the `k` more will be the accuracy.

#### Methods:
**`get_primes()`**: This method returns the list of all prime numbers smaller than the given number with the help of `isPrime()` method.

**`isPrime()`**: This method will run the `miller_test()` method for `k` iterations for a given number.

**`miller_test()`**: This method consists of the definition of Miller Rabin primality test algorithm.

### The UML diagram
Now, our UML diagram looks like this:

![](./images/attributes_and_methods.png)

### Result of OOD stage
As a result of OOD stage, we discovered; What classes we need to implement for our system. We also discovered the associated attributes and methods for the respective classes. We now have the requirements for our Object Oriented Programming stage. We can now implement these classes in any Object Oriented language, we will use Python.

<a name = "oop">
<h1> Object Oriented Programming (OOP)</h1>
</a>

## Documentation
### *class* `Rod` 
A class to construct an object of `Rod` type.

**Parameters:**\
**name**: ***str type***\
It represents the name of the `Rod` object.

**Methods:**\
**move_beads_up()**:\
Moves the bead up on the given rod object.

**move_beads_down()**:\
Moves the bead down on the given rod object.

### *class* `Abacus`
This class is a composite class which is composed of 10 `Rod` objects to form an abacus. 

**Methods:**\
**input()**: ***command: str type***\
 Takes a `command` argument which is `str` type. Each character in the command is the name of the rod on which the bead is moved. It returns the value of the rod after moving the bead.

**get_char_list()**: ***rod: Rod type object***\
Takes a rod type object, and creates a list of characters ('0' representing a bead and '|' representing no bead) to display the abacus on user's screen.

**run()**:\
Runs the whole program.

<a name = "testing">
<h1> Testing </h1>
</a>

For testing our program I have used **`pytest`** library. 
### Testing Rod class and its methods
#### Testing Rod class objects
```py
import pytest
from soroban import Rod, Abacus

# Testing Rod class
def test_Rod_class() -> None:
    # creating a Qth rod of abacus
    # moving up beads at Qth place
    # adds billion in each move
    rodQ = Rod('q')
    result_rod_Q = rodQ.move_beads_up()

    # creating a Pth rod of abacus
    # moving up beads at Pth place
    # adds 1 in each move
    rodP = Rod('p')
    result_rod_P = rodP.move_beads_up()

    assert isinstance(rodQ, Rod)
    assert isinstance(rodP, Rod)
    assert 1_000_000_000 == result_rod_Q
    assert 1 == result_rod_P
```
In the above test code, we create two objects `rodQ` and `rodP`of `Rod` class and do the following tests:
- We check if the rod object is the instance of `Rod` class.
- We check if we move one bead on `rodQ` the value at that rod will be 1 Billion.
- We also check if we move one bead on `rodP` the value at that rod will be 1.

#### Testing move_beads_up() method of Rod class
```py
def test_move_beads_up() -> None:
    # creating a Qth rod of abacus
    # moving up beads at Qth place
    # adds billion in each move
    rodQ = Rod('q')
    # moving 4 beads up
    rodQ.move_beads_up()
    rodQ.move_beads_up()
    rodQ.move_beads_up()
    result_for_Q = rodQ.move_beads_up()

    # creating a Pth rod of abacus
    # moving up beads at Pth place
    # adds 1 in each move
    rodP = Rod('p')
    # moving 5 beads up
    # this will activate the
    # the heaven bead
    # and reset the earth beads
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()
    result_for_P = rodP.move_beads_up()

    # asserting moving 4 beads up on Qth rod will result in 4 billion
    assert 4_000_000_000 == result_for_Q

    # asserting moving 5 beads up on rod will activate Heaven bead
    assert rodP.heaven == 1
    # asserting moving 5 beads up on rod will reset Earth beads
    assert rodP.earth == 0

    # asserting moving 5 beads up on rod will activate Heaven bead and
    # result in 5
    assert 5 == result_for_P
```
The above code will test:
- When we move 4 beads up on `rodQ` the value at that rod will be 4 Billion
- Calling `move_beads_up()` method 5 times will activate the `heaven` bead and reset the `earth` row beads.
- The value after activating heaven bead on `rodP`, the value at `rodP` will be equal to 5. 

#### Testing move_beads_down() method of Rod class
```py
def test_move_beads_down() -> None:
    # creating a Pth rod of abacus
    # moving up beads at Pth place
    # adds 1 in each move
    rodP = Rod('p')
    # moving 5 beads up
    # will result in 5
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()
    rodP.move_beads_up()

    # moving 1 bead down on rod P
    # will deativate the Heaven bead
    # and Earth beads will be 4

    # result will be 4
    result_for_P = rodP.move_beads_down()

    # asserting moving 1 bead down on rod will deactivate Heaven bead
    assert rodP.heaven == 0

    # asserting moving 1 bead down on rod will reset Earth beads to 4
    assert rodP.earth == 4

    # asserting moving 1 beads up on rod will deativate Heaven bead and
    # result in 4
    assert 4 == result_for_P
```
The above code we move 5 beads up on `rodP` and then we call `move_beads_down()` method to move 1 bead down on `rodP`. We test the following things:
- Moving 1 bead down on `rodP` will reset the heaven bead and make it 0
- Value on earth row is equal to 4
- The value at the rod is equal to 4.

### Testing Abacus class
#### Testing the get_char_list() method of Abacus class.
```py
# testing Abacus class
def test_get_char_list(rod:Rod) -> None:
    a = Abacus()

    # moving 3 beads up on rod object
    rod.move_beads_up()
    rod.move_beads_up()
    rod.move_beads_up()
    char_list =  a.get_char_list(rod)

    # asserting the char_list is instance of list type
    assert isinstance(char_list, list)

    # asserting the char_list will look like this
    assert [['0','|','|','0','0','0'],['|','0']] == char_list
```
In the above code we are testing the `get_char_list()` method. We check if the return type of the `get_char_list()` is of `list` type. We also check what kind list we will get after moving 3 beads up on the `rod`(rod at 'u' position).

<a name='demo'>
<h1> Demonstration </h1>
</a>
Given below are some of the snapshots of the final output of the progam.

#### The initial state of the Abacus
The first snapshot shows the, title of the program. Then the abacus itself and some controls to move beads up and down.

![](./images/soroban1.png)


#### The state after we input a command of up/down characters
In the snapshot given below, we have given the command "uoppp", which moves up 1 bead on thousands' place, 1 bead on tens' place and 3 beads on ones' place. And the result of the command is `Total: 1013`. 

![](./images/soroban2.png)


#### Activation of heaven bead
After giving the last input (i.e., "uoppp") if we give "ppp" as our new command to the abacus, it will activate the heaven bead and the value on ones' place will be equal to 6, and hence, the total will be equal to `Total: 1016`.

![](./images/soroban3.png)

<a name = 'lessons'>
<h1> Things that I learnt from this project</h1>
</a>

I have acquired the following skills from this project:
- **Object Oriented Designing**: I have learnt how to approach an OOPs project as a step-by-step procedure, by first analysing the problem at hand from object oriented point of view, finding the objects and the relations between those objects.

- **UML Diagrams**: I have learnt how to draw the basic UML diagrams before jumping into programming step. UML diagrams do really makes implementation easy, when we sit and write the code for the Object Oriented Programming project.

- **Using `dict` for mapping objects**: In this project I have used python dictionaries for mapping objects with the input commands.

- **Unit Testing with `pytest` library**: The most valuable skill I have learnt is unit testing using `pytest` library. Testing my code pointed out a few loopholes in my code which I fixed and ensured that my code is free of bugs.