from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    word_list = text_string.split()
    for i in range(len(word_list) - n):
        # word_list_key = (word_list[i], word_list[i+(n-1), word_list[i+(n-2)])
        word_list_key = []
        for k in range(n):
            word_list_key.append(word_list[i + k])

        word_list_key = tuple(word_list_key)
        word_list_value = []
        word_list_value.append(word_list[i + n])

        # if word_list_key in chains:
        if  word_list_key not in chains:
            chains[word_list_key] = word_list_value
        else:
            chains[word_list_key].append(word_list[i + n])  

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    random_key = choice(chains.keys())
    for i in range(len(random_key)):
        text =  text + " " + random_key[i]

    while (random_key in chains.keys()):
        random_value = chains[random_key]
        random_value = choice(random_value)
        text = text + " " + random_value
        random_key = (random_key[2],random_value)

    return text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 3)

# Produce random text
random_text = make_text(chains)

print random_text
