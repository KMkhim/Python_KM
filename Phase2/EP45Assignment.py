#การค้นหาและนับจำนวนตัวอักษรในสมาชิก

message = ["aa", "aab", "cba", "bba", "aba", "cca"]
result = []

for item in message :
    result.append(item.count("a"))
print(result) #[2, 2, 1, 1, 2, 1]