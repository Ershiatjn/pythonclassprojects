parking_list = []

def show_menu():
    print("Welcome to Parking Project")
    print("1. Add a Car to parking lot")
    print("2. View all parking lots")
    print("3.search car by plate")
    print("4.exit")
    print("________________________")

    option = int(input("Enter your choice: "))
    return option

def get_car_info():
    model = input("Enter car model: ")
    plate = int(input("Enter plate number: "))
    color = input("Enter car color: ")
    enter_time = int(input("Enter car enter time: "))
    return {""
            "model": model,
            "plate": plate,
            "color": color,
            "enter time": enter_time
            }

def print_parking_list(parking_list):
    print("Cars in parking lot:")
    for car in parking_list:
        print(f"|     {car['model']}     |     {car['plate']}     |     {car['color']}     |     {car['enter time']}     |")

def find_car(parking_list,plate):
    for car in parking_list:
        if car['plate'] == plate:
            return car