from persian_tools import national_id
from persian_tools import phone_number
from persian_tools.bank import card_number
from persian_tools import plate
from persian_tools import bill

while True:
    print("1. Check information")
    print("2. Exit")
    print("______________")

    option = int(input("Enter your choice: "))

    match option:

        case 1:
            national = input("Enter your national ID: ")
            mobile = input("Enter your mobile number: ")
            card = input("Enter your bank card number: ")
            car_plate = input("Enter your car plate: ")

            print("\n========== RESULT ==========")

            # National ID
            if national_id.validate(national):
                print("National ID: Valid")
                print("Place:", national_id.find_place(national))
            else:
                print("National ID: Invalid")

            # Mobile
            if phone_number.validate(mobile):
                print("Mobile: Valid")
                print("Operator:", phone_number.operator_data(mobile))
            else:
                print("Mobile: Invalid")

            # Bank Card
            if card_number.validate(card):
                print("Bank Card: Valid")
                print("Bank:", card_number.bank_data(card))
            else:
                print("Bank Card: Invalid")

            # Car Plate
            if plate.is_valid(car_plate):
                print("Car Plate: Valid")

                plate_info = plate.get_info(car_plate)

                print("Category:", plate_info["category"])
                print("Province:", plate_info["province"])
                print("Type:", plate_info["type"])
            else:
                print("Car Plate: Invalid")

        case 2:
            break

        case _:
            print("!!! Error: invalid choice !!!")