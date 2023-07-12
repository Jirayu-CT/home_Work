a_list =[]
b_list = []
c_list = []
d_list = []
num_List = []

def Check_numbers(num):
    if num < 0:
        a = num
        a_list.append(a)

    elif num > 0 and num <= 101:
        b = num
        b_list.append(b)

    elif num > 101 and num <= 1000:
        c = num
        c_list.append(c)

    elif num > 1000:
        d = num
        d_list.append(d)


def Sum():
    print("---ผลสรุป---")
    num_str = num_List
    print("ผู้ใช้กรอกตัวเลข", ListToString(num_str))

    print("เลขที่น้อยกว่า 0 มี %d ตัวเลข" %(len(a_list)))
    print("เลขที่มากกว่า 0 แต่น้อยกว่าหรือเท่ากับ 101มี %d ตัวเลข" %(len(b_list)))
    print("เลขที่มากกว่า 100 แต่น้อยกว่าหรือเท่ากับมี 1000 มี %d ตัวเลข" %(len(c_list)))
    print("เลขที่มากกว่า 1000 มี %d ตัวเลข" %(len(d_list)))

    print(" Press 'q'for exit this program")


def ListToString(num_str):
    str1 = ""

    for ele in num_str:
        str1 = str1 + ele + " "

    return str1

def while_input():
    while True:
        num = int(input("Press input Number: "))
        num_List.append(str(num))
        Check_numbers(num)

        if num == 0:
            Sum()
            break

print("-----Press 0 To Conclusion-----")
while True:
    num_List = []
    while_input()

    _exit = input()
    if _exit == "q":
        print("END PROGRAME")
        break