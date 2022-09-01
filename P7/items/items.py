##
#  This program reads a file whose lines contain items and prices, like this:
#  item name 1: price1
#  item name 2: price2
#  ...
#  Each item name is terminated with a colon.
#  The program writes a file in which the items are left-aligned and the 
#  prices are right-aligned. The last line has the total of the prices.
#

# Prompt for the input and output file names.
input_file_name = input("Input file: ")
output_file_name = input("Output file: ")

# Open the input and output files.
input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w")

# Read the input and write the output.
total = 0.0

for line in input_file:
    # Make sure there is a colon in the input line, otherwise skip the line.
    if ":" in line:
        # Split the record at the colon.
        parts = line.split(":")

        # Extract the two data fields.
        item = parts[0]
        price = float(parts[1])

        # Increment the total.
        total = total + price

        # Write the output.
        output_file.write(f'{item:<20s}{price:10.2f}\n')

# Write the total price.

output_file.write(f'{"Total:":<20s}{total:10.2f}')

# Close the files.
input_file.close()
output_file.close()
