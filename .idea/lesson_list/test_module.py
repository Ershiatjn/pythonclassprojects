from methods import *

lesson1 = Lesson()
lesson1.name = "python"
lesson1.code = "35"
lesson1.teacher = "mesbah"

lesson1.save_lesson(lesson1.name)
lesson1.edit_lesson("algorithm")

print(lesson1)