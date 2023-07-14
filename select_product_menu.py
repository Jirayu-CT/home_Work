total_price = 0
show_bill = []
menu_list_2 = []

system_menu = {
    "ลาบ": 40,"ลาบเถา": 50, "ก้อย": 30, "ซอยจุวัว": 45, "ต้มแซ่บ": 60, "ต้มยำปลา":60, "ต้มยำไก่":60 ,"ข้าวจ้าว":15 ,"ข้าวเหนียว":15,
    "เบียร์ลีโอ": 65,"เบียร์ช้าง":65, "โค้ก":20, "แปปซี่":20
}

menu_list = [
    ["ลาบ", 40], ["ลาบเถา", 50], ["ก้อย", 30], ["ซอยจุวัว", 45], ["ต้มแซ่บ", 60], ["ต้มยำปลา",60], ["ต้มยำไก่",60],
    ["ข้าวจ้าว",15], ["ข้าวเหนียว",15], ["เบียร์ลีโอ", 65], ["เบียร์ช้าง",65], ["โค้ก",20], ["แปปซี่",20]
]


#โปรแกรมหลัก สร้างขึ้นมาอีกเพื่อใว้ วนกลับไปใช้ใหม่
def Mine_program():
    while True:
        select_menu = ""
        select_menu = input("เลือกเมนู: ")

        if select_menu.lower() == "exit":
            print("---END PROGRAM THANK YOU :)---")
            break

        elif select_menu in menu_list_2:
            num_menu = 0
            num_menu = int(input("จำนวนเมนู: "))

            show_bill = []
            show_bill.append([select_menu, num_menu, system_menu[select_menu]])

        else:
            print("ไม่มีเมนูนี้ในรายการ")


        select = input("ต้องการเมนูอีกหรือไม่(y/n): ")
        if select == "n":
            Show_bill()

            muney = 0
            muney = int(input("จำนวนเงินที่จ่าย : "))

            if muney == total_price:
                print("ขอบคุณที่ใช้บริการ โอกาศหน้าเชิญร้านบ่าวเปรมใหม่นะครับ:))")
                break
            elif muney < total_price:
                Money_not_enough()
                print("ขอบคุณที่ใช้บริการ โอกาศหน้าเชิญร้านบ่าวเปรมใหม่นะครับ:))")
                break
            else:
                print("เงินทอน: %s บาท" %(muney-total_price))
                print("ขอบคุณที่ใช้บริการ โอกาศหน้าเชิญร้านบ่าวเปรมใหม่นะครับ:))")
                break


#โชว์บิลรายการที่สั่งซื้อ
def Show_bill():
    total_price = 0
    print("บ่าวเปรม ลาบ-ก้อย-ซอยจุ-ต้มแซ่บ".center(35, "-"))

    for number in range(len(show_bill)):
        print(show_bill[number][0], "*", show_bill[number][1], "--", show_bill[number][2], "บาท")
        total_price += (show_bill[number][1] * show_bill[number][2])

    print("Total : %s Bath" % total_price)


#ถ้าจ่ายเงินน้อยกว่าจะให้วนจ่ายใหม่ จนกว่าจะจ่ายเงิน เกินหรือเท่ากับ ราคารวม
def Money_not_enough():
    while True:
        print("โปรดกรอกจำนวนเงินมากกว่าหรือเท่ากับ %s บาท!!!" %total_price)
        muney = int(input("กรอกจำนวนที่ต้องการจ่าย: "))

        if muney == total_price:
            break
        elif muney > total_price:
            return print("เงินทอน: %s บาท" %(muney-total_price))


#โชว์เมนูรายการที่มีทั้งหมด
def Show_menu():
    print("บ่าวเปรม ลาบ-ก้อย-ซอยจุ-ต้มแซ่บ".center(35, "-"))
    for number in range(len(menu_list)):
        print(menu_list[number][0], menu_list[number][1], "บาท")



Show_menu()
print("กรอก exit เพื่อจบการทำงาน")

for i in range(len(menu_list)):
        menu_list_2.append(menu_list[i][0])


while True:
    select_menu = input("เลือกเมนู: ")

    #เช็คข้อมูลที่รับมาว่าตรงไหม
    if select_menu.lower() == "exit":
        print("---END PROGRAM THANK YOU :)---")
        break
    elif select_menu in menu_list_2:
        num_menu = int(input("จำนวนเมนู: "))
        show_bill.append([select_menu, num_menu, system_menu[select_menu]])
    else:
        print("ไม่มีเมนูนี้ในรายการ")


    select = input("ต้องการเมนูอีกหรือไม่(y/n): ")
    #โชว์บิลเมื่อกด n
    if select == "n":
        Show_bill()

        muney = int(input("จำนวนเงินที่จ่าย: "))
        if muney == total_price:
            print("ขอบคุณที่ใช้บริการ โอกาศหน้าเชิญร้านบ่าวเปรมใหม่นะครับ:))")
            break
        elif muney < total_price:
            Money_not_enough()
            print("ขอบคุณที่ใช้บริการ โอกาศหน้าเชิญร้านบ่าวเปรมใหม่นะครับ:))")
            break
        else:
            print("เงินทอน: %s บาท" %(muney-total_price))
            print("ขอบคุณที่ใช้บริการ โอกาศหน้าเชิญร้านบ่าวเปรมใหม่นะครับ:))")
            break


while True:
    _next = input("ต้องการรายการต่อไปหรือไม่(y/n): ")
    if _next.lower() == "y":
        print("---รายการต่อไป---")
        Show_menu()
        Mine_program()

    elif _next.lower() == "exit" or _next == "n":
        print("---END PROGRAM THANK YOU :)---")
        break