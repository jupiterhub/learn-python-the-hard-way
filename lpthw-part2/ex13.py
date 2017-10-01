# Parmeters, unpacking, variables
from sys import argv # argv is a reserved keyword. this is how you import modules

# read the WYSS section for how to run this
# unpack argv (assign to 4 variables - whatever is argv)
script, first, second, third = argv # expect 4 cli arguments

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)

# input() is used for additional input from user
