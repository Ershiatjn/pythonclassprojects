product_list = []

def show_menu():
    print("1) Add Product")
    print("2) Show Products")
    print("3) Total")
    print("4) Exit")
    return int(input("Enter your choice: "))

def get_product():
    name = input("Name : ")
    quantity = int(input("Quantity : "))
    price = int(input("Price : "))
    description = input("Description : ")
    total = quantity * price
    return {"name": name, "quantity": quantity, "price": price, "total" : total, "description": description}

def calculate_total(order_list):
    total = 0
    for product in order_list:
        total = total + product["total"]
    return total

def print_product_list(product_list):
    print("Product List")
    for product in product_list:
        print(f"{product['name']:10} {product['quantity']:3} * {product['price']:8}")
