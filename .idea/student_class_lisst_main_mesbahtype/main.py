from persiantools import digits


Lesson_List = [
    {"name": "Python", "unit": 3, "teacher": "Ali"},
    {"name": "C++", "unit": 5, "teacher": "Reza"},
    {"name": "Csharp", "unit": 3, "teacher": "Mohsen"},
    {"name": "HTML", "unit": 2, "teacher": "Ali"},
    {"name": "Java", "unit": 4, "teacher": "Reza"},
    {"name": "SQL", "unit": 5, "teacher": "Mohsen"}
]


def Check_Lesson(Entered_Lesson):

    result = list(filter(
        lambda x: x["name"].lower() == Entered_Lesson["name"].lower() and
                  x["unit"] == Entered_Lesson["unit"] and
                  x["teacher"].lower() == Entered_Lesson["teacher"].lower(),
        Lesson_List
    ))

    if len(result) > 0:
        return True

    return False


def Select_Lesson(Entered_Lesson, Selected_Lessons):

    if Check_Lesson(Entered_Lesson):

        Entered_Lesson = Add_Price(Entered_Lesson)

        Selected_Lessons.append(Entered_Lesson)

        print("-----------")
        print("Lesson selected")
        print("-----------")

        Show_Selected_Lessons(Selected_Lessons)

    else:

        print("-----------")
        print("Lesson not found, try again")
        print("-----------")


def Add_Price(lesson):

    if lesson["unit"] == 2:
        lesson["price"] = 1000

    elif lesson["unit"] == 3:
        lesson["price"] = 1200

    elif lesson["unit"] == 4:
        lesson["price"] = 1400

    elif lesson["unit"] == 5:
        lesson["price"] = 1600

    return lesson


def Sort_By_Unit(Selected_Lessons):

    return sorted(
        Selected_Lessons,
        key=lambda x: x["unit"]
    )


def Sort_By_Name(Selected_Lessons):

    return sorted(
        Selected_Lessons,
        key=lambda x: x["name"].lower()
    )


def Calculate_Total(Selected_Lessons):

    prices = list(map(
        lambda x: x["price"],
        Selected_Lessons
    ))

    return sum(prices)


def Price_To_Word(price):

    return digits.to_word(price)


def Show_Selected_Lessons(Selected_Lessons):

    print("Shopping Cart:")
    print("-----------")

    for lesson in Selected_Lessons:
        print(lesson)

    Total = Calculate_Total(Selected_Lessons)

    print("-----------")
    print("Total:", Total, "Toman")
    print("Total In Words:", Price_To_Word(Total), "Toman")
    print("-----------")


Selected_Lessons = []


print("Lessons in system:")

for lesson in Lesson_List:
    print(lesson)


print("-----------")


while True:

    print("Main Menu")
    print("1. Select Lesson")
    print("2. Show Selected Lessons")
    print("3. Exit")

    choice = input("Choice: ")

    print("-----------")


    if choice == "1":

        print("Select Lesson")
        print("Enter Exit to finish selecting lessons")
        print("-----------")

        while True:

            name = input("Lesson Name: ")

            if name.lower() == "exit":
                break

            unit = int(input("Unit: "))

            teacher = input("Teacher: ")

            Entered_Lesson = {
                "name": name,
                "unit": unit,
                "teacher": teacher
            }

            Select_Lesson(
                Entered_Lesson,
                Selected_Lessons
            )


    elif choice == "2":

        Show_Selected_Lessons(Selected_Lessons)

        print("Sorted By Unit:")
        print("-----------")

        Result_Unit = Sort_By_Unit(Selected_Lessons)

        for lesson in Result_Unit:
            print(lesson)

        print("-----------")
        print("Sorted By Name:")
        print("-----------")

        Result_Name = Sort_By_Name(Selected_Lessons)

        for lesson in Result_Name:
            print(lesson)

        print("-----------")


    elif choice == "3":

        break


print("-----------")
print("Final Shopping Cart")
print("-----------")

Show_Selected_Lessons(Selected_Lessons)

print("Sorted By Unit:")
print("-----------")

Result_Unit = Sort_By_Unit(Selected_Lessons)

for lesson in Result_Unit:
    print(lesson)

print("-----------")
print("Sorted By Name:")
print("-----------")

Result_Name = Sort_By_Name(Selected_Lessons)

for lesson in Result_Name:
    print(lesson)

print("-----------")
print("Total:", Calculate_Total(Selected_Lessons), "Toman")
print("Total In Words:", Price_To_Word(Calculate_Total(Selected_Lessons)), "Toman")
print("-----------")