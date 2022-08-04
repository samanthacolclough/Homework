"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""
from collections import Counter

characters = "masmassam"
phrase = "samsamsam"

def generate_phrase(characters, phrase):
    phrase_cnt = Counter(phrase.lower())
    chars_cnt  = Counter(characters.lower())

    if len(phrase) > len(characters):  # not enough characters to match required phrase
        return False

    for ch, cnt in phrase_cnt.items():

        if ch in chars_cnt and cnt <= chars_cnt.get(ch):
            continue
        else:
            return False

    return True


if __name__ == '__main__':

 print(generate_phrase(characters, phrase)) # returns true
 print(generate_phrase('lipgloss', 'slogans')) # returns false











