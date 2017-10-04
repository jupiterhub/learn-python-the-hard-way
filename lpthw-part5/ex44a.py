# inheritance - methods
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    # note when you define a class
    # there must be at least a code
    # pass works on this
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
