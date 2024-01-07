number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fruit = ["mango" , "orange" , "tomato"]

x = []
print(x) #[]

#การคัดลอกข้อมูล  => list1 = list2.copy()

x = fruit.copy()
print(x) #['mango', 'orange', 'tomato']

#การรวมข้อมูล  

#list3 = list1 + list2
allGroup = number + fruit
print(allGroup) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'mango', 'orange', 'tomato']

# .extend()
number.extend(fruit)
print(number) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'mango', 'orange', 'tomato']

#แสดงจำนวนสมาชิก (count)
number = [1, 2, 3, 4, 5, 6, 7, 5, 5, 5]
x = number.count(5)
print(x) #4

