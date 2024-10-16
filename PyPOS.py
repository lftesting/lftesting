from products import products

sales = []

def main():
    while True:
        print("\n--- POS System ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Process Sale")
        print("4. Sales Report")
        print("5. Inventory Report")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            process_sale()
        elif choice == "4":
            sales_report()
        elif choice == "5":
            inventory_report()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


def sales_report():
    print("\nSales Report:")
    print("Total sales:", len(sales))
    total_revenue = sum(sale["total"] for sale in sales)
    print(f"Total revenue: ${total_revenue:.2f}")

def process_sale():
    cart = []
    total = 0
    while True:
        add = input("Enter Product ID or 'done' to finish: ").lower().strip()
        if add == "done":
            break
        if add in products:
            quantity = int(input("Enter quantity: "))
            if quantity <= products[add]["stock"]:
                price = products[add]["price"] * quantity
                total += price
                cart.append((add, quantity, price))
                print(f"Added {quantity} {products[add]["name"]} to your cart. Total: ${total:.2f}.")
            else:
                print("Not enough stock.")
        else:
            print("Invalid product. Please try again.")

    print("\nFinalizing Sale:")
    print("Product  | Quantity | Price")
    print("---------------------------")
    for item in cart:
        print(f"{products[item[0]]['name']} | {item[1]} | ${item[2]:.2f}")
        products[item[0]]['stock'] -= item[1]  

    print(f"\nTotal amount due: ${total:.2f}")
    sales.append({"cart": cart, "total": total})
    print("Sale completed!\n")


def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Stock Quantity: "))
    
    products[product_id] = {"name": name, "price": price, "stock": stock}
    print(f"Product {name} added successfully!")

def display_products():
    print("\nAvailable Products:")
    print("ID  | Name   | Price | Stock")
    print("-----------------------------")
    for product_id, details in products.items():
        print(f"{product_id} | {details['name']} | ${details['price']:.2f} | {details['stock']}")


def inventory_report():
    print("\nInventory Report:")
    display_products()


if __name__ == "__main__":
    main()
