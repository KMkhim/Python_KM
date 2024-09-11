#sort string
student = list(["khim", "prawta" , "Andy" ,"andy ", "nick"])
student.sort()
print(student)#['Andy', 'andy ', 'khim', 'nick', 'prawta']

#เรียงสมาชิกจากหลังสุดไปหน้าสุด
student = student[::-1] #['prawta', 'nick', 'khim', 'andy ', 'Andy']
print(student)

student.reverse()
print(student) #['Andy', 'andy ', 'khim', 'nick', 'prawta']