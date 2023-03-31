class Car:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

Honda = Car()
car_name = input("car name: ")
Honda.setName(car_name)
print(f"Honda car name: {Honda.getName()}")