total_price = 100



def Money_not_enough():
    while True:
        print("โปรดกรอกจำนวนเงินมากกว่าหรือเท่ากับ %s บาท!!!" %total_price)
        muney = int(input("กรอกจำนวนที่ต้องการจ่าย: "))
        if muney == total_price:
            break
        elif muney > total_price:
            return print("เงินทอน: %s บาท" %(muney-total_price))


muney = int(input("Muney :"))
if muney == total_price:
    print("ขอบคุณที่ใช้บริการ โอกาศหน้าเชิญร้านบ่าวเปรมใหม่นะครับ:))")
elif muney < total_price:
    Money_not_enough()
    print("ขอบคุณที่ใช้บริการ โอกาศหน้าเชิญร้านบ่าวเปรมใหม่นะครับ:))")
else:
    print("เงินทอน: %s บาท" %(muney-total_price))
    print("ขอบคุณที่ใช้บริการ โอกาศหน้าเชิญร้านบ่าวเปรมใหม่นะครับ:))")