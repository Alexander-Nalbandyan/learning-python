from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13]

right_this_minute = datetime.today().second

if right_this_minute in odds:
    print("This minute seems a little odd." + str(right_this_minute))
else:
    print("Not an odd minute: " + str(right_this_minute))
