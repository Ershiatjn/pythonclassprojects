#برنامه ای بنویسید که طول و عرض یک زمین را دریافت کند و بر اساس  مساحت پاسخ دهد


while True:
    length = float(input("Enter Length: "))
    width = float(input("Enter width: "))

    if length < 0 or width < 0 :
        print("wrong input")
        break
    else:
        area = length * width
        print("area is : ", area)

#permits
    if 0 < area <= 100:
        print("no permit required")
    elif 100 <area <= 200 :
        print("permit required")
    elif 200 < area :
        print("permit will not be issued")
    else :
        print("wrong area size")

    print("______")