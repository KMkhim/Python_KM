name = "korbun s"

# variable[0 : lenght]  print ตน. 0 => lenght -1
# เริ่มตำแหน่งที่ 0 และเอาความยาวมา len ตัว
'''
0   1   2   3   4   5   6   7   
k   o   r   b   u   n       s
'''
print(name[0:6]) #korbun
print(name[0:8]) #korbun s
print(name[0:]) #start to end

age = "40"

'''
0   1   
-2  -1
----------
4   0   
'''
# เริ่มตำแหน่งที่ 0 และเอาความยาวมา len ตัว
print(age[0:2]) # เริ่มตำแหน่งที่ 0 และเอาความยาวมา 2 ตัว  print 40
print(age[-2:2]) # เริ่มตำแหน่งที่ -2 และเอาความยาวมา 2 ตัว  print 40

# len function

name2 = "  khim  "
print(name2)
print("len of name2 is : " ,len(name2))

#.strip() ลบช่องว่างซ้ายขวา ของข้อความ
name2 = name2.strip()
print(name2)
print("len of name2 is : " ,len(name2))

#.lstrip() ลบช่องว่างซ้าย ของข้อความ
name2 = "  khim  "
name2 = name2.lstrip()
print(name2)
print("len of name2 is : " ,len(name2))

#.rstrip() ลบช่องว่างขวา ของข้อความ
name2 = "  khim  "
name2 = name2.rstrip()
print(name2)
print("len of name2 is : " ,len(name2))

#.lower() and .upper()
namek = "khim"
names = "KHIM"

print(namek.upper())
print(namek.lower())

#.capitalize()
#ขึ้นต้นพิมพ์ใหญ่ที่เหลือพิมพ์เล็ก
print(namek.capitalize())

# .replace("" , "")
surname = "Korragarn"
print("Surname before replace : " , surname)
surname = surname.replace("Kor","Sug")
print("Surname after replace : " , surname)

# .replace("" ,"", "")  3 paramiter
word = "ขิม เกรด 4 เรียน ชั้นปี ที่ 4"

word = word.replace("4" , "3.5" )
print(word)

word = "ขิม เกรด 4 เรียน ชั้นปี ที่ 4"
word = word.replace("4" , "3.5" , 1)
print(word)

# "str" in variable => true /false

name = "i want to do sth"
x = "want" in name
print(x)





