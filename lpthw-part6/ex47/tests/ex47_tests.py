from nose.tools import *
from ex47.game import Room # ex47/game.py

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
