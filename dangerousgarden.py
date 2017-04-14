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
import random


class MonsterRoom:

    def __init__(self, name, desc, monster):
        self.name = name
        self.desc = desc
        self.monster = monster
        self.connecting_rooms = []

    def __str__(self):
        return self.name

    def connects_to(self, connecting_room):
        self.connecting_rooms.append(connecting_room)

    def encounter(self, player):
        print(self.desc)
        self.monster.encounter(player)
        print("Where would you like to go next?")
        print("(Enter the number listed next to the location)")
        listout = 1
        for room in self.connecting_rooms:
            print(str(listout) + ' the ' + str(room))
            listout += 1
        selection = int(input())
        newroom = self.connecting_rooms[selection-1]
        print("You head off to the " + str(newroom))
        return newroom

class Entry:

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.connecting_rooms = []

    def __str__(self):
        return self.name

    def connects_to(self, connecting_room):
        self.connecting_rooms.append(connecting_room)

    def encounter(self, player):
        print(self.desc)
        ##whatever encounter goes here
        print("Where would you like to go next?")
        print("(Enter the number listed next to the location)")
        listout = 1
        for room in self.connecting_rooms:
            print(str(listout) + ' the ' + str(room))
            listout += 1
        selection = int(input())
        newroom = self.connecting_rooms[selection-1]
        print("You head off to the " + str(newroom))
        return newroom

class Exit:

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.connecting_rooms = []

    def __str__(self):
        return self.name

    def connects_to(self, connecting_room):
        self.connecting_rooms.append(connecting_room)

    def encounter(self, player):
        print(self.desc)
        if player.macguffin:
            print("You have a thing! You win!")
        else:
            print("You need a macguffin! Go out and beat plants up till you get it.")
            return Atrium

class Monster:
    def __init__(self):
        self.intro = random.choice(["Hello I am Steve I am here to hurt you now.",
            "Hi I'm not Steve, I am another plant."])
        self.wallop = "Steve wallops you for "
        self.defeat = "Steve keels over with a pollen-filled death rattle."
        self.loot = ["bat", "hammer", "vine whip"]

    def encounter(self, player):
        player.monster_intro(self.intro)
        hp = 3
        while hp > 0:
            damage = 1
            player.take_damage(self.wallop, damage)
            hp -= player.deal_damage()
        if hp <= 0:
            player.fight_win(self.defeat, self.loot)

class Player:
    def __init__(self, location):
        self.hitpoints = 10
        self.location = location

    def encounter(self):
        self.location = self.location.encounter(self)

    def monster_intro(self, message):
        print(message)

    def take_damage(self, message, damage):
        self.hitpoints -= damage
        print(message + str(damage) + ' hitpoints!')
        if self.hitpoints <= 0:
            self.fight_lose()

    def deal_damage(self):
        print("How much damage would you like to do?")
        damage = int(input())
        return damage

    def fight_win(self, message, loots):
        print(message)
        print("You win the fight!")
        print("Would you like to replace your <current verb> with new loot?")
        print("(Enter the number listed next to the item)")
        listout = 1
        for stuff in loots:
            print(str(listout) + ' a ' + stuff)
            listout += 1
        selection = int(input())
        newloot = loots[selection-1]
        print("You drop your <current verb> and grab up a " + newloot)

    def fight_lose(self):
        print("You lose the fight, and also the game.")
        exit()


A_monster = Monster()
S_monster = Monster()

atrium = MonsterRoom("Atrium", "atrium desc", A_monster)
entry = Entry("Entryway", "entryway desc")
steamy = MonsterRoom("Steamroom", "steamy", S_monster)
exit = Exit("Exit", "exit desc")

entry.connects_to(atrium)
atrium.connects_to(steamy)
steamy.connects_to(atrium)
atrium.connects_to(exit)


player = Player(atrium)
while player.location:
    player.encounter()



























    #
