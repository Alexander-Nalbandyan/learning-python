from datetime import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
        23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    sleep_amount = random.randint(1, 1000) / 1000
    print(F"Sleeping for: {sleep_amount} seconds")
    time.sleep(sleep_amount)

    right_this_second = datetime.today().second

    if right_this_second in odds:
        print(F"This second: {right_this_second} seems little odd")
    else:
        print("Not an odd second")