#concatinate

fname = "korbun"
lname = "sugragarn"
age = "20"
salary = 500.90000


fullname = fname + lname + age
print(fullname)
print("Name : " + fname + "\tSurname : " + lname + "\tAge : " + age)

# .format() => {}
#การจัดรูปแบบการแสดงผล
text = "Name :{}\tSurname :{}\tAge :{}"
print(text.format(fname, lname, age))

#print(text2.format({0},{1},{2},{3}))
text2 = "Name :{0}\tSurname :{1}\tAge :{2}\toccupation :{3}\t salary :{4:.2f}"
print(text2.format(fname, lname, age, "student",salary))

# .count()
#นับจำนวนคำ
fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด แวะไปสวนทุเรียนด้วย"

print(fruit.count("ทุเรียน"))

# .startswith()
# เช็คคำขึ้นต้น 
name = "นายกอไก่ ใจดี"

if  name.startswith("นาย") :
    print("yes")
else :
    print("no")


# .endswith()
# เช็คคำลงท้าย 
name = "1150"

if name.endswith("0") :
    print("yes")
else :
    print("no")