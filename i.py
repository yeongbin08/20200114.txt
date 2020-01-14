#요일을 인텍스로 만드는 for문
for i in range(0,10):
    
    if i>6:
        j=i%7
        print(i,j)
    else:
        i=i
        print(i,i)