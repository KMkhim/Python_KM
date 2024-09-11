#การแสดงผลด้วย loop
number = [1, 2, 3, 4, 5, 6]


sum = 0 

for x in number:
    sum += x
    print("สมาชิก :" , x) 
# สมาชิก : 1
# สมาชิก : 2
# สมาชิก : 3
# สมาชิก : 4
# สมาชิก : 5
# สมาชิก : 6
print("sum is : " , sum ) #sum is :  21

#การตรวจสอบข้อมูล

fruit = list(["mango" , "tomato" , "orange"])

if 20 in number :
    print("true")
else : 
    print("false") #false

if "tomato" in fruit:
    print("true")
else : 
    print("false") #true

#นับจำนวนสมาชิก len 
print(len(number)) #6
print(len(fruit)) #3

#len ทำวานร่วมกับ for loop

for i in range(len(fruit)) :
    print(fruit[i])
#or you can write this 
for i in fruit :
    print(i)

#การเพิ่มข้อมูล => append , insert
    #append  ข้อมูลต่อท้าย
    #insert  แทรกข้อมูล

    
# .append("--")   
fruit = list(["mango" , "tomato" , "orange"])

print("before add : " , fruit)
#before add :  ['mango', 'tomato', 'orange']

fruit.append("banana")
fruit.append("melon")

print("after add : " , fruit)
#after add :  ['mango', 'tomato', 'orange', 'banana', 'melon']

# .insert("--")
print("before add : " , fruit)
#before add :  ['mango', 'tomato', 'orange', 'banana', 'melon']

fruit.insert(1, "durian")
print("after add : " , fruit)
#after add :  ['mango', 'durian', 'tomato', 'orange', 'banana', 'melon']


#การลบข้อมูล => remove , pop , del , clear

# .remove("--")
fruit.remove("durian")
print("after remove : " , fruit)
#after remove :  ['mango', 'tomato', 'orange', 'banana', 'melon']

# .pop() เอาข้อมูลสามาชิกตัวล่าสุดออก
fruit.pop()
print("after pop : " , fruit)
#after pop :  ['mango', 'tomato', 'orange', 'banana']

# del List[x]
del fruit[1]
print("after del : " , fruit)
#after del :  ['mango', 'orange', 'banana']

# .clear()  => clear ความจำ
fruit.clear()
print(fruit) #[]

# del List
del fruit #ลบยันตัวแปร
print(fruit) #name 'fruit' is not defined

