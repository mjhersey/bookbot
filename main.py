def word_count(file_contents):
    words = file_contents.split()
    return len(words)


def character_count(file_contents):
    char_dictionary = {}
    file_contents = file_contents.lower()
    for char in file_contents:
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1

    return char_dictionary


def print_report(char_dictionary):
    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count(file_contents), " words found in the document")

    # convert the dictionary to a list
    char_list = list(char_dictionary.items())
    # sort the list by value, high value first
    char_list = sorted(char_list, key=lambda x: x[1], reverse=True)

    for key, value in char_list:
        if str(key).isalpha():
            print("The '" + key + "' character was found " + str(value) + " times")

    print("--- End report of books/frankenstein.txt ---")


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

print(word_count(file_contents))
print(character_count(file_contents))
print_report(character_count(file_contents))
