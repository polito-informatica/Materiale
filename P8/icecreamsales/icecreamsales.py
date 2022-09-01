## 
#  This program processes a collection of sales data for flavors of ice cream
#  and prints a report sorted by flavor.
#

def main():
    sales_data = read_data("icecream.txt")
    print_report(sales_data)


def read_data(filename):
    """
    Reads the tabular data

    :param filename: name of the input file
    :return: a dictionary whose keys are ice cream flavors and whose values are sales data
    """
    # Create an empty dictionary.
    sales_data = {}

    infile = open(filename, "r")

    # Read each record from the file.
    for line in infile:
        fields = line.split(":")
        flavor = fields[0]
        sales_data[flavor] = build_list(fields)

    infile.close()
    return sales_data


def build_list(fields):
    """
    Builds a list of store sales contained in the fields split from a string.

    :param fields: a list of strings comprising the record fields
    :return: a list of floating-point values
    """
    store_sales = []
    for i in range(1, len(fields)):
        sales = float(fields[i])
        store_sales.append(sales)

    return store_sales


def print_report(sales_data):
    """
    Prints a sales report
    :param sales_data: a table composed of a dictionary of lists
    """
    # Find the number of stores as the length of the longest store sales list.
    num_stores = 0
    for store_sales in sales_data.values():
        if len(store_sales) > num_stores:
            num_stores = len(store_sales)

    # Create a list of store totals.
    store_totals = [0.0] * num_stores

    # Print the flavor sales.
    for flavor in sorted(sales_data):
        print(f'{flavor:15}', end='')

        flavor_total = 0.0
        store_sales = sales_data[flavor]
        for i in range(len(store_sales)):
            sales = store_sales[i]
            flavor_total = flavor_total + sales
            store_totals[i] = store_totals[i] + sales
            print(f'{sales:10.2f}', end='')

        print(f'{flavor_total:15.2f}')

    # Print the store totals.
    print(" " * 15, end="")
    for i in range(num_stores):
        print(f'{store_totals[i]:10.2f}', end='')
    print()


# Start the program.
main()
