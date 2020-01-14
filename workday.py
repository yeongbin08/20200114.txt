#

prd=0
for i in range(1,30):
    print(i)
    if i%7<5:
        prd+=1
        print(prd)
    else:
        prd=prd
        print(prd)

print("일하는 날의 수는 %d 입니다" %(prd))
 