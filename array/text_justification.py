'''
Given an array of words and a max length per line, return an array of strings where each string represents a fully justified line. A fully justified line means that the first letter and last letter in the line should be a letter and not a space, and extra spaces are distributed as evenly as possible.

For the last line of text, it should be left-justified, and no extra space is inserted between words.
 

EXAMPLE(S)
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], k = 16

returns
["the  quick brown", // (2 spaces, 1 space)
"fox  jumps  over", // (2 spaces, 2 spaces)
"the lazy dog    "]  // (left justify, fill the end with 4 spaces)
 
FUNCTION SIGNATURE
function justify(words, maxWidth) {
def fullJustify(words: list[str], maxWidth: int) -> list[str]:

Explore:
Each word will be shorter than the max width of the line
Each word will consist of at least one character
Every two words on a line should be separated by at least one space
'''


import math


def fullJustify2(words: list[str], maxWidth: int) -> list[str]:
    track = []
    res = []
    counter = 0
    index = 0

    def format(track):
        word_count = len(track)
        word_letters_count = counter - word_count
        spaces = maxWidth - word_letters_count
        gaps = word_count - 1

        if word_count == 1:
            return track[0] + ' ' * (maxWidth - len(track[0]))
        else:
            if index < len(words):
                res = ""
                i = 0
                while i < len(track) - 1:
                    space = math.ceil(spaces / gaps)
                    res += track[i] + ' ' * space
                    spaces -= space
                    gaps -= 1
                    i += 1
                res += track[i]
                return res
            else:
                return " ".join(track) + ' ' * (spaces - gaps)

    while index < len(words):
        curr = words[index]
        track.append(curr)
        counter += len(curr)
        counter += 1
        if index + 1 < len(words) and counter + len(words[index + 1]) > maxWidth:
            res.append(format(track))
            counter = 0
            track = []

        index += 1
        if index == len(words):
            res.append(format(track))

    return res


def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    res = []
    current_line = []
    current_length = 0  # Length without counting spaces between words

    for word in words:
        # +len(current_line) accounts for spaces
        if current_length + len(current_line) + len(word) <= maxWidth:
            current_line.append(word)
            current_length += len(word)
        else:
            if len(current_line) > 1:
                spaces_needed = maxWidth - current_length
                base_space = spaces_needed // (len(current_line) - 1)
                extra_space = spaces_needed % (len(current_line) - 1)
                for i in range(extra_space):
                    current_line[i] += ' '
                line = (' ' * base_space).join(current_line)
            else:
                line = current_line[0].ljust(maxWidth)
            res.append(line)
            current_line = [word]
            current_length = len(word)

    # Handle the last line
    last_line = ' '.join(current_line).ljust(maxWidth)
    res.append(last_line)

    return res


print(fullJustify(["the", "quick", "brown", "fox",
      "jumps", "over", "the", "lazy", "dog"], 16))
print(fullJustify(["the", "quick", "brown", "fox",
      "jumps", "over", "the", "lazy", "dog"], 6))
print(fullJustify(["the", "quick", "brown", "fox",
      "jumps", "over", "the", "lazy", "dog"], 9))
