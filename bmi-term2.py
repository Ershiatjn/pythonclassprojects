#محاسبه bmi
while True :
    weight = int(input("Enter your weight: "))
    height = int(input("Enter your height: "))

    bmi = weight / ((height/100)**2)
    print("your bmi : ", round(bmi ,2))

    if 0< bmi < 18.5 :
        print("your bmi is low")
    if 18.5 < bmi < 30 :
        print("your bmi is normal")
    elif 30 < bmi :
        print("your bmi is overweight")

    print("_________")