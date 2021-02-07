word = "bottles"
# for decreasing range we need to specify the step for range function otherwise the default step is +1 and it won't print
# anything if a > b with call range(a, b)
# for beer_num in range(99, 0, -1):
#     print(beer_num, word, "of beer on the wall")

# empty print prints new line on output.
print()

for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
            print(new_num, word, "of beer on the wall.")
    print()
