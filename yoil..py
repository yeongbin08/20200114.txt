# 요일을 인덱스와 부합되게 해 줌

import calendar
from datetime import datetime, timedelta


startDate=calendar.weekday(2019,12,10)
finishDate=calendar.weekday(2019,5,19)
print(startDate)
my_list=["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
my_list_len=len(my_list)
for i in range(0,my_list_len):
    print(i,my_list[i])





