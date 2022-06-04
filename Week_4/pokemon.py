import random

class Pokemon :
    def __init__(self, name, start_health, poke_attack, poke_defense) :
        self.name = name
        self.health = start_health
        self.att = poke_attack
        self.defense = poke_defense
    
    def __str__(self) :
        return f'A {self.name} with {self.healh} health, {self.att} attack, and {self.defense} defense.'

    def calculate_damage(self, other_pokemon) :
        return (12/5 * (self.att / other_pokemon.defense) + 2) * random.uniform(0.85, 1.0)

    def attack(self, other_pokemon) :
        other_pokemon.health -= round(self.calculate_damage(other_pokemon))
        if other_pokemon.health <= 0 :
            other_pokemon.health = 0
            print (f'The {other_pokemon.name} has fainted due to having no more health!')
