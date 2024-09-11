'''
oxoxoxox
xoxoxoxo
oxoxoxox
xoxoxoxo
oxoxoxox
xoxoxoxo
oxoxoxox
xoxoxoxo
'''

for i in range(8) :
    for j in range(8) :
        if ( i % 2 == 0 and j % 2 == 0) :
            print('o' , end= '')
        elif(i % 2 == 0 and j % 2 != 0) :
            print('x' , end= '')

        if ( i % 2 != 0 and j % 2 == 0) :
            print('x' , end= '')
        elif(i % 2 != 0 and j % 2 != 0) :
            print('o' , end= '')   
    print("")

print("")

for i in range(8) :
    for j in range(8) :
        if( (i + j) % 2 == 0) :
            print('o' , end= '')
        else :
            print('x' , end= '')
    print("")
