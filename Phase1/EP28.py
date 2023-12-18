#loop in loop

i = 1
while (i <= 3) :
    #print("i : " , i)
    j = 1
    while (j <= 3) :
        print("i : " , i,"j : ", j)
        j+=1
    i+=1


for i in range(1,4,1) :
    for j in range(1,4,1) :
        print("i : " , i,"j : ", j)
