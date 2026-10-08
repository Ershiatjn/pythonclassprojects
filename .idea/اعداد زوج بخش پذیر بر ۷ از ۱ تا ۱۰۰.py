#برنامه ای بنویسید که اعداد زوج بخش پذیر بر ۷ را از ۱ تا ۱۰۰ چاپ کند

numbers = []

for number in range (1,100,1):
    if number % 2 == 0 and number % 7 == 0:
        numbers.append(number)

print("numbers list: ", numbers)
print("__________")
