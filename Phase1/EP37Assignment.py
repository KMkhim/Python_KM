
import random

myrandom = random.randrange(1,7)
#print(myrandom)

while True :
    num = int(input("your ans : "))
    if (num == myrandom) :
        print("correct")
       
    else :
        print("not correct")
        break

print(myrandom)