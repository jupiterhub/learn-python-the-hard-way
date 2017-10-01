name = 'Jupiter Tecson'
age = 30 # not a lie
height = 168 # cm
weight = 70.6 # kilos
eyes = "Brown" # double quotes is also fine
teeth = 'White'
hair = 'Black'

# f"String {variable_name}", f on the front says to format
print(f"Let's talk about {name}")
print(f"He's {height}cm tall.")
print(f"He's {weight}kg heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

# this line is tricky, try to get it exactly right
total = age + height + weight
# use round function
print(f"If i add {age}, {height}, and {weight} I get {round(total)}")
