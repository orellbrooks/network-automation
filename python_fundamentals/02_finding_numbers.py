# Problem 2: Find Numbers
# Given a string containing words and numbers,
# return a list containing only the numbers.
#
# Example:
# Input: "Switch 1 has 24 ports and Switch 2 has 48 ports"
# Output: [1, 24, 2, 48]


input = "Switch 1 has 24 ports and Switch 2 has 48 ports"

def find_numbers(text):
    output = []
    clean_data = text.split()

  
    for word in clean_data:
        if word.isdigit():
            output.append(int(word))

    return output
    

print(find_numbers(input))
