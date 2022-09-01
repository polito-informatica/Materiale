##
#  This program reads a file containing numbers and writes the numbers to 
#  another file, lined up in a column and followed by their total and average.
#

# Prompt the user for the name of the input and output files.
input_file_name = input("Input file name: ")
output_file_name = input("Output file name: ")

# Open the input and output files.
infile = open(input_file_name, "r")
outfile = open(output_file_name, "w")

# Read the input and write the output.
total = 0.0
count = 0

line = infile.readline()
while line != "":
    value = float(line)
    outfile.write(f"{value:15.2f}")
    total = total + value
    count = count + 1
    line = infile.readline()

# Output the total and average.
outfile.write("%15s\n" % "--------")
outfile.write("Total: %8.2f\n" % total)

avg = total / count
outfile.write("Average: %6.2f\n" % avg)

# Close the files.
infile.close()
outfile.close()
