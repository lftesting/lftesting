# implement a program that enables a user to place an order
# prompting one item per line until user inputs "control-d"
# after each item inputted display order total prefixed with a $ sign and formatted to 2 decimals

menu = {
    "Baja Taco":"4.25",
    "Burrito":"7.50",
    "Bowl":"8.50",
    "Nachos":"11.00",
    "Quesadilla":"8.50",
    "Super Burrito":"8.50",
    "Super Quesadilla":"9.50",
    "Taco":"3.00",
    "Tortilla Salad":"8.00"
}

def main():
    final_price = order(print(f"Total price:${final_price:.2f}"))  

def order():
    total_price = 0.0
    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                price = float(menu.get(item))
                total_price += price
                print(f"${total_price:.2f}")
        except KeyError:
                continue
        except EOFError:
                break
               
    

order()
