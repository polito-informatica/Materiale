##
#  This program simulates tosses of a pair of dice.
#

from random import randint

for i in range(10):
    # Generate two random numbers between 1 and 6, inclusive.
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    # Print the two values.
    print(d1, d2)
