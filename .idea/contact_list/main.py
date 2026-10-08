from pythonclassminiprojects.contact_list.module import *

while True:
    option = show_menu()
    print("______________")

    match option:
        case 1:
            contact = get_contact_info()
            if search_by_phone(contact_list,contact['number']):
                print("!!!Error: contact is already exist!!!",contact)
                print("________________________")
            else:
                contact_list.append(contact)
                print("_________________________")
                print("info: new contact added")
                print("_________________________")
        case 2:
            print_contact_list(contact_list)
        case 3:
            number = int(input("enter your phone number: "))
            result = search_by_phone(contact_list,number)
            print("_____________________________")
            if result:
                print("contact found : ",result)
            else:
                print("contact not found!!!")

        case 4:
            break
        case _:
            ("!!!Error: invalid choice!!!")
            print("________________________")

