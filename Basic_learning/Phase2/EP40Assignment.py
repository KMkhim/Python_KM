#find max min , input num into list
number = []
while(True) :
    num = int(input("number : "))
    if(num < 0):
        break
    number.append(num)
    

print("min is : " , min(number))
print("max is : " , max(number))