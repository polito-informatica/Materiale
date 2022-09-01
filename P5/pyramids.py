## 
#  This program defines a function for calculating a pyramid's volume and
#  provides a unit test for the function.
#

def main():
    print("Volume:", pyramid_volume(9, 10))
    print("Expected: 300")
    print("Volume:", pyramid_volume(0, 10))
    print("Expected: 0")


def pyramid_volume(height, base_length):
    """
    Computes the volume of a pyramid whose base is a square.

    :param height: a float indicating the height of the pyramid
    :param base_length: a float indicating the length of one side of the pyramid's base
    :return: the volume of the pyramid as a float
    """
    base_area = base_length * base_length
    return height * base_area / 3


# Start the program.
main()
