#برنامه ای بنویسید که تا زمانی که کاربر عدد مثبت وارد میکند مجموع آنها را محاسبه کند

sum_num = 0
num  = 0

while True:
    if num >= 0:
        num = int(input("enter number : "))
        majmoo = majmoo + num
        print(sum_num)
    if num <0:
        break

    print(sum_num)