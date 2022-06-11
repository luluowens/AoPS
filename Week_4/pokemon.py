'''Write a class named Pokemon that represents a Pokemon monster.
Every Pokemon should have the following attributes:

1) name: a string. Because Pokemon are more than a collection of stats.

2) health: an integer. Represents how much stamina the pokemon has left.
This number should not fall below zero. If it is at zero, the pokemon has fainted.

3) att: an integer. Represents how powerful the pokemon's attack is.
(Don't name this 'attack' because we'll name a method that.)

4) defense: an integer. Represents how well the pokemon avoids damage.

Also write 4 methods:

a) A constructor that takes 5 arguments: self and initial values for
name, starting health, attack, and defense.

b) A string representation: return a string of whatever makes sense to you.

c) A calculate_damage() method that takes 2 arguments: self and another Pokemon object.
The method returns the amount of damage self would inflict if it attacked the other Pokemon.
Use the following formula:

((12/5 * A/D) + 2)r
where A is self's attack strength, D is the other Pokemon's defense,
and r is a random floating point number from 0.85 to 1. Do not round yet.

d) An attack() method that takes 2 arguments: self and another Pokemon object.
The other Pokemon loses health equal to the above formula, rounded to the nearest integer.
However, if the other Pokemon's health would drop zero or less, it merely goes to 0
(and the Pokemon faints). If the Pokemon faints, print a message saying so.

This is a simplified version of Pokemon without Pokemon type, weakness/resistance,
attacks of different powers, speed, critical hits, levels, stat increases, items, etc.
'''

import random

class Pokemon :
    def __init__(self, name, start_health, poke_attack, poke_defense) :
        self.name = name
        self.health = start_health
        self.att = poke_attack
        self.defense = poke_defense
    
    def __str__(self) :
        return f'A {self.name} with {self.health} health, {self.att} attack, and {self.defense} defense.'

    def calculate_damage(self, other_pokemon) :
        return (12/5 * (self.att / other_pokemon.defense) + 2) * random.uniform(0.85, 1.0)

    def attack(self, other_pokemon) :
        other_pokemon.health -= round(self.calculate_damage(other_pokemon))
        if other_pokemon.health <= 0 :
            other_pokemon.health = 0
            print (f'The {other_pokemon.name} has fainted due to having no more health!')


# Create 2 Pokemon
b = Pokemon('Bulbasaur', 45, 49, 49)
print(b)
# Bulbasaur (45)
# ATT: 49 DEF: 49
c = Pokemon('Charmander', 39, 52, 43)
print(c)
# Charmander (39)
# ATT: 52 DEF: 43
 
# A couple attacks, notice that health drops
c.attack(b)
# Charmander does 4 damage!
print(b)
# Bulbasaur (41)
# ATT: 49 DEF: 49
b.attack(c)
# Bulbasaur does 5 damage!
print(c)
# Charmander (34)
# ATT: 52 DEF: 43
 
# Really long battle sequence because level 1 Pokemon are weak
c.attack(b)
# Charmander does 4 damage!
b.attack(c)
# Bulbasaur does 4 damage!
 
c.attack(b)
# Charmander does 4 damage!
b.attack(c)
# Bulbasaur does 5 damage!
 
c.attack(b)
# Charmander does 4 damage!
b.attack(c)
# Bulbasaur does 4 damage!
 
c.attack(b)
# Charmander does 4 damage!
b.attack(c)
# Bulbasaur does 4 damage!
 
c.attack(b)
# Charmander does 4 damage!
b.attack(c)
# Bulbasaur does 5 damage!
 
c.attack(b)
# Charmander does 4 damage!
b.attack(c)
# Bulbasaur does 5 damage!
 
c.attack(b)
# Charmander does 4 damage!
b.attack(c)
# Bulbasaur does 5 damage!
print(c)
# Charmander (2)
# ATT: 52 DEF: 43
 
# Check that fainting works
c.attack(b)
# Charmander does 4 damage!
print(b)
# Bulbasaur (9)
# ATT: 49 DEF: 49
b.attack(c)
# Bulbasaur does 5 damage!
# Charmander has fainted!