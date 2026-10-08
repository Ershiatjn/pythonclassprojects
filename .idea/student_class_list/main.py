from university_module import *


print("Selected Lessons:")
print(student_lesson_list)


result = sort_by_teacher(student_lesson_list)

print()
print("Sort By Teacher:")
print(result)


result = sort_by_unit(student_lesson_list)

print()
print("Sort By Unit:")
print(result)