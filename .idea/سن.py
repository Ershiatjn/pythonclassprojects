#برنامه ای بنویسید که از کاربر تاریخ تولد را دریافت کند و سن را محاسبه کند


date_time = 2026

while True:
    birth_year =int(input("enter year of birth: "))
    age = date_time - birth_year

    if age < 0 or age > 100:
        print("not valid")
        continue

    if 0< age < 10:
        print("you are child")

    elif 10 < age < 18:
        print("you are teenager")

    elif 18 <= age < 40:
        print("you are adult")

    elif  40 <= age < 65:
        print("you are old")

    elif 65 <= age:
        print("you are dying")

    print("age: ",age)

