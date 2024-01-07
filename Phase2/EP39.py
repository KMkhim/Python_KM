#Assignment รับและเรียงลำดับข้อมูล

i = 0
number = []
while(i >= 0) :
    num = int(input("input number :"))
    if(num <= 0) :
        break
    number.append(num)
    i+=1

i = 0
k = len(number)
for i in range(k) :
    box = []
    box.append(number[i])
    print("box : " , box)
    for j in range(i , k) :
        print("j is : " , j)
        if(box[0] >= number[j]) :
            box[0] = number[j]
            box.insert(1 , j)
        print("box[0] is ", box[0])
    z = number[i]
    number[i] = box[0]
    number[box[1]] = z
    print("number[i] : " ,i , number[i])
    print("")



        

print(number)


