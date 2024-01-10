#หาค่าเลขยกกำลัง

number = [1, 2, 3, 4, 5, 6, 7]

#ปกติ    
for i in range(len(number)) :
    number[i] = number[i]**2
print(number) #[1, 4, 9, 16, 25, 36, 49]

#ลดรูป
number = [1, 2, 3, 4, 5, 6, 7]
number = [ i*i for i in number]
print(number) #[1, 4, 9, 16, 25, 36, 49]
