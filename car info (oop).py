class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        proper_name = str(self.year) + " " + self.make.title() + " " + self.model.title()

        return(proper_name)

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " kms on it.")

    def update_odometer(self,mileage):
        if int(mileage) >= int(self.odometer_reading):

            self.odometer_reading = mileage
        else:
            print("You can't re-roll the odometer!")




my_car = Car( make= input("Enter your car's make: "), model= input("Enter model: "),year= input("Enter year: "))
print(my_car.get_descriptive_name())
my_car.update_odometer(input("Enter car's mileage: "))
my_car.read_odometer()

your_car = Car(make= input("Enter your car's make: ") , model= input("Enter car's model: "), year= input("Enter year: "))
print(your_car.get_descriptive_name())
your_car.update_odometer(input("Enter car's mileage: "))
your_car.read_odometer()

