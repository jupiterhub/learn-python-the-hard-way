print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow')) #  single quotes, double is fine too, typically short strings are in single quotes
print("Adn everywhere that Mary went.")
print("." * 10) # print string 10x

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# print('string', end=' ') - by default it goes to next line. override to be a space
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
