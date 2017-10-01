# More functions, with file
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) # go to the 1st byte of the file

def print_a_line(line_count, f):
    # notice readline() NO camelcase
    print(line_count, f.readline())

current_file = open(input_file)

print("First Let's print the while file:\n")
print_all(current_file)

print("\nNow let's rewind, kind of like a tape.\n")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
