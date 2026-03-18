from models import Animal, Dog, Cat


def main():
    animal1 = Animal("Generic Animal", 5, "Gray")
    dog1 = Dog("Buddy", 3, "Brown", "Labrador")
    cat1 = Cat("Misty", 2, "White", True)

    animals = [animal1, dog1, cat1]

    for animal in animals:
        print(animal)
        print(animal.eat())
        print(animal.sleep())
        print(animal.speak())
        print("-" * 30)

    print(dog1.fetch())
    print(cat1.climb())


if __name__ == "__main__":
    main()