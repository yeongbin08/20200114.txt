import calendar

mon_12=calendar.monthrange(2019,12)
print(mon_12)
print(max(mon_12))
start_mon12=(max(mon_12))-9
print(start_mon12)
mon_1=calendar.monthrange(2020,1)
print(max(mon_1))
mon_2=calendar.monthrange(2020,2)
print(max(mon_2))
mon_3=calendar.monthrange(2020,3)
print(max(mon_3))
mon_4=calendar.monthrange(2020,4)
print(max(mon_4))
mon_5=calendar.monthrange(2020,5)
print(max(mon_5))
finish_mon5=(max(mon_5))-11
print(finish_mon5)
toPrd=start_mon12+(max(mon_1))+(max(mon_2))+(max(mon_3))+(max(mon_3))+finish_mon5
print(toPrd)


