# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_23.md

import calendar

month, day, year = map(int, input().split())

dayId = calendar.weekday(year, month, day)
print(calendar.day_name[dayId].upper())
