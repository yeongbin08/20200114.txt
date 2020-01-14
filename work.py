import calendar
from datetime import datetime, timedelta

mon_12=calendar.monthrange(2019,12)

print(mon_12)
print(max(mon_12))
print(mon_12[0])
time0=datetime(2019,12,1,9,00,1)
idx0=mon_12[0]
print(idx0)
timeI=time0+timedelta(days=1)
idxI=idx0+1
print(idxI)
print(timeI)
print(time0)


