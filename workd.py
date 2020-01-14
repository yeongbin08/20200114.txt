my_list=["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
my_list_len=len(my_list)
prd=0
for i in range(0,my_list_len):
    print(i)
    if i<5:
        prd+=1
        print(prd)
    else:
        prd=prd
        print(prd)
 
