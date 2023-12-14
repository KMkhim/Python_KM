age = int(input("input your age : "))
name = "กอบุญ"

#ถ้าไม่มีช่องว่างด้านหน้า คือไม่ได้อยู่ภายใต้คำสั่ง if
if age >=15 :
    print("นางสาว" + name)
else :
    print("เด็กหญิง" + name)
print("end")


if age >= 35 :
    print("วัยทำงาน")
elif age >=20 :
    print("วัยผู้ใหญ่")
elif age >=15 :
    print("วัยรุ่น")
else : 
    print("วัยเด็ก")

if age < 15 :
    print("วัยเด็ก")
elif age >=15 and age <20 :
    print("วัยรุ่น")
elif age >=20 and age <35 :
     print("วัยผู้ใหญ่")
else :
    print("วัยทำงาน")

