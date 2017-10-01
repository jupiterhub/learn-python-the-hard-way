from sys import argv

script, filename = argv # expect 2 cli params

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("opening the file...")

target = open(filename, 'w') # open the file with write perm

print("Truncating the file. Goodbye!")
# this is not necessary
# when you open with 'w' write mode, file is automatically truncated
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
target.write(line1 + "\n" + line2 + "\n" + line3)

print("And finally, we close it.")
target.close()
