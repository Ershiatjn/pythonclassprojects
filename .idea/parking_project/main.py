from pythonclassminiprojects.parking_project.module import *

while True:
    option = show_menu()
    print("___________________")

    match option:
        case 1:
            car = get_car_info()
            if find_car(parking_list, car['plate']):
                print("___________________________________________")
                print("!!!Error Car is already in the parking!!!")
            else:
                parking_list.append(car)
                print("___________________________________________")
                print("info : car added to parking")
        case 2:
            print_parking_list(parking_list)
        case 3:
            plate = int(input("Enter plate number for search: "))
            result= find_car(parking_list, plate)
            if result:
                print("car found: ",result)
            else:
                print("car not found!!!")
        case 4:
            break
        case _:
            print("Error: invalid option")

    print("___________________")