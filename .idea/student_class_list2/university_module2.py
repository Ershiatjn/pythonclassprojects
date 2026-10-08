from persiantools import digits


lesson_list = [
    {"name": "Python", "unit": 3, "teacher": "Ali"},
    {"name": "Java", "unit": 2, "teacher": "Reza"},
    {"name": "C Sharp", "unit": 4, "teacher": "Ahmad"},
    {"name": "Network", "unit": 3, "teacher": "Mohammad"},
    {"name": "Database", "unit": 2, "teacher": "Hassan"}
]


student_lesson_list = []


unit_price = {
    1: 1000,
    2: 1000,
    3: 1200,
    4: 1400,
    5: 1400
}


# اضافه کردن درس

def add_lesson(name, unit, teacher):

    lesson = {
        "name": name,
        "unit": unit,
        "teacher": teacher
    }

    result = list(
        filter(
            lambda lesson_item:
            lesson_item["name"].lower() == lesson["name"].lower()
            and lesson_item["unit"] == lesson["unit"]
            and lesson_item["teacher"].lower() == lesson["teacher"].lower(),
            lesson_list
        )
    )

    if result:

        if result[0] in student_lesson_list:
            return "Lesson Already Selected"

        else:
            student_lesson_list.append(result[0])
            return "Lesson Added"

    else:
        return "Lesson Not Found"


# مرتب سازی دروس براساس استاد

def sort_lessons_by_teacher(lessons):

    result = sorted(
        lessons,
        key=lambda lesson: lesson["teacher"].lower()
    )

    return result


# مرتب سازی دروس براساس تعداد واحد

def sort_lessons_by_unit(lessons):

    result = sorted(
        lessons,
        key=lambda lesson: lesson["unit"]
    )

    return result


# مرتب سازی دروس براساس نام

def sort_lessons_by_name(lessons):

    result = sorted(
        lessons,
        key=lambda lesson: lesson["name"].lower()
    )

    return result


# اضافه کردن شهریه

def add_price(lesson):

    lesson["price"] = unit_price[lesson["unit"]]

    return lesson


# محاسبه مبلغ کل

def calculate_total(lessons):

    total_list = list(
        map(
            lambda lesson: lesson["price"],
            lessons
        )
    )

    total = sum(total_list)

    return total


# تبدیل مبلغ به حروف

def total_in_words(total):

    return digits.to_word(total)