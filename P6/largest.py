##
#  This program reads a sequence of values and prints them, marking the 
#  largest value.
#

# Create an empty list.
values = []

# Read the input values.
print("Please enter values, Q to quit:")
user_input = input("")
while user_input.upper() != "Q":
    values.append(float(user_input))
    user_input = input("")

# Find the largest value.
largest = max(values)

# Print all values, marking the largest.
for element in values:
    print(element, end="")
    if element == largest:
        print(" <== largest value", end="")
    print()
