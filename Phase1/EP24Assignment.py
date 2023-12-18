#fahrenheit_to_celsius
#celsius_to_fahrenheit

#c = (f-32)*5/9
#f = (c*9/5) +32

num = input(" 1 : for change f => c | 2 : for change c => f : ")
if(num == '1') :
    temp = float(input("fahrenheit : "))
    temp = (temp - 32)*( 5 / 9)
    text = "celsius : {0:.2f}"
    print(text.format(temp))
else :
    temp = float(input("celsius : "))
    temp = (temp * ( 9 / 5)) + 32
    print("fahrenheit : ", temp)



temp = input("temperature(degree) : ") #45C

degree = int(temp[:-1]) #45
unit = temp[-1].upper() #C

if (unit == 'C') :
    degree = (degree * ( 9 / 5)) + 32
    print("temp is : " , degree, "F")
elif (unit == 'F') :
    degree = (degree - 32)*( 5 / 9)
    print("temp is : " , degree, "C")
else :
    print("not f or c")

