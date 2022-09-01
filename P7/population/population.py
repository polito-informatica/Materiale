##
#  This program reads data files of country populations and areas and prints the
#  population density for each country.
#

POPULATION_FILE = "worldpop.txt"
AREA_FILE = "worldarea.txt"
REPORT_FILE = "world_pop_density.txt"


def main():
    # Open the files.
    pop_file = open(POPULATION_FILE, "r")
    area_file = open(AREA_FILE, "r")
    report_file = open(REPORT_FILE, "w")

    # Read the first population data record.
    pop_data = extract_data_record(pop_file)
    while len(pop_data) == 2:
        # Read the next area data record.
        area_data = extract_data_record(area_file)

        # Extract the data components from the two lists.
        country = pop_data[0]
        population = pop_data[1]
        area = area_data[1]

        # Compute and print the population density.
        density = 0.0
        if area > 0:  # Protect against division by zero.
            density = population / area
        report_file.write("%-40s%15.2f\n" % (country, density))

        # Read the next population data record.
        pop_data = extract_data_record(pop_file)

    # Close the files.
    pop_file.close()
    area_file.close()
    report_file.close()


def extract_data_record(infile):
    """
    Extracts and returns a record from an input file in which the data is
    organized by line. Each line contains the name of a country (possibly
    containing multiple words) followed by an integer (either population
    or area for the given country).

    :param infile: the input text file containing the line oriented data
    :return: a list containing the country (string) in the first element
        and the population (int) or area (int) in the second element. If the end of
        file was reached, an empty list is returned.
    """
    line = infile.readline()
    if line == "":
        return []
    else:
        parts = line.rsplit(" ", 1)
        parts[1] = int(parts[1])
        return parts


# Start the program.
main()
