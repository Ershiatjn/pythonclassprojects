#برنامه ای بنویسید که از کاربر ۲ عدد دریافت کند و از شروع تا پایان را چاپ کند

while True:
    start = int(input("enter start number : "))
    end = int(input("enter end number : "))

    if start > end:
        step = -1
    else:
        step = 1

    for i in range(start, end + step , step):
        print(i)
