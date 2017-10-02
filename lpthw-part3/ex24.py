# return multiple variables, passing a list to .format() using *
print("Let's practice everthing.")
# not necessary to escape the single-quotes. just demo
print("You\'d need to know \'bout escapes with \\ that do:")

print("\n newlines addd \t tabs")

#printed with newlines as well
poem = """
\tThe lovely  world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehened  passion from intuition
and requires an explanation
\n\t\ttwhere there is none
"""

print("---------------")
print(poem)
print("---------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates # note returning multiple values

start_point = 10000

# assigning multiple values to the variables
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# It's  just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# shorthand of start_point = start_point / 10
start_point /=  10

print("We can also do that this way:")
formula = secret_formula(start_point)

# this is an easy way to apply a list to a format string
print("We'd have {} beans. {} jars, and {} crates."
    .format(*formula))  # notice the use of "*" in *formula

print("Formula", formula) # list
print("Formula", *formula) # iterated, this is what you want to use for prints
