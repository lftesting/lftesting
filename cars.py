class Car:
    def __init__(self, car_id, category, model, price_per_day, available_quantity):
        self.car_id = car_id
        self.category = category
        self.model = model
        self.price_per_day = price_per_day
        self.available_quantity = available_quantity

    def is_available(self):
        self.available_quantity > 0

    def isnot_unavailable(self):
        self.available_quantity = 0
    
