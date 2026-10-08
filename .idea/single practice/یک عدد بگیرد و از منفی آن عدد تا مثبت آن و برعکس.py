#برنامه ای بنویسید که از کاربر یک عدد بگیرد و اگر مثبت بود از منفی آن تا مثبت آنرا بنویسد و اگر منفی بود از مثبت آن تا منفی آن را بنویسد


while True:
    num = int(input("enter start number : "))

    if num > 0 :
        for i in range(-num,num+1,1):
            print(i)

    elif num < 0 :
        for i in range(-num,num-1,-1):
            print(i)
            
    else:
        print(0)

