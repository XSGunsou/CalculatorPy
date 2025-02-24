print("Calculator V1.0")

while True:
    print("เลือกวิธีการคำนวณ:")
    print("1. บวก")
    print("2. ลบ")
    print("3. คูณ")
    print("4. หาร")
    print("5. ออกจากโปรแกรม")

    choice = input("เลือกวิธีการคำนวณ (1/2/3/4/5): ")

    if choice == "5":
        print("ขอบคุณที่ใช้โปรแกรม!")
        break

    num1 = float(input("ใส่ตัวเลขที่ 1: "))
    num2 = float(input("ใส่ตัวเลขที่ 2: "))

    if choice == "1":
        print("ผลลัพธ์:", num1 + num2)
    elif choice == "2":
        print("ผลลัพธ์:", num1 - num2)
    elif choice == "3":
        print("ผลลัพธ์:", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("ไม่สามารถหารด้วย 0")
        else:
            print("ผลลัพธ์:", num1 / num2)
    else:
        print("ไม่มีวิธีการคำนวณนั้นน่ะ")

