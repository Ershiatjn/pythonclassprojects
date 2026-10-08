# برنامه ای بنویسید که ۵ نمره دریافت کند و میانگین را چاپ کند

total = 0

for num in range(1,6,1):
    grade = float(input("enter grade:" ))
    total = total + grade

average = total/5
print("average: ",average)