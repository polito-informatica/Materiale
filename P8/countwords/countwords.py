##
#  This program counts the number of unique words contained in a text document.
#

def main():
    unique_words = set()

    filename = input("Enter filename (default: nurseryrhyme.txt): ")
    if len(filename) == 0:
        filename = "nurseryrhyme.txt"
    input_file = open(filename, "r")

    for line in input_file:
        the_words = line.split()
        for word in the_words:
            cleaned = clean(word)
            if cleaned != "":
                unique_words.add(cleaned)

    print("The document contains", len(unique_words), "unique words.")


def clean(string):
    """
    Cleans a string by making letters lowercase and removing characters
    that are not letters

    :param string: the string to be cleaned
    :return: the cleaned string
    """
    result = ""
    for char in string:
        if char.isalpha():
            result = result + char.lower()

    return result


# Start the program.
main()
