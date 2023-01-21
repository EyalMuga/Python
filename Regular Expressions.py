import re


def is_capitalized(word):
    pattern = r"^[A-Z][a-z]*$"
    # return TRUE for any string starts with capitalized letter followed by any chars not capitalized
    if re.fullmatch(pattern, word):
        return True
    return False


# print(is_capitalized("Eyal"))


def has_tata_box(dna_string):
    pattern = r"TATAA[ACGT]{3}TT"
    if re.search(pattern, dna_string):
        return True
    return False


# print(has_tata_box("ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
# print(has_tata_box("ACGACGTTTACACGGATATAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))

# Match two digits then any character then two non digits
def match_pattern(string):
    pattern = r'[a-zA-Z]{2}.[^A-Za-z]{2}$'
    if re.match(pattern, string):
        return True
    return False


# print(match_pattern('AB.22'))


# Check whether the given string contains at least two TATA-lke patterns
def TATA2more(dna_string):
    pattern = r"TATAA[ACGT]{3}TT(TATAA[ACGT]{3}TT){2,}"
    if re.search(pattern, dna_string):
        return True
    return False


# checks exactly 2
def TATA2(dna_string):
    pattern = r"TATAA[ACGT]{3}TT(TATAA[ACGT]{3}TT){,2}"
    if re.search(pattern, dna_string):
        return True
    return False


# Write a regular expression to look for 3 digits, possibly separated by whitespace.
def has_three_digit_number(string):
    # \d for any digit in range 0-9- {3} times and then \s whitespaces 0 or more times
    pattern = r"\d{3}\s*"
    if re.search(pattern, string):
        return True
    return False


# Find all the israeli cell phone numbers in the text.
def israeli_number_verification(phone):
    pattern = r'^05\d-\d{7}$'
    if re.fullmatch(pattern, phone):
        return True
    return False


print(israeli_number_verification('052-6021864'))
