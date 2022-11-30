# Towers of Hanoi
In this project, I have turned the famous Towers of Hanoi problem into a very interactive game using Object Oriented Programming and Functional Programming. Also, tested the functionality of program with the help of `pytest` library.

## Project Procedure
- [Problem Description](#description)
- [Object Oriented Analysis (OOA)](#ooa)
    - Identifying the objects and interactions
    - Result of OOA stage
- [Object Oriented Design (OOD)](#ood)
    - High level design
    - Identifying the Attributes and Methods
    - UML Diagram
    - Result of OOD stage
- [Object Oriented Programming (OOP)](#oop)
    - Documentation
    - Examples

<a name = "description">
<h1> Problem Description</h1>
</a>

Towers of Hanoi is a mathematical puzzle where we are given three rods (**A**, **B**, and **C**) and **N** of disks. Initially, all the discs are stacked in their decreasing size such that, the largest disc is at the bottom of rod and the smallest disc is at the top.

The objective of the puzzle is to move the entire stack of disc from rod **A** to rod **C** using rod **B** as auxiliary rod, obeying the following simple rules:
- Only one disc can be moved at a time.
- Each move consists of taking the upper disk from one of the rods and placing it on top of another rod i.e. a disc can only be moved if it is the uppermost disc on a stack.
- No disc may be placed on top of a smaller disc.

![](./images/Towers-Of-Hanoi-768x576.png)

*Figure. Towers of Hanoi*

<a name = "ooa">
<h1> Object Oriented Analysis (OOA)</h1>
</a>
Now that we are familiar with the problem, let's analyse the problem and look it from the Object Oriented point of view. This stage is known as Object Oriented Analysis (OOA). We just simply see the problem and identify the objects and the interface of the problem.

### Identifying the objects
The problem has two objects:
- Rods
- Discs

The problem has the following interface:
- Discs are put on Rods.
- Discs are removed from Rods.
- Small disc cannot be put on large disc.
- Goal is to stack all the discs on Rod 'C' in correct order.

### Result of the OOA stage
From the OOA stage we have got the description of the system that needs to be built. We determined that we need two type of objects, Rods and Discs. And we also determined the behaviors on the objects, and which object activate a certain behavior on what object.

<a name = "ood">
<h1> Object Oriented Design (OOD)</h1>
</a>
In the OOA stage, we came up with the high level description of the system we are required to build. Now, let's use that description and transform it into requirements for our program.

### High level design
With the above description of the system, our high level design looks like this:
![](./images/high_level_design.png)

Since, there are tree **Rods** and N number of **Discs**, we are required to make two classes. Class **Rod** and class **Disc**. The above UML diagram shows that the object of class Disc is pushed to an object of class Rod.
The '*' beside the Disc class and '1' beside the Rod class tells that, **many** object of Disc class can be pushed to **one** object of Rod class, respectively.

Now, let's move further and see what kind of attributes and methods we can define on these classes.

### Identifying the Attributes and Methods
#### Attributes:
**`size`**: The class `Disc` can have a `size` attribute since, all the discs are of different size.

**`rod_name`**: The class `Rod` can have a `rod_name` attribute to identify which rod it is. 

**`disc`**: Also class `Rod` can have a `disc` attribute which is the object of `Disc` type to be pushed into the rod.

#### Methods:
**`push()`**: Since, we are required to push discs in the rods, the `Rod` class can have a `push()` which takes a object of type `Disc` and push it to the rod. This method is only activated by an object of `Disc` type on the rod.

**`pop_and_put()`**: Also, we are required to move disc from one rod to another rod. For that, we can have another method `pop_and_put()` in the `Rod` class to pop the disc from given rod and push it to another Rod type object. It takes an object of `Rod` type as an argument to which we want to push.

### The updated UML diagram
Now, our UML diagram looks like this:

![](./images/attributes_and_methods.png)

### Result of OOD stage
As a result of OOD stage, we discovered: what classes we need to implement for our system. We also discovered the associated attributes and methods for the respective classes. We now have the requirements for our Object Oriented Programming stage. We can now implement these classes in any Object Oriented language, we will use Python.

<a name = "oop">
<h1> Object Oriented Programming (OOP)</h1>
</a>

## Documentation
### *class* `Disc(size: int)` 
A class to construct an object of `Disc` type.

**Parameters:**\
**size**: ***int type***\
            It represents the size of the disc object.


### *class* `Rod(name: str, disc: Disc = None)`
The **`Rod`** class extends the buit-in `List` class.

**Parameters:**\
**name**: ***str type***\
            It represents the name of the rod object.

**disc**: ***object of Disc type***\
The disc which will be pushed into the given rod object.

**Methods:**\
**push()**: ***arguments: object of Disc type***\
Takes an object of type `Disc` and push it to the object of `Rod` class. This method is only activated by an object of `Disc` type on the rod.

**pop_and_put()**: ***arguments: object of Rod type***\
Pops the disc from *`self`* and push it to given `Rod` type object.


### Exceptions
#### `TypeError`
This exception is raised when a parameter is passed in the `Rod` class which is not of type `Disc`.

#### `InvalidMove`
This is a custom exception class, which is raised when the user tries to push the small disc on top of large disc in the rod.

#### `IndexError`
This exception is raised when the user tries to pop from a rod object which is empty.

\#Note: Later we use these exceptions in our user interface to show warning messages to the user.

## Examples:
Pushing disc in a rod.
```py
# instantiating object of Disc
# setting size parameter as 1
d1 = Disc(size=1)

# instantiating object of Rod
# setting name parameter as 'A'
rod1 = Rod(name='A')

# pushing d1 in rod1
rod1.push(d1)
```
**Output**
```
 Rod A: [1]
```

Popping disc from rod and putting on other rod.
```py
# instantiating two Disc objects
d1 = Disc(size=1)
d2 = Disc(size=2)

# instantiating two Rod objects
rod1 = Rod(name='A')
rod2 = Rod(name='B')

# pushing d2 in rod1
rod1.push(d2)
# pushing d2 in rod1
rod1.push(d1)

# popping from rod1 and putting on rod2
rod1.pop_and_put(rod2)
```
**Output**
```
Rod A: [2]
Rod A: [2, 1]
Rod B: [1]
Disc 1 popped from rod A and pushed on rod B.
```










