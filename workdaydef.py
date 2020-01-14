
       

 #한 달에 일하는 날의 수를 찾기 위한 것입니다.
def workDay(a,b):

    prd=0
    for i in range(a,b):
        print(i)
        if i%7<5:
         prd+=1
         print(prd)
        else:
            prd=prd
            print(prd)
    
    print("일하는 날의 수는 %d 입니다" %(prd))

print(workDay(1,30))
 
