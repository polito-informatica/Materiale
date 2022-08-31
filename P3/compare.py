##
#  This program demonstrates comparisons of numbers and strings.
#

from math import sqrt

# Comparing integers 
m = 2
n = 4

if m * m == n:
    print("2 times 2 is four.")

# Comparing floating-point numbers.
x = sqrt(2)
y = 2.0

if x * x == y:
    print("sqrt(2) times sqrt(2) is 2")
else:
    print(f"sqrt(2) times sqrt(2) is not two but {x * x:.18f}")

EPSILON = 1E-14
if abs(x * x - y) < EPSILON:
    print("sqrt(2) times sqrt(2) is approximately 2")

# Comparing strings
s = "120"
t = "20"

if s == t:
    comparison = "is the same as"
else:
    comparison = "is not the same as"

print(f"The string '{s}' {comparison} the string '{t}'.")

u = "1" + t
if s != u:
    comparison = "not "
else:
    comparison = ""

print(f"The strings '{s}' and '{u}' are {comparison}identical.")
