'''
<18 ต่ำกว่าเกณฑ์
18.5 - 22.9 =  สมส่วน
23.0 - 24.9  = น้ำหนักเกิน
25.0 - 29.9  = โรคอ้วน ระดับ1
>30 = โรคอ้วนระดับอันตราย

'''

weight = int(input("input weight(kg) : "))
height = int(input("input height(cm) : "))

BMI = weight / (height/100) ** 2

if (BMI < 18 and BMI >=0) :
    print("ต่ำกว่าเกณฑ์")
if (BMI >= 18.5 and BMI <= 22.9) :
    print("สมส่วน")
if (BMI >= 23.0 and BMI <= 24.9) :
    print("น้ำหนักเกิน")
if (BMI >= 25.0 and BMI <= 29.9) :
    print("โรคอ้วน ระดับ1")
if (BMI > 30) :
    print("โรคอ้วนระดับอันตราย")
else :
    print("ไม่ทราบค่าที่ชัดเจน")