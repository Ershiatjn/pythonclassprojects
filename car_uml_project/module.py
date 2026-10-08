class Car:
    def __init__(self, name,color,plate):
        self.name = name
        self.color = color
        self.plate = plate

    def name(self):
        return self.__name

    def color(self):
        return self.__color

    def plate(self):
        return self.__plate

    def name(self,name):
        if not isinstance(name,str):
            raise TypeError ("name must be a string")
        self.__name = new_name

    def color(self,color):
        if not isinstance(color,str):
            raise TypeError ("color must be a string")
        self.__color = new_color

    def plate(self,plate):
        if not isinstance(plate,str):
            raise TypeError ("plate must be a string")
        self.__plate = new_plate
