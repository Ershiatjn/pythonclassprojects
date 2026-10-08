class Product():
    def __init__ (self):
        self.name = None
        self.price = None

class NonElectronicProduct(Product):
    def __init__ (self):
        self.weight = None

class Furniture(NonElectronicProduct):
    def __init__ (self):
        self.person_count= None
        self.color = None

    def __repr__(self):
        return f"furniture Saved-> name:{self.name} | price:{self.price} | weight:{self.weight} | person count:{self.person_count} | color:{self.color}"

class ElectronicProduct(Product):
    def __init__ (self):
        self.voltage = None

class LaptopProduct(ElectronicProduct):
    def __init__(self):
        self.ram = None
        self.cpu = None

    def __repr__(self):
        return f"laptop Saved->  name:{self.name} | price:{self.price} | voltage:{self.voltage} | ram:{self.ram} | cpu:{self.cpu}"

class MobileProduct(ElectronicProduct):
    def __init__ (self):
        self.display = None

class Samsung(MobileProduct):
    def __init__ (self):
        self.serial = None

    def __repr__(self):
        return f"Samsung Phone Saved-> name:{self.name} | price:{self.price} | voltage:{self.voltage} | display:{self.display} | serial number:{self.serial}"

class Apple(MobileProduct):
    def __init__ (self):
        self.serial = None

    def __repr__(self):
        return f"Apple Phone Saved-> name:{self.name} | price:{self.price} | voltage:{self.voltage} | display:{self.display} | serial number:{self.serial}"




