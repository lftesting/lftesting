### THIS PROJECT IS FULLY DEVELOPED BUT CODE IS NOT PUBLISHED BECAUSE OF ACADEMIC HONESTY POLICIES. 
### AVAILABLE UPON REQUEST FOR COLLABORATION OR NON ACADEMIC INTERESTS

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

#### REST OF THE CODE AVAILABLE UPON REQUEST. FULLY DEVELOPED PROJECT.
