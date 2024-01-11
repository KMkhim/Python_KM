#union
str1 = {"1", "2", "3", "4"}
str2 = {"0", "7", "2"}

allStr = str1.union(str2)
print(allStr) #{'7', '4', '1', '3', '0', '2'}


str1 = {"1", "2", "3", "4"}
str2 = {"0", "7", "2"}
str1.update(str2)
print(str1) #{'0', '7', '4', '1', '3', '2'}

# .copy()
str1 = {"1", "2", "3", "4"}

str3 = str1.copy()
print(str3) #{'2', '1', '3', '4'}

# .difference()
num1 = {"1", "2", "3"}
num2 = {"1", "3"}

num3 = num1.difference(num2) #เก็บแยกไว้ที่ num3
print(num3) #{'2'}

num1.difference_update(num2) #เก็บไว้ที่ num1
print(num1) #{'2'}


# .intersection()
num1 = {"1", "2", "3"}
num2 = {"1", "3"}

num4 = num1.intersection(num2) #เก็บแยกไว้ที่ num4
print(num4) #{'1', '3'}

num1.intersection_update(num2) #เก็บไว้ที่ num1
print(num1) #{'1', '3'}

# subset
charac = {"A", "B", "C", "D"}
charac2 = {"A", "B"}

print(charac2.issubset(charac)) #True

#min/max
number = {"1", "2", "3", "4", "5"}
print(min(number)) #1
print(max(number)) #5

