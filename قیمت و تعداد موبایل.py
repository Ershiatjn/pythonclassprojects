total_price = 0
mobile_list = []

while True:
    mobile_name = input("enter mobile name: ")
    quantity = int(input("enter quantity: "))
    price = float(input("enter price: "))

    mobile_total_price = price * quantity
    total_price = total_price + mobile_total_price

    if 123 < total_price + mobile_total_price < 1000000:
        print ("total price max")
        print("________")
        break

    mobile_dict = {
        "mobile_name": mobile_name,
         "quantity": quantity,
         "price": price,
    }

    mobile_list.append(mobile_dict)
    total_price += mobile_total
    print("mobile_saved")

for mobile_dict in mobile_list:
    print(f'{mobile_dict["mobile_name"]} by {mobile_dict["quantity"]} is {mobile_dict["price"]} USD   ')


print("________")
print("mobile total :",mobile_total)
print("________")
print("total price is :",total_price)
print("________")



