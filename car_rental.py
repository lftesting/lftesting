# CAR RENTAL MANAGEMENT SYSTEM - EARLY STAGES - IN PROCESS

import cars
from cars import Car

cars = [Car(1, "Basic", "VK Golf", 50, 10),
            Car(2, "Intermediate", "VK Passat", 80, 5),
            Car(3, "Luxury", "Audi A8", 150, 3),
            Car(4, "Family", "VK Touran", 100, 5)]


def main():
    selection = display_options(cars)
    if 1 <= selection <= 4:
        selected_car = cars[selection - 1]
        if is_available(selected_car):
            days = int(input("Days of hire: "))
            price = calculate_price(selected_car.price_per_day, days)
            print(f"Final price: ${price:.2f}")
        else:
            print("Selected car is not available")
    else:
        print("Invalid selection")
    

def function_1():
    ...

def calculate_price(price_per_day, days):
    return price_per_day * days
    


def is_available(car):
    if car.available_quantity > 0:
        car.available_quantity -= 1
        return True
    else:
        print("The selected car is not available")

def display_options(cars):
    for i, car in enumerate(cars,1):
        print(f"{i}. {car.category}: {car.model}.")
    return int(input("Select the car you want: "))

if __name__ == "__main__":
    main()

