'''There is a well-known puzzle involving a 3-liter jar and a 5-liter jar.
We can do 3 things with each jar:

* Fill the jar: the jar is completely filled with water.

* Empty the jar: the jar is emptied completely and contains no water.

* Pour into the other jar: water is poured from jar A into jar B until either:
(1) jar A runs out of water and is empty;
or (2) jar B becomes full, and jar A contains any leftover water.
Notice that no water is lost while pouring, and we are not allowed to pour "halfway"
-- we must pour until either the source jar is empty or the destination jar is full
(whichever happens first).

The goal is to end up with exactly 4 liters of water in the 5-liter jar.

Write a new Python class called $\verb#Jar#$ to simulate a jar from this puzzle.
You should write a constructor method to create a new empty jar
(where the capacity of the jar is passed as a parameter), a string conversion method
to return the status of a jar (for example, "a 3-liter jar with 2 liters of water"),
and a method for each of the three operations listed above.

Then, write a program that creates two empty jars of sizes 3-liters and 5-liters,
and perform the necessary operations to result in the 5-liter jar containing exactly 4 liters of water.
'''

class Jar :

    def __init__(self, jar_size) :
        self.size = jar_size
        self.amount = 0

    def __str__(self) :
        answer = "a "
        answer += str(self.size) + "-liter jar with "
        answer += str(self.amount) + " liters of water"
        return answer

    def fill_jar(self) :
        self.amount = self.size

    def empty_jar(self) :
        self.amount = 0

    def pour(self, other_jar) :
        other_leftover = other_jar.size - other_jar.amount
        if self.amount <= other_leftover :
            other_jar.amount += self.amount
            self.amount = 0
        else :
            other_jar.amount = other_jar.size
            self.amount -= other_leftover

