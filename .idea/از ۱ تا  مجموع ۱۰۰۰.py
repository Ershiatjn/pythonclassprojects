# برنامه ای بنویسید که مشخص کند از ۱ تا چند را جمع کنیم تا مجموع آن ۱۰۰۰ شود

target= 1000
total = 0
i = 0

while total < target :
    i = i + 1
    total = total + i
    print(i)
    print("________")


    if total == target:
        print("total: ", total)
else :
        print("امکان پذیر نیست")
