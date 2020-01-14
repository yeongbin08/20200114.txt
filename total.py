
#기간의 전체 날짜의 수를 찾는 것과 5일 후의 날짜 찾기 한 것입니다.
from datetime import datetime, timedelta

t1=datetime(2019,12,10,9,00,1)
t2=datetime(2020,5,20,17,40,1)
t3=datetime.now()
totalDay=t2-t1

print(t2-t1)
print(t1+ timedelta(days=5))