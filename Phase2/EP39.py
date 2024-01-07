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
for i in range(len(number)) :
    box = []
    box.append(number[i])
    for j in range(i , len(number)) :
        if(box[0] >= number[j]) :
            box[0] = number[j]
            box.insert(1 , j)
    z = number[i]
    number[i] = box[0]
    number[box[1]] = z
print(number)
    



        




