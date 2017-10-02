# Review of reserved keywords, data types, escape sequences, operators

# +++++++++++++++++++++++++++++++++++++
# keyword
# check the book for complete list, only noting down uncommon stuff
# +++++++++++++++++++++++++++++++++++++
# https://www.programiz.com/python-programming/keyword-list
# as - import math as myAlias; myAlias.cos(myAlias.pi)
# assert - assert a < 5, "message to display on assert false" throws AssertionError
# break stops loop
# def - define function
# except - catch excetpion
#    try:
#        r = 1 / num
#    except:
#        print('Exception caught')
# exec - run string as python
# finally
# from - import from specific module
# global - declare global variable, modifying it inside a func requires global keyword on fron
#   def write1():
#    global globvar
#    globar = 5
# import
# lambda - anonymous function;
#    a = lambda x: x * 2
#    a(10) # 20
# pass - empty block. def empty() : pass
# raise - throw exception. raise ValueError("No")
# with - ensures __exit__ is called within a block. Similar to try-finally block
#    with open('example.txt') as my_file:
#        my_file.write("Hello world")
# yield - like a return but returns a "generator"  (like a stream, good for memory intense tasks)
#    def generator():
#        for i in range(6): # square the numbers till 5
#            yield i*i
#
#    g = generator()
#    next(g) # 0
#    next(g) # 1
#    next(g) # 4
#    next(g) # 9 and so on..

# +++++++++++++++++++++++++++++++++++++
# Data types
# +++++++++++++++++++++++++++++++++++++
# True, False
# None - no value. x = None (null)
# bytes - x= b"hello"
# strings
# numberss
# floats
# list - j = [1,2,3]
# dicts - e = {'x':1, 'y':2} # think map

# +++++++++++++++++++++++++++++++++++++
# Escape sequences
# +++++++++++++++++++++++++++++++++++++
# \a - Bell
# \v - Vertial tab
# \b - backspace
# \t \n \r \f \' \"

# +++++++++++++++++++++++++++++++++++++
# Formatting strings python 2 style
# +++++++++++++++++++++++++++++++++++++
# %d = "%d" % 45 == 45
# %i - int
# %o - octal
# %u - unsigned dcimal
# %x hex lowercase  ie. 3e8
# %X - hex uppercase ie. 3E8
# %e - exponentioal notation. ie. 1.000000e+01
# %E - exponentioal notation uppercase. ie. 1.000000E+01
# %f - floating point
# %g - either %f or %e whichever is smaller
# %c - character
# %s - string
# %% - percent sign

# +++++++++++++++++++++++++++++++++++++
# OPERATORS 0 skipped common ones (+,-,*,/,etc.)
# +++++++++++++++++++++++++++++++++++++
# ** - Power of
# // - Floor division
# [] - list brackets
# {} - dict curly braces
# @ - decorators. ie. @classmethod
# //= - floor divide and assign shorthand. ie. x //=2
# %= - modulus and assign shorthand. ie. x %=2
# ** - power and assign. ie. x **=2
