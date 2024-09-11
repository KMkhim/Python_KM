
#ค้นหาและนับจำนวนสมาชิก .count()

tup = (1, 2, 3, 4, "khim", "mango", True, 3.99, 4)
print(tup.count(4)) #2

#หาตำแหน่งของข้อมูล(ตัวแรกที่เจอ)
print(tup.index(4)) #3

# .sort()
tup = (100, 99, 98, 66 ,900, 1)
#print(tup.sort()) #'tuple' object has no attribute 'sort'

#tuple => list
lis = list(tup)
lis.sort()
print(lis) #[1, 66, 98, 99, 100, 900]

tup = tuple(lis)
print(tup) #(1, 66, 98, 99, 100, 900)

#นำค่า tuple ใส่ใน ตัวแปร
tup = (10, 20, 30)
a, b , c = tup
print(a , b, c) #10 20 30

#สลับตัวแปร
x = (50, 60)
y = (1, 2)

x,y = y,x

print(x) #(1, 2)
print(y) #(50, 60)

#แปลง tuple เป็น string

charac = ("k", "h", "i", "m")
name = "".join(charac) #เอา str "" ไป join กับ ตัวอักษรสี่ตัว และเก็บไว้ที่ตัวแปร name
print(name) #khim

# reverse tuple
x = (1, 2, 3)
#x = x.reverse() 'tuple' object has no attribute 'reverse'
y = reversed(x)
print(tuple(y)) #(3, 2, 1)


#string => tuple
x = "khim"
y = tuple(x)
print(y) #('k', 'h', 'i', 'm')
z = tuple(reversed(x))
print(z) #('m', 'i', 'h', 'k')