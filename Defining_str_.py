class CarRecord:
    def __init__(self):
        self.year_made = 0
        self.car_vin = ''

    # FIXME add __str__()
    def __str__(self):
        return print('Year: {}, VIN: {}'.format(self.year_made, self.car_vin))

my_car = CarRecord()
my_car.year_made = int(input("Enter car year made: "))
my_car.car_vin = input("Enter car vin: ")

print(my_car)

