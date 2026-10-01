# برنامه ای بنویسید که تا وقتی عدد صفر وارد نشده عدد بگیرد و تعداد اعداد منفی و مثبت را چاپ کند

num = None
c_negative = 0
c_positive = 0

while num !=0:
    num = int(input("enter number : "))

    if num == 0:
        print("wrong number")
    else:
        if num >0:
            c_positive = c_positive + 1
        else :
            c_negative = c_negative + 1

        print("positive",c_positive)
        print("negative",c_negative)