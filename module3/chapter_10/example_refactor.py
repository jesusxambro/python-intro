from module3.chapter_10.Vegetable import Vegetable

def water_vegetable(vegetable_to_water):
    vegetable_to_water.water_vegetable()

def main():
    carrot = Vegetable("Carrot")
    carrot.water_vegetable()
    carrot.set_sunlight_required(.5)
    marigold = Vegetable("Marigold")
    print(f"How much sunlight does the {carrot.name}?  {carrot.get_sunlight_requirement() * 100}%")

    my_garden = [carrot, marigold]
    for vegetable in my_garden:
        if not vegetable.is_vegetable_watered():
            water_vegetable(vegetable)
        print(f"I have this vegetable: {vegetable.get_vegetable_name()} in my garden!")
        print(vegetable)

if __name__ == '__main__':
    main()