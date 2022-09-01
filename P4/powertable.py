##
#  This program prints a table of powers of x.
#

# Initialize constant variables for the max ranges.
NMAX = 4
XMAX = 10

# Print table header.
for n in range(1, NMAX + 1):
    print(f'{n:10}', end="")
print()

for n in range(1, NMAX + 1):
    print(' ' * 8 + 'x ', end="")

print("\n", "    ", "-" * (5 + 10 * (NMAX - 1)))

# Print table body.
for x in range(1, XMAX + 1):
    # Print the x row in the table.
    for n in range(1, NMAX + 1):
        print(f"{x ** n:10d}", end="")

    print()
