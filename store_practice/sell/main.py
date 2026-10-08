from sell.store_module import *

while True:
    option = show_menu()
    print("------------------------------------")

    match option:
        case 1:
            product = get_product()
            if product["total"]  + calculate_total(product_list) < 1000:
                product_list.append(product)
                print("Product Added")
            else:
                print("Cant Buy more than 1000")

        case 2:
            print_product_list(product_list)

        case 3:
            print("Total :", calculate_total(product_list))

        case 4:
            break

        case _:
            print("Invalid option !!!")

    print("------------------------------------")



