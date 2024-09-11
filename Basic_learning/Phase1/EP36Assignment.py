'''
xxxx
x  x
x  x
xxxx
'''

num = int(input("num : "))

for i in range (num ) :
    for j in range (num ) :
        if( i == 0 or i == num - 1) :
            print('x' , end='')
        else :
            if(j == 0 or j == num - 1) :
                print("x" , end='')
            else :
                print(" " , end='')
    print("")
