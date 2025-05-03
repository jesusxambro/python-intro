class Vegetable():
    def __init__(self, name):
        self.name = name
        self.sunlight_required = 1
        self.is_watered = False
    def water_vegetable(self):
        self.is_watered = True
    def set_sunlight_required(self, sunlight_percentage):
        self.sunlight_required = sunlight_percentage
    def get_sunlight_requirement(self):
        return self.sunlight_required
    def is_vegetable_watered(self):
        return self.is_watered
    def get_vegetable_name(self):
        return self.name

    def __str__(self):
        watered = ""
        if self.is_watered:
            watered = "watered"
        else:
            watered = 'not watered'

        return (f"This is a {self.name}. It needs this much sunlight: {self.sunlight_required * 100}%."
                f"It is currently {watered}.")


def main():
    carrot = Vegetable("Carrot")
    carrot.water_vegetable()
    carrot.set_sunlight_required(.5)
    marigold = Vegetable("Marigold")
    print(f"How much sunlight does the {carrot.name}?  {carrot.get_sunlight_requirement() * 100}%")

    my_garden = [carrot, marigold]
    for vegetable in my_garden:
        print(f"I have this vegetable: {vegetable.get_vegetable_name()} in my garden!")

if __name__ == '__main__':
    main()