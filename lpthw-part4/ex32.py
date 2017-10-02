# For Loops and lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
# notice use of double quotes (same as single)
change = [1, "pennies", 2, 'dimes', "quarters"]

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"this is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we ca go through mixed lists too
# notice we have to use {} since we don't know what's in
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# The use range function to do 0 to 5 counts
for i in range(0,6): # loop stops at 6
    print(f"Adding {i} to the list.")
    # append is a function that lists Understand
    elements.append(i)

# this appends the whole list within a list
# elements.append(range(0,6))

print("Putting additional element")
elements.append("Added element")

# now we can print them out too
for i in elements:
    print(f"Element was {i}")
