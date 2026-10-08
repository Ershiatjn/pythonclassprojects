contact_list=[]

def show_menu():
    print("1. Add new contact")
    print("2. contact list")
    print("3. search contacts")
    print("4. Exit")
    print("______________")

    option = int(input("Enter your choice: "))
    return option

def get_contact_info():
    name = str(input("Enter your name: "))
    last_name = str(input("Enter your last name: "))
    number = int(input("Enter your number: "))
    description = str(input("Enter your description: "))

    return {
        "name":name,
        "last name":last_name,
        "number":number,
        "description":description
    }


def print_contact_list(contact_list):
    print("your contact list: ")
    print("____________________")
    for contact in contact_list:
        print(f"{contact['name']} | {contact['last name']} | {contact['number']} | {contact['description']}")


def search_by_phone(contact_list,number):
    for contact in contact_list:
        if contact['number']== number:
            return contact


