#break / continue

i = 1
while (i <= 10) :
    print("i : ", i)
    if (i == 5) :
        break
    i+=1
else :
    print("end")
print("end2")


i = 0
while (i <= 10) :
    i+=1 # มันจะถูกตรวจก่อน แล้วค่อยบวกเพิ่ม เลยมีเลข  i = 11
    if (i == 5) :
        continue
    print("i : ", i) #เมื่อ i = 5 คำสั่งนี้จะไม่ทำงานเพรา continue
else :
    print("end")
print("end2")