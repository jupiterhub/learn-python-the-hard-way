# composition over multiple inheritance
# class Other(object) - python2 version
class Other():

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

# class Child(object) - python2 version
class Child():

    def __init__(self):
        self.other = Other()

    def override(self):
        print("CHILD override()")

    def implicit(self):
        self.other.implicit()

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
