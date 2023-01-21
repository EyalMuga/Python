# Implement a function that receives a list of english letters and returns a list with alphabet
# indexes of the letters in the English Alphabet. Use map() to map a letter from the English alphabet
# to its alphabet index. Your code should support both lowercase and uppercase letters.
# The alphabet index for “a” and “A” is 1.
# The alphabet index for “b” and “B” is 2.
# The alphabet index for “z” and “Z” is 26.
# If one of the received elements of the list is not an English alphabet letter - raise an exception.
# For example, if you receive [‘a’, ‘Z’, ‘C’, ‘e’], your function should return [1, 26, 3, 5].
# If you receive [3, ‘bla’, ‘a’, ‘D’], you should raise an exception.
import string

def alpha2index(letter):
    if not letter.isalpha():
        raise ValueError(f'Invalid character: {letter}')
    return string.ascii_lowercase.find(letter) + 1


def compare(letters: list[str]):
    return list(map(string.ascii_lowercase.find, map(str.lower, letters)))


try:
    alpha2index(['1', 5, 'r'])
except Exception:
    print("error expected ")

print(compare(['a', 'b']))
