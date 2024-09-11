#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = weight(kg) / height*htight (m)

weight = input("weight(kg) : ")
height = input("height(m) : ")

BMI = float(weight) / float(height)**2

print("Your BMI is : " , BMI)