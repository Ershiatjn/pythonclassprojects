#برنامه ای بنویسید که تا وقتی کاربر اکزیت وارد نکرده اسم بگیرد و به ترتیب حروف الفبا چاپ کند

names = []

while True:
    name = input("enter your name: ")

    if name == "exit":
        print("list finished")
        print("_________")
        break

    names.append(name)
    names.sort()

print("name list :",names)