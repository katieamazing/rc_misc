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
from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class Atrium(Scene):

    def enter(self):
        pass

class Steam(Scene):

    def enter(self):
        pass

class Loot(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, entry_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def entry_scene(self):
        pass

a_map = Map('main_atrium')
a_game = Engine(a_map)
a_game.play()
