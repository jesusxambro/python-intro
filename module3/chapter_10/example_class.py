import random


class Car():
    def __init__(self, max_fuel_level):
        self.make = "Volvo"
        self.model = "V60"
        self.fuel_level = 10
        self.max_fuel_level = 20
    def drive(self, miles):
        self.fuel_level = self.fuel_level - miles * .7
    def get_fuel_level(self):
        return self.fuel_level

class Coin():
    def __init__(self):
        self.sideup = "Heads"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    def get_sideup(self):
        return self.sideup

def main():
    # coin = Coin()
    # print(coin.get_sideup())
    # coin.toss()
    # print(coin.get_sideup())
    my_car = Car(50)
    print(my_car.get_fuel_level())
    my_car.drive(20)
    print(my_car.get_fuel_level())

if __name__ == '__main__':
    main()

