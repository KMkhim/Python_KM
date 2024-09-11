#การนิยาม Tuple
tup = (1, 2, 3, 4) #tuple
print(tup) #(1, 2, 3, 4)

tup = (1, "k", True, 3.9)
print(tup) #(1, 'k', True, 3.9)

print(type(tup)) #<class 'tuple'>

#constructor
tup1 = tuple(((1, 2, 3, 4)))
print(tup1) #(1, 2, 3, 4)

#tuple vs list
lis = list([1, 2, 3, "k"])
tup1 = tuple((1, 2, 3, 4))
print(len(tup1))

lis[0] = 29
#tup1[0] = 29
print(lis) #[29, 2, 3, 'k']
print(tup1) #'tuple' object does not support item assignment

"""
tuple cannot change data

"""

#การเข้าถึงข้อมูล
tup = (1, "k", True, 3.9)

print(tup[3]) #3.9
print(tup[0:3]) #(1, 'k', True)
print(tup[1:]) #('k', True, 3.9)
print(tup[:-1]) #(1, 'k', True)

#การแก้ไขข้อมูล

tup1 = tuple((1, 2, 3, 4))
#tuple => List
lis = list(tup1)
print(lis) #[1, 2, 3, 4]
lis[0] = "bangkok"
print(lis) #['bangkok', 2, 3, 4]
tup1 = tuple(lis)
print(tup1) #('bangkok', 2, 3, 4)
print(type(tup1)) #<class 'tuple'>