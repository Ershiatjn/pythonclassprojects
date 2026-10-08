# برنامه ای بنویسید که تا زمانی که کاربر عدد مثبت وارد میکند مجموع آنها را محاسبه کند

majmoo = 0
i = 0

while i >= 0 :
    num = int(input("enter number : "))
    if num > -1:
        majmoo = majmoo + num
        print("majmoo: ", majmoo)
    else:
        print("wrong input")
