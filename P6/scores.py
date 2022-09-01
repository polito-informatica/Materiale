##
#  This program computes a final score for a series of quiz scores: the sum after 
#  dropping the two lowest scores. The program uses a list.
#

def main():
    scores = read_floats()
    if len(scores) > 1:
        remove_minimum(scores)
        remove_minimum(scores)
        total = sum(scores)
        print("Final score:", total)
    else:
        print("At least two scores are required.")


def read_floats():
    """
    Reads a sequence of floating-point numbers

    :return: a list containing the numbers
    """

    # Create an empty list.
    values = []

    # Read the input values into a list.
    print("Please enter values, Q to quit:")
    user_input = input("")
    while user_input.upper() != "Q":
        values.append(float(user_input))
        user_input = input("")

    return values


def remove_minimum(values):
    """
    Removes the minimum value from a list

    :param values: a list of size >= 1
    """

    smallest_position = 0
    for i in range(1, len(values)):
        if values[i] < values[smallest_position]:
            smallest_position = i

    values.pop(smallest_position)


# Start the program.
main()
