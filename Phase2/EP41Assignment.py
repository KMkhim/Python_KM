#Assignment find group odd and even

number = []
odd = []
even = []

while(True) :
    num = int(input("input number : "))
    if(num < 0):
        break
    number.append(num)

for i in number :
    if( i % 2 == 0) :
        even.append(i)
    else :
        odd.append(i)
print("odd : " , odd)
print("even : " , even)

