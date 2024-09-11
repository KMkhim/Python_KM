#แม่สูตรคูณ

num = int(input("number : "))

for i in range(1, 13, 1) :
    multi = num*i
    print(num ," * ", i ," = ", multi)

#1-12 for loop
for i in range(1, 13 ,1) :
    for j in range(1, 13, 1) :
        multi = i*j
        print(i ," * ", j ," = ", multi)

#1-12 : while loop 
i = 1
while (i < 13) :
    j = 1
    while(j < 13) :
        multi = i*j
        print(i ," * ", j ," = ", multi)
        j+=1
    i+=1