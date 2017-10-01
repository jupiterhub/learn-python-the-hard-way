# escaping characters, singlequote, double, tab, newline
tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line." #\n
backslash_cat = "I'm \\ a \\ cat"

# triple single quotes also work
fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
