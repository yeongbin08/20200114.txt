#12월 날짜와 요일을 인텍스에 맞춰서 튜플로 나타냄

import calendar
from datetime import datetime, timedelta

mon_12=calendar.monthrange(2019,12)
time0=datetime(2019,12,1,9,00,1)
idx0=mon_12[0]
for i in range(9,31):
    timeI=time0+timedelta(days=i)
    print(timeI)

    if i>6:
        j=i%7
        print(i,j)
    else:
        i=i
        print(i,i)


    
    
   