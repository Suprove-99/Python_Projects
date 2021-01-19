from datetime import datetime

today = str(datetime.date(datetime.now()))
today = list(int(i) for i in today.split('-'))
# print(today)
while True:
    print("Enter your Birth Date:")
    birth = [int(input("Year")), int(input("Month")), int(input("Day"))]
    flag = ''
    if (birth[0] | birth[1] | birth[2]) < 1 or (birth[1] > 12) or birth[2] > 31:
        print("Incorrect info. Do you want to try again? y/n :")
        flag = str.lower(input())
        if flag is 'y':
            continue
        else:
            break
    else:

        # day
        if today[2] < birth[2]:
            day = today[2] + 30 - birth[2]
            birth[1] = birth[1] + 1
        else:
            day = today[2] - birth[2]

            # month
        if today[1] < birth[1]:
            month = today[1] + 12 - birth[1]
            birth[0] = birth[0] + 1
        else:
            month = today[1] - birth[1]

            # year
        year = today[0] - birth[0]

        print("Your age is:", year, "Year", month, "Month", day, "Day")
    break
