def get_person():
    name = input("Name : ")
    family = input("Family Name : ")
    phone = input("Phone Number : ")
    return {"name": name, "family": family, "phone": phone}



person = get_person()
print(person)
