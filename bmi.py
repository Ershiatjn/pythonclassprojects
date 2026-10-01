#برنامه ای بنویسید ک قد و وزن کاربر را دریافت کند و bmi را محاسبه کند

while True:
    height = int(input("enter height: "))
    weight = int(input("enter weight: "))
    bmi = weight / ((height/100)**2)

    print(round(bmi,2))


