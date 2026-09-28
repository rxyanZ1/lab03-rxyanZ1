from lab03 import pig_latin, word_lengths, reverse_words, letter_counts


def test_pig_latin():
    assert pig_latin("banana") == "ananabay"
    assert pig_latin("python") == "ythonpay"
    assert pig_latin("apple") == "appleway"
    assert pig_latin("igloo") == "iglooway"
    assert pig_latin("a") == "away"


def test_word_lengths():
    assert word_lengths("the quick brown fox") == [3, 5, 5, 3]
    assert word_lengths("hello") == [5]
    assert word_lengths("a bb ccc") == [1, 2, 3]
    assert word_lengths("") == []


def test_reverse_words():
    assert reverse_words("the quick brown fox") == "fox brown quick the"
    assert reverse_words("hello") == "hello"
    assert reverse_words("a b c") == "c b a"
    assert reverse_words("") == ""


# STRETCH (optional) - skipping this one still passes the three above.
def test_letter_counts():
    assert letter_counts("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert letter_counts("Mississippi") == {"m": 1, "i": 4, "s": 4, "p": 2}
    assert letter_counts("a a a") == {"a": 3}
    assert letter_counts("") == {}
