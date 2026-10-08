course_list=[]
sum_unit = 0

while True :
    course_title= input("Enter course title: ")
    course_unit= int(input("Enter course unit: "))
    course_teacher = input("Enter course teacher: ")
    course_duration = int(input("Enter course duration: "))
    print("____________")

#dictionary
    course = {
        "title": course_title,
        "unit": course_unit,
        "teacher": course_teacher,
        "duration": course_duration
    }

    sum_unit = sum_unit + course_unit

    if sum_unit <= 17:
        course_list.append(course)
        print("course added")
        print("_________")

    elif course_unit == 0 or sum_unit == 0 or course_duration == 0:
        print("wrong unit or duration input , please try again")
        continue

    else:
        print("unit max reached : ", sum_unit)
        print("___________")
        break

for course in course_list:
    print(f'course name: {course["title"]}     by    teacher name: {course["teacher"]}    is    ({course["unit"]}) units    and    ({course["duration"]}) hours')
print("____________")
