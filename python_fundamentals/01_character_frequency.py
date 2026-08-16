# Problem 1: Character Frequency
# Given a string, count how many times each character appears
# and return the results in a dictionary.




def character_frequency(word):
    output = {}

    for char in word:
        if char not in output:
            output[char] = 1
        else:
            output[char] += 1

    return output

print(character_frequency("testme"))




