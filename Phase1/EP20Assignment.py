#exchange money
#2000 => 1000 ==> 2
#1500 => 1000(1) , 500(1) 
#1800 ==>1000(1), 500(1) , 100(3)
# 100 =>  50(2)

money = int(input("input your money : "))

#วิธีเรา
if(money >=1000) :
    count1000 = int(money / 1000)
    money = money - count1000*1000
    print("1000 " , count1000 , "ใบ")
if(money >= 500) :
    count500 = int(money / 500)
    money = money - count500*500
    print("500 " , count500, "ใบ")
if(money >= 100) :
    count100 = int(money / 100)
    money = money - count100*100
    print("100 ", count100 , "ใบ")
if(money >= 50) :
    count50 = int(money / 50)
    money = money - count50*50
    print("50 ", count50 , "ใบ")
if(money >= 20) :
    count20 = int(money / 20)
    money = money - count20*20
    print("20 ", count20 , "ใบ")

print("เงินที่เหลือ " , money)


#วิธีจาร

# if(money >=1000) :
#     print("1000 " , money//1000 , "ใบ")
#     money = money % 1000
    
# if(money >= 500) :
#     print("500 " , money // 500, "ใบ")
#     money = money % 500
    
# if(money >= 100) :
#     print("100 ",money // 100 , "ใบ")
#     money = money % 100
    
# if(money >= 50) :
#     print("50 ", count50 , "ใบ")
#     money = money % 100

# print("เงินที่เหลือ " , money)









