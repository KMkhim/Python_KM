#function input 

fname = input("insert your name : ")
Iname = input("insert your surname : ")

print("your name is " + fname)
print("your type name is " , type(fname))
print("your surname is " + Iname)
print("your type surname is " , type(Iname), "\n")

#input
x = input("number one : ")
y = input("number two : ")
#process
z = x + y 
#output
print("your sum is " + z)
print("your type sum is " , type(z), "\n")

#process
z = int(x) + int(y) 
#output
print("your sum is " + str(z))
print("your type sum is " , type(z), "\n")

#process + output
print("process + output " , int(x) + int(y));


