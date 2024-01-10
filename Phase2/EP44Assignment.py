#จับคู่คำ

"""
Hi , Hello
khim , prawta

=> hi khim, hi prawta , Hello khim , Hello prawta
"""

greeting = ["Hi" , "Hello" , "Goodbye"]
people = ["khim", "prawta"]
k = len(greeting) * len(people)

#1
output = []
for i in range(len(greeting)) :
    for j in range(len(people)) :
            output.append(greeting[i] + " " + people[j])
print(output)
#['Hi khim', 'Hi prawta', 'Hello khim', 'Hello prawta', 'Goodbye khim', 'Goodbye prawta']

#2
output = []
for x in greeting :
      for y in people :
            output.append(x+ " " +y)
print(output)#['Hi khim', 'Hi prawta', 'Hello khim', 'Hello prawta', 'Goodbye khim', 'Goodbye prawta']  

#3
output = []
output = [x + " " + y for x in greeting for y in people]
print(output)#['Hi khim', 'Hi prawta', 'Hello khim', 'Hello prawta', 'Goodbye khim', 'Goodbye prawta']

"""
fruit = mango , papaya , banana
price = 50 ,20 ,15

"""
fruit = ["mango" , "papaya" , "banana"]
price = ["50" , "20" , "15"]

for x,y in zip(fruit, price):
      print("สินค้า : " , x , " ราคา : " , y)

# สินค้า :  mango  ราคา :  50
# สินค้า :  papaya  ราคา :  20
# สินค้า :  banana  ราคา :  15
      
for x,y in zip(fruit, price[::-1]):
      print("สินค้า : " , x , " ราคา : " , y)
# สินค้า :  mango  ราคา :  15
# สินค้า :  papaya  ราคา :  20
# สินค้า :  banana  ราคา :  50