# Logical operations
print(True and True) # true
print(False and True) # false
print(1 == 1 and 2 == 1) # false
# using "and" instead of "==" returns the first operand
# ie. 'False and 1' returns False
# ie. 'True and 1' returns 1
print("test" and "test") #'test' (true)
print(1 == 1 or 2 != 1) # true
print(True and 1 == 1) # true
print(False and 0 != 0) # false
print(True or 1 == 1) # true
print("test" == "testing") # false
print(1 !=0 & 2 == 1) # false
print("test" != "testing") # true
print("test" == 1) # false
print(not (1 == 1 and 0 != 1)) # false
print(not (10 == 1 or 1000 == 1000)) # false
print(not (1 != 10 or 3 == 4)) # false
print(not ("testing" == "testing" and "Zed" == "Cool Guy")) # true
print(1 == 1 and (not ("testing" == 1 or 1 == 0))) # true
print("chunky" == "bacon" and (not (3 == 4 or 3 == 3))) # false
print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))) # false
