# Reading files
from sys import argv # load argv module from sys package

script, filename = argv # expect 2 parameters

txt = open(filename) # load the file

print(f"Here's your file {filename}")
print(txt.read())   # read lines using .read()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# Close fiel streams
txt.close()
txt_again.close()
