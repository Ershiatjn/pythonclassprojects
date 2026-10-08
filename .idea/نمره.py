# برنامه ای بنویسید که از کاربر نمره دریافت کند و قبولی و مردود را نشان دهد

while True:
    score = float(input("enter your score:"))

    if score < 0 or score > 20:
        print("not a valid score")
        continue

    if 0 <= score <= 10:
        print("مردود")

    elif 10 <= score <= 12:
        print("مشروط")

    elif 12 <= score <= 18:
        print("قبول")

    elif 18 <= score <= 20:
        print('ممتاز')


