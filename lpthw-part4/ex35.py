# Branches and functions
from sys import exit # import exit() from sus

def is_a_number(user_input):
    # built in function. check pydoc str
    return user_input.isdigit()

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    # check if it contains 0 or 1
    if is_a_number(choice):
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0) # terminate
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        # try in here
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    # 'in' = contains
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good, job")
    # 1 or more denotes that there was an error in app
    exit(0) # you can also say exit(1)

def start():
    print("You're in a dark room.")
    print("There is a door to your right and left")
    print("Which one do you take?")

    choice = input("> ")
    # contains "left".
    # note order literal then variable
    if "left" in choice:
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
