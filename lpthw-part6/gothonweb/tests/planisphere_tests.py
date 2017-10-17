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

def test_central_corridor_success_to_armory():
    start_room = load_room(START)
    room = start_room.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
    assert_equal('laser_weapon_armory', name_room(laser_weapon_armory))

def test_central_corridor_deaths():
    start_room = load_room(START) # central_corridor

    scene = start_room.go('shoot!')
    assert_equal('death_via_shoot', scene.name)

    scene = start_room.go('dodge!')
    assert_equal('death_via_dodge', scene.name)

def test_weapon_armory_success_to_bridge():
    room = load_room('laser_weapon_armory')
    assert_equal(room, laser_weapon_armory)

    next_room = room.go('0132')
    assert_equal(the_bridge, next_room)

def test_weapon_armory_deaths():
    room = load_room('laser_weapon_armory')
    assert_equal(room, laser_weapon_armory)

    # TODO: update when door retry is implemented.
    #  only die on the 10x fail
    scene = room.go('*')
    assert_equal(death_via_failed_unlock, scene)

def test_bridge_success_to_escape_pod():
    room = load_room('the_bridge')
    assert_equal(room, the_bridge)

    next_room = room.go('slowly place the bomb')
    assert_equal(escape_pod, next_room)
    assert_equal('escape_pod', name_room(next_room))

def test_bridge_deaths():
    room = load_room('the_bridge')
    assert_equal(the_bridge, room)

    scene = room.go('throw the bomb')
    assert_equal(death_via_throw_bomb, scene)

def test_escape_pod_success_to_win():
    room = load_room('escape_pod')
    assert_equal(escape_pod, room)

    scene = escape_pod.go('2')
    assert_equal(the_end_winner, scene)

def test_escape_pod_deaths():
    room = load_room('escape_pod')
    assert_equal(escape_pod, room)

    scene = escape_pod.go('*') # todo make it regex
    assert_equal(the_end_loser, scene)

def test_rooms_are_registered():
    assert_equal('central_corridor', name_room(central_corridor))
    assert_equal('laser_weapon_armory', name_room(laser_weapon_armory))
    assert_equal('the_bridge', name_room(the_bridge))
    assert_equal('escape_pod', name_room(escape_pod))
