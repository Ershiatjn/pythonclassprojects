class Lesson:
    def __init__ (self):
        self.code = None
        self.name = None
        self.teacher = None

    def __repr__(self):
        return f"Lesson: {self.code}, {self.name}, {self.teacher}"

    def save_lesson(self,name):
        print(name, "saved")

    def edit_lesson(self,edited_name):
        self.name = edited_name
        print("name edited,new name: " , edited_name)

