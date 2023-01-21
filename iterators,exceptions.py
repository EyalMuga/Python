import string


# class AlphabetIterator:
#     def __init__(self, start_letter: str):
#         if start_letter not in string.ascii_letters:
#             raise ValueError('Invalid letter')
#         self.current_letter = start_letter
#         self.start_letter = start_letter
#
#     def __iter__(self):
#         if self.start_letter.islower():
#             self.letters = string.ascii_lowercase
#         else:
#             self.letters = string.ascii_uppercase
#         return self
#
#     def __next__(self):
#         if self.current_letter == self.letters[-1]:
#             raise StopIteration
#         else:
#             current_letter = self.current_letter
#             self.current_letter = self.letters[self.letters.index(self.current_letter) + 1]
#             return current_letter
#
#
# while True:
#     try:
#         start_letter = input('Enter a letter from the English alphabet: ')
#         alphabet_iterator = AlphabetIterator(start_letter)
#         break
#     except ValueError:
#         print('Invalid letter. Please try again.')
#
# for letter in alphabet_iterator:
#     print(letter, end=" ")


