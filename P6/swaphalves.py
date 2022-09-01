##
#  This program implements an algorithm that swaps the first and second halves 
#  of a list with an even number of values.
#

def main():
    values = [9, 13, 21, 4, 11, 7, 1, 3]
    i = 0
    j = len(values) // 2
    while i < len(values) // 2:
        swap(values, i, j)
        i = i + 1
        j = j + 1

    print(values)


def swap(a, i, j):
    """
    Swaps the elements of a list at given positions

    :param a: the list
    :param i: the first position
    :param j: the second position
    """
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


# Start the program.
main()
