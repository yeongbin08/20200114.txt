import calendar

startDate=calendar.weekday(2019,12,10)
finishDate=calendar.weekday(2020,5,19)
mon_12=calendar.monthrange(2019,12)

print(mon_12)
print(max(mon_12))
