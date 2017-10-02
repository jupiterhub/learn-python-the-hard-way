# Functions, list and string manipulation
def break_words(stuff):
    # """ these are documentation.
    # if you type help(ex25) this will be displayed
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
def sort_words(words):
    """Sorts thwe words."""
    return sorted(words) # built-in function

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0) #.pop() does not belong to 'str'
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1) #.pop() is part of 'list'. after .split()
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

def test_functions():
    """Tests all the functions in this file"""
    sentence = "The quick brown fox jumps over the lazy dog."
    broken_words = break_words(sentence)
    print("Break words", broken_words)
    # if you pass raw string, it will break per character
    print("Sort words {}".format(sort_words(broken_words)))

    print("First word:", end=' ')
    print_first_word(broken_words) # pops word
    print("after pop on first_word:", broken_words) # print again
    print("Last word:", end=' ')
    print_last_word(broken_words)
    print("after pop on last_word:", broken_words) # print again

    # notice upper-case comes sorted first before lowercased letters
    print("Sorted sentence", sort_sentence(sentence))

    print("First and last words:")
    print_first_and_last(sentence)

    print("First and last words (sorted):")
    print_first_and_last_sorted(sentence)

    help(break_words) # print help and see documentation
    help(test_functions) # print help and see documentation

# uncomment if you want to test, all call from python cli
# test_functions()
