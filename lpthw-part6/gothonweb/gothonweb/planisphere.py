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
