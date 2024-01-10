#เขียนแบบ primitive
a = 1
a1 = 2
a2 = 3
a3 = 4
a4 = 5

#non primitive : list

#การนิยาม
number = [] #empty list
number = [1, 2, 3, 4, 5, 6] #list มีสมาชิก 1-6
name = ["A" , "B" , "C"] # list name มีสมาชิกเป็น string
all = [10, "A", True, 3.14, -10] #คละกัน

#constructor 
name = list(["A" , "B" , "C"])

#output
print(name , type(name)) #['A', 'B', 'C'] <class 'list'>
print(all) #[10, 'A', True, 3.14, -10]
print(number) #[1, 2, 3, 4, 5, 6]

#การเข้าถึงข้อมูล(เดี่ยว)
print(number[0]) #1
print(number[2]) #3
print(number[0] + number[2]) #4

"""
list  1  2  3  4  5

ตน.   0  1  2  3  4
     -5 -4 -3 -2 -1 

"""

#การเข้าถึงข้อมูล(ช่วง)
print(all[1:3]) #['A', True]
print(all[1:4]) #['A', True, 3.14]
print(all[-3:-1]) #[True, 3.14]

#การแก้ไขข้อมูล
#ชื่อตัวแปร [index] = "ข้อมูลที่ต้องการแก้ไข"
number = [1, 2, 3, 4, 5, 6]
print("number[2] Before : " , number[2]) #3
number[2] =  9 
number[-1] = "A"
print("number[2] after : " , number[2]) #9
print(number) [1, 2, 9, 4, 5, 'A']

