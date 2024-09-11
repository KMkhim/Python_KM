#summation

start, stop = 1,5
sum, avg = 0, 0


while (start <= stop) :
    number = int(input("inout your number " + str(start) + " : "))
    sum += number  #ประกาศ sum ก่อนนำมาใช้ในบรรทัดนี้
    start+=1
print(sum)
print("avg : " + str(sum/stop))


#summation ver.2 ไม่ได้กำหนดขอบเขตบน -ล่าง

sum = 0
while (sum <= 100) :
    number = int(input("inout your number " + str(start) + " : "))
    sum += number  #ประกาศ sum ก่อนนำมาใช้ในบรรทัดนี้
print(sum)
