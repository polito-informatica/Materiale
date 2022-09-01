##
#  This program reads, scales and reverses a sequence of numbers.
#

def main():
    numbers = read_floats(5)
    multiply(numbers, 10)
    print_reversed(numbers)


def read_floats(number_of_inputs):
    """
    Reads a sequence of floating-point numbers

    :param number_of_inputs: the number of inputs to read
    :return: a list containing the input values
    """
    print("Enter", number_of_inputs, "numbers:")
    inputs = []
    for i in range(number_of_inputs):
        value = float(input(""))
        inputs.append(value)

    return inputs


def multiply(values, factor):
    """
    Multiplies all elements of a list by a factor

    :param values: a list of numbers
    :param factor: the value with which element is multiplied
    """
    for i in range(len(values)):
        values[i] = values[i] * factor


def print_reversed(values):
    """
    Prints a list in reverse order

    :param values: a list of numbers
    """
    # Traverse the list in reverse order, starting with the last element
    i = len(values) - 1
    while i >= 0:
        print(values[i], end=" ")
        i = i - 1
    print()


# Start the program.
main()
