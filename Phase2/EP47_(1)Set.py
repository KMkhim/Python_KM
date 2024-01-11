#แบบปกติ

fruit = {"มะม่วง" , "มะขาม" ,"มะยม"}
print(fruit) 
# run : {'มะม่วง', 'มะขาม', 'มะยม'}
# run ครั้งที่2  :{'มะยม', 'มะม่วง', 'มะขาม'}
# ลำดับไม่ชัดเจน ใช้ index

various = {"k" ,11, True, 50.00}
print(various)#{True, 50, 11, 'k'}

#constructor
fish = set(["ปลาดุก" ,"ปลาหมอ", "ปลาทู"])
print(fish) #{'ปลาทู', 'ปลาหมอ', 'ปลาดุก'}

#เพิ่มข้อมูลสมาชิก
fruit.add("ทุเรียน")
fruit.add("pineapple")

print(fruit)#{'ทุเรียน', 'มะม่วง', 'pineapple', 'มะยม', 'มะขาม'}

#เพิ่มหลายๆตัวในคราวเดียว
lis = [1, 2, 3]
fruit.update(lis)
print(fruit) #{'มะขาม', 'มะยม', 1, 2, 3, 'ทุเรียน', 'pineapple', 'มะม่วง'}

#loop แสดงผล

for item in fruit:
    print("ข้อมูล =>" , item)
"""
ข้อมูล => 1
ข้อมูล => 2
ข้อมูล => ทุเรียน
ข้อมูล => 3
ข้อมูล => มะม่วง
ข้อมูล => มะขาม
ข้อมูล => pineapple
ข้อมูล => มะยม
"""

#แสดงจำนวนสมาชิกใน set
print(len(fruit)) #8

if "มะเฟือง" in fruit:
    print("True")
else :
    print("False") #False

# .remove()
print(fruit) #{1, 2, 3, 'มะขาม', 'pineapple', 'มะม่วง', 'มะยม', 'ทุเรียน'}
fruit.remove("pineapple")
print(fruit)#{1, 2, 'มะม่วง', 3, 'ทุเรียน', 'มะขาม', 'มะยม'}

"""
.remove() กับ .discard() ทำหน้าที่ีลบข้อมูล แต่ถ้าข้อมูลที่สั่งให้ลบไม่มี 
remove จะขึ้น error
discard ไม่ขึ้น error
"""

fruit.clear()
print(fruit) #set()

del fruit
print(fruit) #NameError: name 'fruit' is not defined