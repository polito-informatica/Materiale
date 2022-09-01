##
#  This program computes the volumes of two cubes.
#

def main():
    result1 = cube_volume(2)
    result2 = cube_volume(10)
    print("A cube with side length 2 has volume", result1)
    print("A cube with side length 10 has volume", result2)


def cube_volume(side_length):
    """
    Computes the volume of a cube

    :param side_length: the length of a side of the cube
    :return: the volume of the cube
    """
    volume = side_length ** 3
    return volume


# Start the program.
main()
