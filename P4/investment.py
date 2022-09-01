##
#  This program prints a table showing the growth of an investment.
#

# Define constant variables.
RATE = 5.0
INITIAL_BALANCE = 10000.0

# Obtain the number of years for the computation.
num_years = int(input("Enter number of years: "))

# Print the table of balances for each year.
balance = INITIAL_BALANCE
for year in range(1, num_years + 1):
    interest = balance * RATE / 100
    balance = balance + interest
    print(f'{year:4d} {balance:10.2f}')
