"""
Dangerous Garden

An adventure in a garden of beautiful and often dangerous plants. You have been
tasked to get a particular plant for (reason). There is the Entryway, the Main
Atrium, and the Steam Room. There are encounters with plants in each area with
negative and positive outcomes. The player can collect equipment/effects from
encounters. It's like a murderous KOL garden.



Death
This is when the player dies.

Entryway
This is the starting point. The player might be able to pick up an item from a
small selection of items which allow access to an additional (verb).

Atrium
A place to encounter easier plants.

Steam
A place to encounter more difficult plants.

Exit
This is where the player can leave the garden if the player has the (macguffin).

Map
    -next_scene
    -entry_scene
Engine
    -play
Scene
    -entry
    Fighting
    Winning (Getting loot)
    Losing (Death)
    Exit

"""

class Room:

    def __init__(self, name, desc, monster):
        self.name = name
        self.desc = desc
        self.monster = monster

    def arrived(self, readout):
        readout.printout(self.desc)
        self.monster.encounter(readout)


class Monster:
    def __init__(self):
        self.intro = "Hello I am Steve I am here to hurt you now."
        self.wallop = "Name wallops you for "

    def encounter(self, player):
        player.monster_intro(self.intro)
        hp = 3
        while hp > 0:
            damage = 1
            player.take_damage(self.wallop, damage)
            hp -= player.deal_damage()

class Player:
    def __init__(self):
        pass

    def monster_intro(self, message):
        print(message)

    def take_damage(self, message, damage):
        print(message + str(damage) + ' hitpoints!')

    def deal_damage(self):
        print("How much damage would you like to do?")
        damage = int(input())
        return damage

class MockMonster:
    def __init__(self):
        self.was_called = 0
        pass

    def encounter(self, readout):
        self.was_called += 1
        pass

class MockReadout:
    def __init__(self):
        pass

    def printout(self, string):
        self.seen = string

p = Player()
m = Monster()
m.encounter(p)


## arrange
fake_readout = MockReadout()
fake_monster = MockMonster()
room = Room("fake name", "fake desc", fake_monster)
## act
room.arrived(fake_readout)
## assert
assert(fake_monster.was_called == 1)
assert("fake desc" == fake_readout.seen)


























    #
