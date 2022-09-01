##
#  This program computes an estimate of pi by simulating 
#  dart throws onto a square.
#

import random

TRIES = 10000

hits = 0
for i in range(TRIES):

    # Generate two random numbers between -1 and 1
    r = random.random()
    x = -1 + 2 * r
    r = random.random()
    y = -1 + 2 * r

    # Oppure:
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    # Check whether the point lies in the unit circle
    if x * x + y * y <= 1:
        hits = hits + 1

# The ratio hits / tries is approximately the same as the ratio 
# circle area / square area = pi / 4.

pi_estimate = 4.0 * hits / TRIES
print("Estimate for pi:", pi_estimate)
