# user input

print("How old are you?", end=' ') # end=' ' do not make a new line for user input
age = input()   # get user input
print("How tall are you?", end=" ") # double-quotes also work
height = input()
print("How much do you weigh?", end=' ')
weight = int(input()) # convert to int so you can do calculations

print(f"So you're {age} old, {height} tall and {weight} heavy.")
