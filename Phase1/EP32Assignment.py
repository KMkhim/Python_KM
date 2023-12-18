#max/min

max, min, a = 0, 0, 0
while True:
    num = int(input("number  : ")) #ใช้ num เป็นตัวจำ
    if (num < 0) :
        break 
    if ( a == 0) :
        min = num
        a+=1
    if (max < num) :
        max = num
    if (min >= num) :
        min = num
    
        
print("max : " + str(max) + " min : " + str(min) )
    
    
#เพราะใช้ min เป็นตัวจำ ทำให้ป้อน ค่า -1 min = -1 
'''
max, min, a = 0, 0, 0
while True:
    min = int(input("number  : "))
    if (min < 0) :
        break
    #min = num
    if (max < min) :
        a = max
        max = min
        min = a
print("max : " + str(max) + " min : " + str(min) )
    
'''  