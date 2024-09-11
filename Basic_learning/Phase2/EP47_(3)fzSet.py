#frozent set
#แก้ไขข้อมูลไม่ได้


num = frozenset(["1", "2", "3"])
#num.add("55") #'frozenset' object has no attribute 'add'
#num.discard("1") #'frozenset' object has no attribute 'discard'
#num.append("8")  'frozenset' object has no attribute 'append'

lis = list(num)
print("before append" ,lis) #['2', '1', '3']
lis.append("5")
print("after append" ,lis) #['2', '1', '3', '5']

num = frozenset(lis) 
#num = list  แบบนี้ไม่ได้ มันคือ num frozen จะกลายเป็น List
#num.append("8") # 'frozenset' object has no attribute 'append'


for item in num :
    print(item)

'''
output
1
2
3
'''