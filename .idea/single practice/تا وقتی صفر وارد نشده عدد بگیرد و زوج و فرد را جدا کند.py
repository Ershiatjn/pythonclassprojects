#برنامه ای بنویسید که تا وقتی صفر وارد نشده عدد بگیرد و اعداد زوج و فرد را جدا کند

odd_numbers = []
even_numbers = []

while True:
    num = int(input("enter number: "))

    if num == 0:
        print("finished")
        print("_________")
        break

    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 2 != 0:
        odd_numbers.append(num)

    else:
        print("wrong input")
        print("_________")

print("even_numbers: ", even_numbers)
print("odd_numbers: ", odd_numbers)

