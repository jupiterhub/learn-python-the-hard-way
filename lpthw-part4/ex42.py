# Python 3 does not require Class(object),
# ie. Class() - cleaner

# Salmon and fish has-a and is-a example
class Animal(object):
    def __init__(self, language):
        self.language = language

    def speak(self):
        print(self.language)

## Dog is-an animal
class Dog(Animal):

    def __init__(self, name):
        # dog has-a name
        self.name = name
        self.language = "Woof woof!"


## Cat is-an animals
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name
        self.language = "Meoooooow!"

## Person is not a subset of any. object
class Person(object):

    def __init__(self, name):
        ## human has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        # Python 2 requires the class, and self
        # Python 3 only requires super().__init__ (it's the same)
        # DRY
        super(Employee, self).__init__(name)

        ## employee has-a salary
        self.salary = salary

## Fish has no parents (object)
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")
rover.speak()

## satan is a Cat
satan = Cat("Satan")
satan.speak()

## mary is a Person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## Frank is an Employee - he earns a lot
frank = Employee("Frank", 120000)
print("Employee who earns 6digits:", frank.name)

## Frnank has a dog pet named rover
frank.pet = rover

## Flipper is a generic fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
