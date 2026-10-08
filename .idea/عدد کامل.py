# برنامه ای بنویسید که عدد بگیرد و مشخص کند عددکامل هست یا نه

while True:
    num = int(input("enter number : "))

    if num == 0:
        break

    sum = 0
    count = 0

    for i in range(1,num,1):
        if num % i == 0:
            print(i)
            count = count + 1
            sum = sum + i


    print("count: ", count)
    print("sum: ", sum)

    if sum == num :
        print("compelete number")
    else:
        print("not compelete number")

    print ("__________")






