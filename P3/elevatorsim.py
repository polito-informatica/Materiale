##
#  This program simulates an elevator panel that skips the 13th floor.
#

# Obtain the floor number from the user as an integer.
floor = int(input("Floor: "))

# Adjust floor if necessary.
if floor > 13:
    actual_floor = floor - 1
else:
    actual_floor = floor

# Print the result.
print("The elevator will travel to the actual floor", actual_floor)
