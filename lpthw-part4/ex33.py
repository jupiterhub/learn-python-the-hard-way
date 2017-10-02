# While loop and lists
# set default value on second param
def loop_and_return_list(loop_count, increment_size=1):
    numbers = []
    i = 0
    while i < loop_count:
        print(f"At the top is {i}")
        numbers.append(i)
        i += increment_size # shorthand of i = i + 1
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")
    return numbers

loop_count = 10
numbers = loop_and_return_list(loop_count, 2)

print("The numbers: ")
for num in numbers:
    print(num)
