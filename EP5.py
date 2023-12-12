#rules name

'''
1.ใส่ตัวเลข ตัวอักษร เครื่องหมาย
2.ห้ามขึ้นต้นด้วยตัวเลขและสัญลักษณ์พิเศษ  ยกเว้น _
    ex @a = 10  , &a
    ex _a = 10 can do it
3.ห้ามซ้ำกับคียเวิร์ด keyword
    ex. False , Class , def , if , ...
4. case sensitive
'''

#case sensitive
name = "A"
NAME = "B"

print(name)
print(NAME)

a = 10
x = "Korbun"
#if ไม่ได้    _if ใช้ได้
_if = "khim"
print(_if)
