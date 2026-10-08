from methods import *

phone1 = Apple()
phone1.name = "iphone 8"
phone1.price = 6500000
phone1.voltage = "25amp"
phone1.display = ("Retina")
phone1.serial = 12345

phone2 = Samsung()
phone2.name = "a17"
phone2.price = 5300000
phone2.voltage = "30amp"
phone2.display = ("Amoled")
phone2.serial = 67891

laptop1 = LaptopProduct()
laptop1.name = "hp"
laptop1.price = 17000000
laptop1.voltage = "110amp"
laptop1.cpu = ("intel")
laptop1.ram = ("8Gb")

furniture1 = Furniture()
furniture1.name = "mobl"
furniture1.price = 57838273
furniture1.weight = "75kg"
furniture1.person_count = "8"
furniture1.color = "desert"

print(furniture1)
print(phone1)
print(phone2)
print(laptop1)
