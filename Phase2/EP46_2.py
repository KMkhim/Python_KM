tup = (1, 2, 3, 4, "khim", "mango", True, 3.99)

#แสดงผลด้วย loop
for item in tup :
    print (item)

#ตรวจสอบข้อมูล
if "durian" in tup :
    print("True")
else :
    print("False") #False

#นับจำนวนสมาชิก len()
print(len(tup)) #8

for item in range(len(tup)) :
    print(tup[item]) #tup[0] tup[1] ... tup[7]
#1 2 3 4 khim mango True 3.99
    
#การสร้างและเพิ่มข้อมูล
x = ()
print(type(x)) #<class 'tuple'>

y = ("khim")
print(type(y)) #<class 'str'>

y = ("khim" ,)
print(type(y)) #<class 'tuple'>

z = (1)
print(type(z)) #<class 'int'>

z = (1, )
print(type(z)) #<class 'tuple'>

name = ("khim" , "Prawta" )
new = "bb"

#name = name + new "cannot use" คนละ type

name = name + (new ,)
print(name) #('khim', 'Prawta', 'bb')

name = name + tuple(new)
print(name) #('khim', 'Prawta', 'bb', 'b', 'b')

#del ลบข้อมูล 
tup3 = (1, 2, 3, 4)
""" del tup """
print(tup3) #NameError: name 'tup' is not defined

lis = list(tup3) #tuple => list
print(lis) #[1, 2, 3, 4]

lis.pop() #ลบตัวท้ายสุด

print(lis) #[1, 2, 3]

lis.remove(2)

print(lis) #[1, 3]

print(tup3)#(1, 2, 3, 4)

tup3 = tuple(lis)

print(tup3)#(1, 3)
