# برنامه ای بنویسید که میانگین اعداد فرد سه رقمی را محاسبه کند

total = 0
count = 0

for i in range(101,1000,2):
    count= count + 1
    total = total + i
    print(i)

average = total / count

print("count: ", count)
print("total: ", total)
print("average: ", average)