import car

class CarShop:
    def __init__(self):
        self.cars = []
        print('Created new Car Shop')
    
    def addNewCar(self,Car):
        self.cars.append(Car)
    
    def showAllCars(self):
        for item in self.cars:
            print(item.serial_number)

MollerAuto = CarShop()

c1 = car.Car("Volvo","S80",2018,2200)
c2 = car.Car("Toyota","Yaris",2015,1500)

MollerAuto.addNewCar(c1)
MollerAuto.addNewCar(c2)

MollerAuto.showAllCars()