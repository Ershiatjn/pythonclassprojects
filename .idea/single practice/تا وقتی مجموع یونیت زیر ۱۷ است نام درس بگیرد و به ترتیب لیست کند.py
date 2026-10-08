#تمرین کلاسی

sum_unit=0
course_list = []
#حلقه بی نهایت
while sum_unit <=17:
    title = input("enter title: ")
    teacher = input("enter teacher: ")
    duration = int(input("enter duration: "))
    unit = int(input("enter unit: "))
#شرط خروج
    if sum_unit + unit > 17:
        print("total unit is wrong")
        print("________")
        break
#دیکشنری

    if unit > 0 and duration > 0:
        course = {
            "title":title,
            "teacher":teacher,
            "duration":duration,
            "unit":unit,
            }

        course_list.append(course)
        sum_unit = sum_unit + unit
    else:
        print("total unit or duration is wrong")
#چاپ
for course in course_list:
    print(course)
print("Total units:" , sum_unit)
print("________")
