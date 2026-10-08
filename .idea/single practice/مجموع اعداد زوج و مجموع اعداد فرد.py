#برنامه ای بنویسید که از کاربر ۱۰ عدد دریافت کند و مجموع اعداد زوج و مجموع اعداد فرد دریافتی را جداگانه محاسبه کند

odd = 0
even = 0

for i in range(10):
    number = int(input("enter number : "))

    if number % 2 == 0:
        even = even + number
    else:
        odd = odd + number

print("even: ", even)
print("odd: ", odd)