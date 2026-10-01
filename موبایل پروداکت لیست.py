phone_list=[]
phone_total=0
total_price=0

while True:
    brand = str(input("enter phone name: "))
    price = int(input("enter phone price: "))
    quantity = int(input("enter phone quantity: "))

    phone_total = price * quantity

    phone= {
        "phone_brand" : brand,
        "phone_price" :price,
        "phone_quantity" : quantity,
        "phone_total" : phone_total
    }

    total_price = total_price + phone_total
    if total_price <= 1000000:
        phone_list.append(phone)
        print("new phone saved")
        print("__________")
        print("total price : ", total_price)
        print("__________")

    else:
        print("___________")
        print("max price reached : ", total_price)
        print("___________")
        break

for phone in phone_list:
    print(
        f'phone brand: {phone["phone_brand"]}  |  '
        f'phone price: {phone["phone_price"]}  |  '
        f'phone quantity: {phone["phone_quantity"]}  |  '
        f'phone total: {phone["phone_total"]}'
          )
print("__________")