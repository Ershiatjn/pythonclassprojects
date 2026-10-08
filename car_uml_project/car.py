class Car:
    def __init__(self, name, color, plate):
        self.__name = name
        self.__color = color
        self.__plate = plate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("name must be a string")
        self.__name = new_name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError("color must be a string")
        self.__color = new_color

    @property
    def plate(self):
        return self.__plate

    @plate.setter
    def plate(self, new_plate):
        if not isinstance(new_plate, str):
            raise TypeError("plate must be a string")
        self.__plate = new_plate