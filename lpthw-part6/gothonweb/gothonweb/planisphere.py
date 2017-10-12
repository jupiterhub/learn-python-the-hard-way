# you can ommit object for Python 3
# but using it is still recommended
# sa you will get to 'weird' problems
class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        # dict.get(value, fallback)
        # returns self so we can chain
        # go('west').go('east')
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        # dict.update()
        self.paths.update(paths)

        central_corridor = Room("Central Corridor",
        """
        The Gothons of Planet Percal #25 have invaded your ship
        and destroyed your entire crew.
        You are the last surviving member
        and your last mission is to get the neutron destruct bomb
        from the Weapons Armory, put it in the bridge, and blow the ship up
        after getting into an escape pod.

        You're running down the central corridor to the Weapons Armory
        when a Gothon jupms out, red saly skin, dark grimy teeth,
        and evil clown costume flowing around his hate filled body.
        He's blocking the door to the Armory
        and about to pull a weapon to blast you.
        """)
