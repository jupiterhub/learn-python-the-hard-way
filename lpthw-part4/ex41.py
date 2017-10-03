# Class detailed, this is meant to be a training for reading OOP terms
# run the class via "python ex41.py english"
# the read through the code if interested

import random # built in generate random numbers
from urllib.request import urlopen  # from https://docs.python.org/3/library/
import sys # for args?

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'"
}

# do they want to drill phrases first
if (len(sys.argv) == 2 and sys.argv[1] == "english"):
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # cast result to string
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    # snippet.count() return number of occurences
    other_names = random.sample(WORDS, snippet.count("***"))

    # create classes based on random words
    # notice how w is inlined. no ":" after a loop
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]

    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3) #random num between 1-3 including them
        param_names.append(', '.join(
                random.sample(WORDS, param_count)))

    # note that we're looping in 2 params, it will only loops twice (1 per list)
    for sentence in snippet, phrase:
        result = sentence[:] # ???

        # fake class names
        for word in class_names:
            # only replace first occurence
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL+D
# try-catch or in python's case try-except
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets) # randomize list

        for snippet in snippets:
            # key (snippet) = class %%%(%%%):
            # value (phrase) = Make a class named %%% that is-a %%%.
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                # swap value of question and answer
                question, answer = answer, question

            print(question)
            input("< ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")


# for a in ['a','b','c'], [1, 2, 3]:
#   print("looping 2 list sample")
#    print("a:", a)
#    print("a[:]", a[:])
