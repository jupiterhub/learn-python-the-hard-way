# returns a list of tuples. [(token, word)]
# token: verb, direction,   stop,  number
# word: go,   north south, the,   1234
def scan(sentence):
    words = sentence.split()

    word_type_dict  = {
        'bear': 'noun',
        'princess': 'noun',
        'go': 'verb',
        'kill': 'verb',
        'eat': 'verb',
        'the': 'stop',
        'in': 'stop',
        'of': 'stop',
        'north': 'direction',
        'south': 'direction',
        'west': 'direction',
        'east': 'direction'}

    tokenized_words = []
    for word in words:
        token_type = word_type_dict.get(word)

        if word.isnumeric():
            # number
            tokenized_words.append(('number', int(word)))
        elif token_type:
            # get token
            tokenized_words.append((token_type, word))
        else:
            # not a number and not a token
            tokenized_words.append(('error', word))

    # for debugging
    # print("Tokenized words:", tokenized_words)
    return tokenized_words
