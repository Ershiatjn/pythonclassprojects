# برنامه ای بنویسید که تا وقتی کاربر 0 وارد نکرده عدد بگیرد و میانگین اعداد فرد دریافتی را چاپ کند

odd_numbers = []

while True:
    num = int (input("enter number: "))

#دستور خروج
    if num == 0:
        print("end bye")
        break

#دستور ادامه
    if num %2 != 0:
        odd_numbers.append(num)

if len(odd_numbers) > 0 :
    avg_odd = sum(odd_numbers) / len(odd_numbers)

    print("majmoo: ", sum(odd_numbers))
    print ("tedad: ", len(odd_numbers))
    print("avg: ", avg_odd)
    print("----------------")
else :
    print("no odd number")
    print ("----------------")





