#แปลง พ.ศ เป็น ค.ศ.
#แปลง ค.ศ.เป็น พ.ศ
choice = int(input ("พ.ศ => ค.ศ. กด (1) // ค.ศ. => พ.ศ กด (2) "))
if( choice == 1) :
    num = int(input("พ.ศ. : "))
    print("ค.ศ. : " , num - 543)
else :
    num = int(input("ค.ศ. : "))
    print("พ.ศ. : " , num + 543)