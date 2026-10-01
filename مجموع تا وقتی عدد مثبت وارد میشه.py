# برنامه ای بنویسید که تا وقتی صفر یا منفی وارد نکرده ایم عدد بگیرد و مجموع آنها را نمایش دهد

majmoo = 0

while True :
    num = int(input("enter number : "))

    if num <= 0 :
        print("wrong number")
        continue

    elif num >= 0 :
        majmoo = majmoo + num
        print('majmoo: ', majmoo)
