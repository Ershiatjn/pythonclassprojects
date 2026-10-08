lesson_list = [
    {"name": "Python", "unit": 3, "teacher": "Ali"},
    {"name": "Java", "unit": 2, "teacher": "Reza"},
    {"name": "C Sharp", "unit": 4, "teacher": "Ahmad"},
    {"name": "Network", "unit": 3, "teacher": "Mohammad"},
    {"name": "Database", "unit": 2, "teacher": "Hassan"}
]


student_lesson_list = [
    lesson_list[0],
    lesson_list[2]
]


def sort_by_teacher(lessons):

    result = sorted(
        lessons,
        key=lambda lesson: lesson["teacher"]
    )

    return result


def sort_by_unit(lessons):

    result = sorted(
        lessons,
        key=lambda lesson: lesson["unit"]
    )

    return result