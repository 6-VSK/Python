class Car:
    car_counter = 0
    def __init__(self, brand, model, year, weight):
        self.brand = brand
        self.model = model
        self.year = year
        self.weight = weight
        self.id = Car.car_counter
        self.serial_number = Car.setSerialNumber(self)
        Car.car_counter += 1
    
    def setSerialNumber(self):
        return f'{self.brand[0]}_{self.model[0]}_{self.year}_{self.id}'
    