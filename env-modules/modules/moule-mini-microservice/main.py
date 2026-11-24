from add_to_cart import add_to_cart
from show_products import show_products
from calculate_total import calculate_total
from make_payment import make_payment
from register_customer import register_customer

def main():
    print("=== MINI E-COMMERCE APPLICATION ===")

    customer = register_customer("Veera")
    products = show_products()

    cart = []
    cart.append(add_to_cart(products, "Laptop", 1))
    cart.append(add_to_cart(products, "Headphones", 2))

    total = calculate_total(cart)
    make_payment(customer, total)
# Main Guard / Entry Point
if __name__ == "__main__":
    main()

#if __name__ == "__main__":
    #main()
#This is called the Main Guard or Entry Point Check in Python.
#__name__ is a special built-in variable in Python
# When you run a Python file directly, Python automatically sets its __name__ value to "__main__"
# main()

# If the condition is True, Python calls the main() function.
    
#If another Python file imports this one, __name__ gets the file’s module name instead, so the condition is false and main() doesn’t run automatically.