# برنامه ای بنویسید که تا وقتی عدد صفر وارد نشده عدد بگیرد و تعداد اعداد منفی و مثبت را چاپ کند

list_mosbat= []
list_manfi= []

while True:
    num = int(input("enter number: "))

    if num == 0:
        print("program ended")
        break

    elif num > 0 :
        list_mosbat.append(num)
        list_mosbat.sort()

    elif num < 0:
        list_manfi.append(num)
        list_manfi.sort()


    print ("list_mosbat: ", list_mosbat)
    print("count_mosbat: ", len(list_mosbat))
    print ("list_manfi: ", list_manfi)
    print ("count_manfi:", len(list_manfi))
    print ("_________")