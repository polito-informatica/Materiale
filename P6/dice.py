##
#   This program reads a sequence of die toss values and prints how many times
#   each value occurred.
#

def main():
    counters = count_inputs(6)
    print_counters(counters)


def count_inputs(sides):
    """
    Reads a sequence of die toss values between 1 and sides (inclusive)
    and counts how frequently each of them occurs

    :param sides: the die's number of sides
    :return: a list whose ith element contains the number of times the value i
        occurred in the input. The 0 element is unused
    """
    counters = [0] * (sides + 1)  # counters[0] is not used.

    print("Please enter values, Q to quit:")
    user_input = input("")
    while user_input.upper() != "Q":
        value = int(user_input)

        # Increment the counter for the input value.
        if 1 <= value <= sides:
            counters[value] = counters[value] + 1
        else:
            print(value, "is not a valid input.")

        # Read the next value.
        user_input = input("")

    return counters


def print_counters(counters):
    """
    Prints a table of die value counters

    :param counters: a list of counters. counters[0] is not printed
    :return:
    """
    for i in range(1, len(counters)):
        print(f"{i}: {counters[i]}" )


# Start the program.
main()
