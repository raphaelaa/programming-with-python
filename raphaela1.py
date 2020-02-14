#from adventurelib import *
import adventurelib as a
import random

a.Room.items = a.Bag()

current_room = starting_room = a.Room("""
You are in a dark room.
""")

valley = starting_room.north = a.Room("""
You are in a beautiful valley.
""")

magic_forest = valley.north = a.Room("""
You are in a enchanted forest where magic grows wildly.
""")

cave = magic_forest.north = a.Room("""
You are inside a dark cave.
You hear a waterfall nearby.""")

waterfall = cave.east = a.Room(""" You are inside a waterfall and see a secret entrance.""")

secret_entrance = waterfall.south = a.Room("""You found the entrance and you see a plane!!!""")

plane = secret_entrance.east = a.Room(""" You are in the plane and you should fly to NYC""")


mallet = a.Item('rusty mallet', 'mallet')
flower= a.Item ("pretty flower", "flower")
valley.items = a.Bag({mallet, flower})

wizard = a.Item('wizard', 'the wizard', 'a wizard')
wizard.answers = ["Geht so", "jaja", "akra-ka-babra!"]

bear = a.Item( "terrifying bear", "big bear", "bear")
cave.items= a.Bag({bear})

key = a. Item(" golden key", "key")
waterfall.items = a. Bag({key})

pilot = a.Item (" pilot")
ticket= a.Item(" useful ticket", "ticket")
secret_entrance. item = a. Bag({pilot, ticket})

# a bag is a python SET !!
magic_forest.items = a.Bag({wizard,}) # ITEMS must be in a bag

inventory = a.Bag()


@a.when('north', direction='north')
@a.when('south', direction='south')
@a.when('east', direction='east')
@a.when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        a.say('You go %s.' % direction)
        look()
        if room == magic_forest:
            a.set_context('magic_aura')
        else:
            a.set_context('default')


@a.when('take ITEM')
def take(item):
    if item == "wizard":
        a.say("The wizard does not want to be picked up by you")
        return
    obj = current_room.items.take(item)
    if obj:
        a.say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        a.say('There is no %s here.' % item)

@a.when("talk", thing=None)
@a.when("thal to", thing=None)
@a.when("talk THING")
@a.when("talk to THING")
def talk(thing):
    if thing == None:
        a.say("You talk a bit to yourself")
        return
    # check if the thing is in the inventory or in the current room
    # inventory and room.items are SET's. to merge them, I use pythons join command
    for i in inventory.union(current_room.items):
        if thing in i.aliases:
            exist = True
            break
    else:
        # else in a for loop means the whole loop was interrated trough, without any break
        a.say("there is no {} to talk to, neither in your inventory nor in this room/location".format(thing))
        return
    # the thing exist. thing is a string, i is the object
    a.say("you talk to {}...".format(thing))
    # check if object i (the item) has the .answers attribute
    if "answers" in i.__dict__.keys():
        a.say("and the {} says: '{}'".format(thing, random.choice(i.answers)))
    else:
        a.say("but you get no reply. None at all. It seems that the {} is unable to talk".format(thing))





@a.when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        a.say('You do not have a %s.' % thing)
    else:
        a.say('You drop the %s.' % obj)
        current_room.items.add(obj)


@a.when('look')
def look():
    a.say(current_room)
    if current_room.items:
        for i in current_room.items:
            a.say('A %s is here.' % i)


@a.when('inventory')
def show_inventory():
    a.say('You have:')
    for thing in inventory:
        a.say(thing)

@a.when('cast', magic=None, context='magic_aura')
@a.when("cast MAGIC", context='magic_aura')
def cast(magic):
    if magic == None:
        a.say("Which magic you would like to spell?")
    elif magic == "fireball":
        a.say("you cast a flaming Fireball! Woooosh....")




look()
a.say("hallo Raphaela")
a.start()
