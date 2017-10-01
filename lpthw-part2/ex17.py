# Copy one file to the other
from sys import argv
from os.path import exists # new module

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do this in one lin add a ";"
in_file = open(from_file); indata = in_file.read()

# alternatively you can inline
# in_file = open(from_file).read() - automtically closed when program ends


# len() returns the length of string
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
