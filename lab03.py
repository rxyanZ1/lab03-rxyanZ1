# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


from queue import Empty


def pig_latin(word):
    # TODO (Part 1): return the Pig Latin form of a single lowercase word.
    #   If it starts with a vowel (a, e, i, o, u): add "way" to the end.
    #   Otherwise: move the first letter to the end and add "ay".

    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' :
        pig_latinWord = word + 'way'
    else :
        pig_latinWord = word[1:] + word[0] + 'ay'

    return pig_latinWord

def word_lengths(sentence):
    # TODO (Part 2): return a list with the length of each word in `sentence`
    #   (words are separated by spaces).

    wordLengths = []
    wordLen = 0
    i = 0
    
    while i < len(sentence):
        char = sentence[i]

        if char != ' ':
            wordLen += 1
        else:
            wordLengths.append(wordLen)
            wordLen = 0
        i += 1

    if wordLen > 0:
            wordLengths.append(wordLen)

    return wordLengths



def reverse_words(sentence):
    # TODO (Part 3): return `sentence` with the order of its words reversed.
    #   e.g. "hello world" -> "world hello"

    words = []
    word = ''

    for char in sentence:
        if char != ' ':
            word += char
        elif word != '':
            words.append(word)
            word = ''

    if len(word) != 0:
        words.append(word)

    reverse_words = ''

    if words != []:
        reverse_words += words.pop()

    while words != []:
        reverse_words += ' '
        reverse_words += words.pop()

    return reverse_words


def letter_counts(text):
    # TODO (Part 4 - STRETCH, optional): return a dictionary mapping each letter
    #   to how many times it appears in `text`. Ignore case, and ignore anything
    #   that isn't a letter.

    charFrequencies = {}

    for char in text:
        seen = char
        
        if seen != ' ':
            if seen in charFrequencies:
                    charFrequencies[seen.lower()] += 1
            else:
                charFrequencies[seen.lower()] = 1

    return charFrequencies


def main():
    # Optional scratch space - use this to try your functions with sample values.
    print(pig_latin("banana"))                    # ananabay
    print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    print(reverse_words("the quick brown fox"))   # fox brown quick the
    print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()
