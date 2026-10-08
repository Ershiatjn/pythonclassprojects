#برنامه ای بنویسید که میانگین اعداد سه رقمی بخش پذیر بر ۷ را چاپ کند

total = 0
count = 0

for i in range (100,1000,1):
    if i % 2 == 0 and i % 7 ==0:
        total = total + i
        count = count + 1

average =total/count

print("avarage: ", average)