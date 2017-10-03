# Classes baby
# notice the argumet object
# also works if that parameter is not there
# the argument is for inheritance, object is default, or none specified
# you can do Song(Art) note: must be capital
class Song(object):

    # constructor
    # self is this instance (always first)
    # invisible to the caller
    # ie. Song(['song', 'lyrics'])
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # note:'self' gives access to instance vars
    # sing_me_a_song() - self is invisible to caller
    # self is just a variable name, can be anything
    def sing_me_a_song(the_instance_variable_name):
        for line in the_instance_variable_name.lyrics:
            print(line)

# start instantiating
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

# invoke method
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

# access variable
print("Accessing variables:")
print(happy_bday.lyrics)
print(bulls_on_parade.lyrics)
