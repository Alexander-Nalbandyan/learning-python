# iterates over given list and on each iteration assigns next value from list to the i variable.
for i in [1, 2, 3, 6, 9, 10]:
    print(i)

# iterates over characters of the string on each iteration assigning next character of the string to the variable i.
# This works because strings in Python are sequences which are ordered collection of objects.
for i in "Hellow":
    print(i)

# range(start, end) generates sequence from start to end(exclusive) range(end) = range(0, end)

# for is iterated 10 times because the range(10) gives sequence of 10 numbers 0, 1, 2, ....., 9
# So this can be used to specify how many times cycle needs to be iterated.
for i in range(10):
    print("Hello ", i)
