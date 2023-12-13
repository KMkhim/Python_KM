#Type Conversion

x = 10
y = 3.14
z = "20"

print("type x " ,type(x))
print("type y " , type(y))
print("type z " , type(z))

#sum int and float 
sum = x + y

#string to int
# "20" => 20
sum2 = x + int(z)

#int to string
str1 = str(x) + z 

#string to float
float(z)

#float to string
str(y)

#int <==> float
int(y)
float(x)

print("sum is %f" ,sum , type(sum))
print("sum2 is %f" ,sum2 , type(sum2))
print("string is %s" , str1 , type(str) ,"\n")

print("type z " , type(z))
print(float(z) , "type of  float(z) " , type(float(z)),"\n")
print("type y " , type(y))
print(str(y), "type of  str(y) " , type(str(y)))
print(int(y) , "type of  int(y) " , type(int(y)),"\n")
print("type x " ,type(x))
print(float(x), "type of  float(x) " , type(float(x)),"\n")