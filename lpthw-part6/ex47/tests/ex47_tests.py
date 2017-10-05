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
