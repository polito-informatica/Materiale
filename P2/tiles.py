##
#  Computes the number of tiles needed and the gap at each end when
#  placing tiles along a wall.
#

# Define the dimensions.
totalWidth = 100
tileWidth = 5

# Calculate the tiles and gaps.
numberOfPairs = (totalWidth - tileWidth) // (2 * tileWidth)
numberOfTiles = 1 + 2 * numberOfPairs
gap = (totalWidth - numberOfTiles * tileWidth) / 2.0

print("Number of tiles:", numberOfTiles)
print("Gap at each end:", gap)

