#Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency.
# Use dictionaries.


String= input('Please enter a string ')
def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary
def most_frequent(String):
    letters = [letter.lower() for letter in String if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter,"=", count , end=", ")
print(most_frequent(String))