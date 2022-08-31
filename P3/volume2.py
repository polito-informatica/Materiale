##
#  This program prints the price per ounce for a six-pack of cans.
#

# Define constant for pack size.
CANS_PER_PACK = 6

# Obtain price per pack and can volume.
user_input = input("Please enter the price for a six-pack: ")
pack_price = float(user_input)

user_input = input("Please enter the volume for each can (in ounces): ")
can_volume = float(user_input)

# Compute pack volume. 
pack_volume = can_volume * CANS_PER_PACK

# Compute and print price per ounce.
price_per_ounce = pack_price / pack_volume
print("Price per ounce: %8.2f" % price_per_ounce)  # using %-formatting
print(f'Price per ounce: {price_per_ounce:8.2f}')  # using f-Strings

