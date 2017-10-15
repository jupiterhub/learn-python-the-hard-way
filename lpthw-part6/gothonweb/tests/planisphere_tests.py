from nose.tools import *
from gothonweb.planisphere import * # import class and variables

def setup():
    print("SETUP!")

def teardown():
    print("Tear Down!")

def test_basic():
    print("I RAN!")

def test_room():
    gold = Room("GoldRoom", """
            This room has gold in it you can grab.
            There's a door to the north
            """)
    # function comes from nosetools
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the center.")
    south = Room("South", "Test room in the center.")

    center.add_paths({'north': north, 'south': south})

    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "you can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    start_room = load_room(START)
    room = start_room.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
    assert_equal('laser_weapon_armory', name_room(laser_weapon_armory))

def test_central_corridor_deaths():
    start_room = load_room(START) # central_corridor
    scene = start_room.go('shoot!')

    assert_equal('death_via_gothon', scene.name)
