
#อนุกรม 1+2+3+...+n

i = int(input("i : "))
n = int(input("n : "))
sum = 0


while (i <= n) :
    sum = sum + i
    i+=1
print("sum is : " ,sum)
print("average is : " , sum / n )