'''
input = 10

1
12
123
1234
.
.
.
12345678910

'''
num = int(input("num : "))

for i in range (1 , num + 1 , 1) :
    for j in range(1, i + 1, 1) :
        print(j , end='')
    print("")
