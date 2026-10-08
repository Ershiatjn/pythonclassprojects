from university_module2 import *


while True:

    print()
    print("----- Show Menu -----")
    print("1. Show Available Lessons")
    print("2. Add Lesson")
    print("3. Show Shopping Cart")
    print("4. Exit")
    print("=======================")

    option = input("Enter Option: ")


    # نمایش دروس موجود

    if option == "1":

        result = sort_lessons_by_teacher(lesson_list)

        print()
        print("Sort By Teacher:")
        print(result)


        result = sort_lessons_by_unit(lesson_list)

        print()
        print("Sort By Unit:")
        print(result)


    # اضافه کردن درس

    elif option == "2":

        while True:

            name = input("Enter Lesson Name (exit to menu): ")

            if name.lower() == "exit":
                break

            if name == "":
                print("No Lesson Entered")
                continue


            try:
                unit = int(input("Enter Unit: "))
            except ValueError:
                print("Unit Must Be Number")
                continue


            if unit < 1 or unit > 5:
                print("Unit Must Be Between 1 And 5")
                continue


            teacher = input("Enter Teacher: ")

            if teacher == "":
                print("No Teacher Entered")
                continue


            result = add_lesson(name, unit, teacher)

            print(result)


    # نمایش سبد خرید

    elif option == "3":

        if not student_lesson_list:

            print("No Lesson Selected")

        else:

            # مرتب سازی سبد براساس تعداد واحد

            result = sort_lessons_by_unit(student_lesson_list)

            print()
            print("Shopping Cart - Sort By Unit:")
            print(result)


            # مرتب سازی سبد براساس نام درس

            result = sort_lessons_by_name(student_lesson_list)

            print()
            print("Shopping Cart - Sort By Name:")
            print(result)


            # اضافه کردن شهریه

            result = list(
                map(add_price, result)
            )

            print()
            print("Lessons With Price:")
            print(result)


            # محاسبه مبلغ کل

            total = calculate_total(result)

            print()
            print("Total:", total)

            print("Total In Words:", total_in_words(total))


    # خروج

    elif option == "4":

        print("Goodbye")
        break


    else:

        print("Invalid Option")