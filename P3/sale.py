##
#  Compute the discount for a given purchase.
#

# Obtain the original price.
original_price = float(input("Original price before discount: "))

# Determine the discount rate.
if original_price < 128:
    discount_rate = 0.92
else:
    discount_rate = 0.84

# Compute and print the discount.
discounted_price = discount_rate * original_price
print(f"Discounted price: {discounted_price:.2f}")
