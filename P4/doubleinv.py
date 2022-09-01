##
#  This program computes the time required to double an investment.
#

# Create constant variables.
RATE = 5.0
INITIAL_BALANCE = 10000.0
TARGET = 2 * INITIAL_BALANCE

# Initialize variables used with the loop.
balance = INITIAL_BALANCE
year = 0

# Count the years required for the investment to double.
while balance < TARGET:
    year = year + 1
    interest = balance * RATE / 100
    balance = balance + interest

# Print the results.   
print("The investment doubled after", year, "years.")
