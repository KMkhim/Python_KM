#list, Tuple

lis = ["red" , "purple", "green"]
tup = ("red" , "purple", "green")

print(lis[0]) #red
#print(tup[0.0]) #TypeError: tuple indices must be integers or slices, not float

''' Dictionary  => key ,value '''
''' list , tuple => index , value '''

#การสร้าง dictionary

# name = {key : value, key : value, key : value}
color = {"red" : "สีแดง", "purple" : "สีม่วง" , "black" : "สีดำ" }
print(color["red"]) #สีแดง

# name = dict({key : value, key : value, key : value})
color = dict({"red" : "สีแดง", "purple" : "สีม่วง" , "black" : "สีดำ" })
print(color["black"]) #สีดำ
print(color.get("purple")) #สีม่วง

#name = dict( key = value , key = value)
animals = dict(cat = "แมว", dog = "หมา", cow = "วัว")
print(animals["cat"]) #แมว

#ตั้ง key เป็น boolean
bool = { True : "yes" , False : "No"}
print(bool[True]) #yes

#แก้ไขข้อมูล

animals = dict(cat = "แมว", dog = "หมา", cow = "วัว")
animals["cat"] = "เจ้านาย"
print(animals["cat"]) #เจ้านาย


#เพิ่มข้อมูล

animals.update({"human" : "คน" , "pig" : "หมู"}) 
print(animals) 
#{'cat': 'เจ้านาย', 'dog': 'หมา', 'cow': 'วัว', 'human': 'คน', 'pig': 'หมู'}

#update key ซ้ำ

animals.update({"human" : "ทาส"})
print(animals)
#{'cat': 'เจ้านาย', 'dog': 'หมา', 'cow': 'วัว', 'human': 'ทาส', 'pig': 'หมู'}

#for and dict

for item in animals :
    print(item)
''' 
cat
dog
cow
human
pig'''

for item in animals.values() :
    print(item)
'''
เจ้านาย
หมา
วัว
ทาส
หมู
'''

for item in animals.keys() :
    print(item)
'''
cat
dog
cow
human
pig
'''

for k,v in animals.items() :
    print("key = " , k, "value = " , v)
'''
key =  cat value =  เจ้านาย
key =  dog value =  หมา
key =  cow value =  วัว
key =  human value =  ทาส
key =  pig value =  หมู
'''
#ลบข้อมูล
# .pop("....")
print(animals) 
#{'cat': 'เจ้านาย', 'dog': 'หมา', 'cow': 'วัว', 'human': 'ทาส', 'pig': 'หมู'}

animals.pop("pig")

print(animals)
#{'cat': 'เจ้านาย', 'dog': 'หมา', 'cow': 'วัว', 'human': 'ทาส'}

# .popitem() => เอาตัวสุดท้ายออก
animals.popitem()
print(animals) #{'cat': 'เจ้านาย', 'dog': 'หมา', 'cow': 'วัว'}

# .clear()
animals.clear()
print(animals) #{}

#del dictName

del animals
#print(animals) #NameError: name 'animals' is not defined

#คัดลอกข้อมูล

animals = dict(cat = "แมว", dog = "หมา", cow = "วัว" )

x = animals.copy()
print(x) #{'cat': 'แมว', 'dog': 'หมา', 'cow': 'วัว'}

#dict ซ้อน dict

market = {
    "ร้าน A" : {
        "name" : "เอ", #comma
        "menu" : ["กะเพราไก่" ,"เตี๋ยว"] #List
    } , #comma
    "ร้าน B" : {
        "name" : "บี" , #comma
        "menu" : ["ราดหน้า" , "ข้าวซอย"] #List
    }
}

print(market["ร้าน A"]["menu"]) #['กะเพราไก่', 'เตี๋ยว']

if "เตี๋ยว" in market["ร้าน A"]["menu"] :
    print("True") #True
else : 
    print("False")


