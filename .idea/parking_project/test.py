def print_parking_list(parking_list):
    print("Cars in parking lot:")
    for car in parking_list:
        print(f"{car['model']:<10} {car['plate']:10} {car['color']:10} {car['enter_time']:10} ")